import sys

input = sys.stdin.readline

N = int(input())

arr = []

a = list(map(int, input().split()))


a = sorted(a)
sum = 0
for i in range(N):
    for j in range(i+1):
        sum += int(a[j])

print(sum)