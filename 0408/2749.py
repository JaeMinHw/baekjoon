import sys

input = sys.stdin.readline

mod_n = 1000000

n = int(input())

dp_arr = [0] * 3
# co = n % 187500

co = n % 1500000

dp_arr[1] = 1
result = 1

for i in range(2, co+1):
    dp_arr[0] = dp_arr[0] %mod_n
    dp_arr[1] = dp_arr[1] %mod_n
    dp_arr[2] = (dp_arr[0] + dp_arr[1]) % mod_n
    result = dp_arr[2] 

    dp_arr[0] = dp_arr[1]
    dp_arr[1] = dp_arr[2]

    
print(result)



# import sys
# import csv

# input = sys.stdin.readline
# mod_n = 100000
# n = int(input())

# dp_arr = [0] * 3
# co = n
# dp_arr[1] = 1
# result = 0

# # 'w' 모드로 파일을 열어 writer 객체를 생성합니다.
# with open('output.csv', 'w', newline='', encoding='utf-8') as f:
#     writer = csv.writer(f)
    
#     # 초기값 0과 1을 먼저 씁니다. (한 줄에 하나씩 기록하는 방식)
#     writer.writerow([dp_arr[0]])
#     writer.writerow([dp_arr[1]])

#     for i in range(2, co):
#         dp_arr[0] = dp_arr[0] % mod_n
#         dp_arr[1] = dp_arr[1] % mod_n
#         dp_arr[2] = (dp_arr[0] + dp_arr[1])  # 오버플로우 방지를 위해 % 연산 추가 권장
        
#         result = dp_arr[2]
        
#         # 반복문이 돌 때마다 실시간으로 파일에 씁니다.
#         writer.writerow([result])
        
#         # 콘솔 출력 (필요 없으면 삭제 가능)
#         # print(result, end=', ')
        
#         dp_arr[0] = dp_arr[1]
#         dp_arr[1] = dp_arr[2]

# print(f"\n파일 기록 완료: output.csv (최종 결과: {result})")