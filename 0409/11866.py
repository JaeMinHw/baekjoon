import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())

josep_arr = deque([i + 1 for i in range(N)] )

pop_josep_arr = [] 
josep_arr.rotate(-(K-1))
for i in range(N):
   
    pop_josep_arr.append(josep_arr[0])
    del josep_arr[0]
    josep_arr.rotate(-(K-1))

print("<", end = '')
for i in range(N-1):
    print(pop_josep_arr[i], end = ', ')

print(pop_josep_arr[N-1], end = '')

print(">", end = '')