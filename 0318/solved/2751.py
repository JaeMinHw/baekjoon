import sys

input = sys.stdin.readline
N = int(input())

arr = [0] * N
for i in range(N):
    arr[i] = int(input())

sort_arr = sorted(arr)

for i in range(N):
    print(sort_arr[i])