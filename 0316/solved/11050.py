N, K = map(int, input().split())
sum = 1
for i in range(N-K+1, N+1) :
    sum = sum * i

for i in range(1, K+1) :
    sum = sum / i


print(int(sum))