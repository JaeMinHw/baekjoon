import sys

input = sys.stdin.readline

N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

sor_arr = sorted(arr, key=lambda x : (x[1], x[0]))


for i in sor_arr:
    print(*i)

