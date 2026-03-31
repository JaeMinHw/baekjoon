N = int(input())
sum = 1
for i in range(1, N+1) :
    sum *= i

str_sum = str(sum)

flag = 0
sum = 0
for i in range(0, len(str_sum)):
    if flag == 0 and str_sum[len(str_sum)- i -1] == '0':
        sum += 1
    else :
        flag = 1
        pass


print(sum)