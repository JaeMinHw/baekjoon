import sys

input = sys.stdin.readline
N = int(input())


arr_N = [0] * N


arr_N = set(map(int, input().split()))

M = int(input())

arr_M = [0] * M


arr_M = list(map(int, input().split()))


for i in range(M):
    if arr_M[i] in arr_N:
        print("1")
    else:
        print("0")
