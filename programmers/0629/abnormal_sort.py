
def solution(numlist, n):
    answer = []
    arr = []
    
    for i in range(len(numlist)):
        arr.append((numlist[i], (numlist[i]-n) * (numlist[i]-n)))
    print(arr)
    arr.sort(key = lambda x:(x[1], -x[0]))
    print(arr)
    for i in range(len(arr)):
        answer.append(arr[i][0])
    return answer