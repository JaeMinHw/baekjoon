# 그러면 1부터 100까지 자연수에 대해 "합의 제곱"과 "제곱의 합"의 차이는 얼마입니까?

sum =0
sum2 = 0
for i in range(1, 101):
    sum += i
    sum2 += i*i

print((sum*sum) - sum2)
