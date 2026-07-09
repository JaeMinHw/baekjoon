def solution(n):
    answer = 0
    arr = [0]
    for i in range(200):
        if i% 3 != 0:
            if '3' not in str(i) :
                arr.append(i)
        
    answer = arr[n]
    return answer