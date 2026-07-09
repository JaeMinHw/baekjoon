def solution(score):
    answer = []
    avg_arr = []
    for i in range(len(score)):
        avg_arr.append((score[i][0] + score[i][1] ) /2 )

    
    for i in range(len(avg_arr)):
        a = 1
        for j in range(len(avg_arr)):
            if avg_arr[i] <= avg_arr[j] :
                a += 1
            if avg_arr[i] == avg_arr[j] :
                a -= 1
        answer.append(a)

                
    return answer