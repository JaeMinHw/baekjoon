def solution(schedules, timelogs, startday):
    answer = 0

    for i in range(len(timelogs)) :
        start_day_c = startday 
        c = 1
        if schedules[i] % 100 >= 50 :
            p_time_p = (schedules[i] // 100 + 1) * 100 + (((schedules[i] +10 ) % 100) % 60)
            p_time_m = schedules[i] - 10
        elif schedules[i] % 100 < 50 and schedules[i] % 100 >= 10 :
            p_time_p = schedules[i] + 10
            p_time_m = schedules[i] - 10
        elif schedules[i] % 100 < 10 :
            p_time_p = schedules[i] + 10
            p_time_m = (schedules[i] // 100 -1) * 100 + 60 - ((schedules[i] % 100) + 10 )
        
        for j in range(len(timelogs[i])) :
            today = (start_day_c - 1) % 7 + 1
            if today > 5 :
                start_day_c += 1
                
            else :
                start_day_c +=1
#                 50분에서 10분 더하면 시간이 바뀌어야하는데 그냥 60으로 되면 계산 틀림 -> %100을 했을 때 숫자를 가지고 계산하고 만약 시간이 넘어간다면 /100을 하고 더하고 하는 방식
                if p_time_p >= timelogs[i][j] :
                    c += 1
                else :
                    c = 0
                    break
            
        if c != 0 :
            answer +=1
                
    return answer