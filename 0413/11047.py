import sys

input = sys.stdin.readline

N, K = map(int, input().split())

arr = [0] * N

for i in range(N):
    arr[i] = int(input())
count = 0

min = K
for i in range(N):
    money = K
    if K / arr[N-i-1] > 0 :
        coin = N-i-1
        count = 0

        while coin > -1 :
            count += int(money / arr[coin])
            money = money % arr[coin]
            coin -= 1

        if count < min :
            min = count
        

print(min)