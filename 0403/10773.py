import sys

input = sys.stdin.readline

N = int(input())
sum = 0
arr = [0] * N
for i in range(N):
    a= int(input())
    if a == 0:
        p = arr.pop()
        sum -= p
    else :
        sum += a

print(sum)