import sys
input = sys.stdin.readline
list = []
d = {}
temp = []
n = int(input())
list.extend(input().split())
m = int(input())
temp.extend(input().split())

map(int,temp)

for i in temp:
    d[i] = int(0)



for i in list:
    if i in d:
        d[i] +=1

for i in temp:
    print(d[i],end=" ")
