import sys

input = sys.stdin.readline

N = int(input())

arr = []
re_arr = []
for i in range(N):
    a = list(map(int,input().split()))
    arr.append(a)


re_arr = [["".join(s.s)]]
re_arr.sort()

# print(re_arr)
# arr = re_arr[::-1]


# for i in arr:
#     print(*i)


# 디렉터리