import sys

input = sys.stdin.readline

N = int(input())

arr = [0] * N

for i in range(N):
    arr[i] = list( input().split())


arr.sort(key=lambda x: int(x[0])) 


for i in range(N):
    print(arr[i][0], arr[i][1] )
    

# 디렉터리