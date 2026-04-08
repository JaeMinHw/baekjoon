import sys
input = sys.stdin.readline

T = int(input())

arr = [[0 for _ in range(15)] for _ in range(15)]


for i in range(15):
    arr[0][i] = int(i+1)
    arr[i][0] = 1

for i in range(T):
    k = int(input())
    n = int(input())
    for j in range(k+1):
        for a in range(n+1):
            if arr[j][a] == 0:
                arr[j][a] = arr[j-1][a] + arr[j][a-1]
    print(arr[k][n-1])


