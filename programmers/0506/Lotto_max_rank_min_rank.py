def solution(lottos, win_nums):
    answer = []
    arr = [6,5,4,3,2,1]
    count = 0

    for i in range(6):
        if lottos[i] in win_nums :

            count += 1
    if count == 0 and lottos.count(0) == 0 :
        answer.append(arr[0])
    else :
        answer.append(arr[count+lottos.count(0)-1])
    if count == 0 :
        count = 1
    answer.append(arr[count-1])
    
    return answer