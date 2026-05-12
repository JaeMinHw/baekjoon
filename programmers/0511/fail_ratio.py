def solution(N, stages):
    answer = []
    total = len(stages)
    arr = {}

    for i in range(N):
        count_sta = stages.count(i+1)
        if count_sta != 0:
            arr[i+1] = count_sta / total

            total -= count_sta
        else :
            arr[i+1] = 0
    print(arr)
    arr = dict(sorted(arr.items(),  key=lambda x: x[1] ,reverse=True))
    print(arr)
    
    for key in arr.keys():
        answer.append(key)
    return answer


solution(5, [2, 1, 2, 6, 2, 4, 3, 3])