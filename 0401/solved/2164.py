from collections import deque

N = int(input())


if N==1:
    print("1")
    exit()

arr = deque([i+1 for i in range(N)])


while 1:
    arr.popleft()
    if (len(arr)==1): break

    arr.rotate(-1)
    

print(arr[0])