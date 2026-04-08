import sys

input = sys.stdin.readline

n = int(input())

dp_arr = [0] * (n +1)

dp_arr[1] = 1

for i in range(2, n+1):
    if dp_arr[i] == 0:
        dp_arr[i] = dp_arr[i-1] + dp_arr[i-2]
    

print(dp_arr[n])
