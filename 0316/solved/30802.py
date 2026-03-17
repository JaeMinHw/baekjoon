N = int(input())

si = list(map(int, input().split()))

t_t, p_t = map(int, input().split())

sum = 0
p_sum = 0
for i in range(len(si)):
    sum += int(si[i] / t_t)
    if si[i] % t_t > 0:
        sum += 1

    
p_sum = int(N / p_t)

p_rest = int(N % p_t)

print(sum)
print(p_sum, p_rest)