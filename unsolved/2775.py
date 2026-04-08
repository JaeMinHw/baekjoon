import sys
input = sys.stdin.readline

T = int(input())


# for i in range(T):
k = int(input())
n = int(input())
arr= [[0] * (k+1)] * (n+1)
for j in range(0,k+1):
    print("T", end = '')
    arr[0][j]= j+1


print(arr)