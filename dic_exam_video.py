import cv2
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import time

# ==========================================
# 1. 설정값
# ==========================================
VIDEO_SOURCE = 'C:/Users/admin_user/Desktop/dic_test.mp4' 
BUILDING_HEIGHT_M = 0.3    # 추적할 상/하단 사이의 실제 수직 거리 (m)
HEIGHT_CM = BUILDING_HEIGHT_M * 100

clahe = cv2.createCLAHE(clipLimit=2.5, tileGridSize=(8,8))

def preprocess(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return clahe.apply(gray)

def find_best_feature_in_roi(gray_img, roi):
    x, y, w, h = roi
    x, y = max(0, x), max(0, y)
    h_img, w_img = gray_img.shape
    w, h = min(w, w_img - x), min(h, h_img - y)
    sub_img = gray_img[y:y+h, x:x+w]
    if sub_img.size == 0: return x, y
    corners = cv2.goodFeaturesToTrack(sub_img, maxCorners=1, qualityLevel=0.01, minDistance=10)
    if corners is not None:
        cx, cy = corners[0][0]
        return int(x + cx), int(y + cy)
    return x + w//2, y + h//2

# ==========================================
# 2. 초기화 및 영역 설정
# ==========================================
cap = cv2.VideoCapture(VIDEO_SOURCE)
ret, first_frame = cap.read()
if not ret: exit()

gray_init = preprocess(first_frame)
H_img, W_img = gray_init.shape

print("\n[실시간 시각 적용 모드]")
roi_building = cv2.selectROI("Step 1: Building Area", first_frame, False)
roi_fixed = cv2.selectROI("Step 2: Fixed Reference", first_frame, False)
cv2.destroyAllWindows()

# 자동 특징점 추출
tx, ty = find_best_feature_in_roi(gray_init, (roi_building[0], roi_building[1], roi_building[2], int(roi_building[3]*0.15)))
bx, by = find_best_feature_in_roi(gray_init, (roi_building[0], roi_building[1] + int(roi_building[3]*0.85), roi_building[2], int(roi_building[3]*0.15)))
rx, ry = find_best_feature_in_roi(gray_init, roi_fixed)

T_W, T_H = 60, 60 
def get_safe_tpl(img, x, y):
    x1, y1 = max(0, x - T_W // 2), max(0, y - T_H // 2)
    x2, y2 = min(W_img, x1 + T_W), min(H_img, y1 + T_H)
    x1, y1 = max(0, x2 - T_W), max(0, y2 - T_H)
    return img[y1:y2, x1:x2], (x1 + T_W//2, y1 + T_H//2)

tpl_top, p_t0 = get_safe_tpl(gray_init, tx, ty)
tpl_bot, p_b0 = get_safe_tpl(gray_init, bx, by)
tpl_ref, p_r0 = get_safe_tpl(gray_init, rx, ry)

v_pixel_dist = abs(p_t0[1] - p_b0[1])
if v_pixel_dist == 0: v_pixel_dist = 1

# ==========================================
# 3. 실시간 그래프 설정 (X축 실제 시각 적용)
# ==========================================
plt.ion()
fig, ax = plt.subplots(figsize=(10, 5))
line, = ax.plot([], [], 'b-', linewidth=1.5, label='Tilt Displacement')

ax.set_title("Building Tilt Monitoring (Actual Time)", fontsize=14)
ax.set_ylabel("Displacement (cm)", fontsize=12)
ax.set_xlabel("Current Time", fontsize=12)

# X축 포맷 설정: 시:분:초 형식
ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
fig.autofmt_xdate() # 시간 라벨이 겹치지 않게 회전

ax.grid(True, linestyle='--', alpha=0.7)
ax.legend(loc='upper right')
value_text = ax.text(0.02, 0.95, '', transform=ax.transAxes, fontsize=12, fontweight='bold', color='red')

history_cm = []
time_history = [] # 실제 datetime 객체를 저장

print("\n▶ 분석 시작 (현재 시각 기준으로 기록됩니다)")
cv2.namedWindow("Smart DIC Monitor", cv2.WINDOW_NORMAL)
# ==========================================
# 4. 분석 루프
# ==========================================
while True:
    ret, frame = cap.read()
    if not ret: break
    gray_frame = preprocess(frame)

    def track_point(img, tpl):
        res = cv2.matchTemplate(img, tpl, cv2.TM_CCOEFF_NORMED)
        _, _, _, max_loc = cv2.minMaxLoc(res)
        return max_loc[0] + tpl.shape[1]//2, max_loc[1] + tpl.shape[0]//2

    curr_t = track_point(gray_frame, tpl_top)
    curr_b = track_point(gray_frame, tpl_bot)
    curr_r = track_point(gray_frame, tpl_ref)

    # 변위 계산
    shake_x = curr_r[0] - p_r0[0]
    net_move_top = (curr_t[0] - p_t0[0]) - shake_x
    net_move_bot = (curr_b[0] - p_b0[0]) - shake_x
    rel_tilt_px = net_move_top - net_move_bot
    tilt_cm = (rel_tilt_px / v_pixel_dist) * HEIGHT_CM

    # [핵심] 현재 시스템 시각 획득
    now = datetime.now()
    
    # 데이터 업데이트
    history_cm.append(tilt_cm)
    time_history.append(now)
    
    if len(history_cm) > 200: # 최근 200개 데이터 유지
        history_cm.pop(0)
        time_history.pop(0)

    # 그래프 갱신
    line.set_data(time_history, history_cm)
    value_text.set_text(f"Tilt: {tilt_cm:.3f} cm | Time: {now.strftime('%H:%M:%S')}")
    
    ax.relim()
    ax.autoscale_view()
    plt.pause(0.001)

    # 화면 시각화
    for p, color in [(curr_t, (255,0,0)), (curr_b, (0,255,0)), (curr_r, (0,0,255))]:
        cv2.drawMarker(frame, p, color, cv2.MARKER_CROSS, 20, 2)
    
    cv2.putText(frame, f"Time: {now.strftime('%H:%M:%S')} | Disp: {tilt_cm:.2f}cm", (20, 50), 
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
    
    cv2.imshow("Smart DIC Monitor", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()
plt.ioff()
plt.show()