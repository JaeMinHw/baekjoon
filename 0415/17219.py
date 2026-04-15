import sys

input = sys.stdin.readline

N, M = map(int, input().split())


add = {}
for i in range(N):
    a, b = map(str, input().split())
    add[a] = b


for i in range(M):
    a = input().replace("\n","")
    print(add.get(a))