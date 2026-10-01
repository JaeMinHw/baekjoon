# 소수를 크기 순으로 나열하면 2, 3, 5, 7, 11, 13, ... 과 같이 됩니다.

# 이 때 10,001번째의 소수를 구하세요.

def check_prime(check_num):
    c = 0
    for i in range(2, int(check_num ** 0.5 + 1)):
        if check_num % i == 0:
            c += 1
    if c >= 1 :
        return 0
    else :
        return 1


i = 0
num = 1
while (i != 10002) :
    if check_prime(num) == 1:
        i += 1
        print(i)
    num += 1

print(num-1)