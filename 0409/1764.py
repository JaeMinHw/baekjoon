import sys

input = sys.stdin.readline

N, M = map(int,input().split())

not_lis = set([])
not_see = set([])
re = []
for i in range(N):
    not_lis.add(input().replace("\n",""))


for i in range(M):
    not_see.add(input().replace("\n",""))


inter_set = not_lis.intersection(not_see)

sor_inter_set = sorted(inter_set)
len_sor = len(inter_set)
print(len_sor)

for i in range(len_sor):
    print(sor_inter_set[i])
