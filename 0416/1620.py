import sys

input = sys.stdin.readline

N, M = map(int, input().split())

def reverse_dict(dictionary):
    return dict(map(reversed, dictionary.items()))

poket_list = {}

for i in range(N):
    a = input().replace("\n","")
    poket_list[a] = i
revers_poket_list = reverse_dict(poket_list)

# print(revers_poket_list)
for i in range(M):
    a = input().replace("\n","")
    
    if a not in poket_list:

        print(revers_poket_list.get(int(a)-1))
    else :
        print(poket_list.get(a)+1)