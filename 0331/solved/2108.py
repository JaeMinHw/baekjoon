import sys

input = sys.stdin.readline

N = int(input())
a = [0]  * N 

sum = 0


count = {}

for i in range(N):
    a[i] = int(input())
    sum += a[i]

    if a[i] not in count.keys() :
        count[a[i]] = 1
    else :
        count[a[i]] += 1




value_max = max(count.values())
sort_count = sorted(count.keys())
flag = 0
c_keys = 0
c_value = 0




if N != 1:
    for i in sort_count:

        if count[i] == value_max:
            flag += 1
            c_keys = i
        if flag == 2:
            c_keys = i
            break

else :
    c_keys = a[0]









sort_a = sorted(a)

print(round(sum / N))
print(sort_a[int(N/2)])
print(c_keys)
print(sort_a[N-1] - sort_a[0])









# --------------------------------- 아래는 기존에 풀었던 코드. 시간초과

import sys

input = sys.stdin.readline
N = int(input())
a = [0]  * N 

sum = 0


val = 0

max_num = 0
flag = 0
for i in range(N):
    a[i] = int(input())
    sum += a[i]

uniq_a = sorted(list(set(a)))
val_arr = [0] * len(uniq_a)

count = [0] * len(uniq_a)
for i in range(len(uniq_a)):

    for j in range(N):
        if uniq_a[i] == a[j]:
            count[i] += 1


    if count[i] > max_num  :
        flag = 0
        max_num = count[i]
        val_arr[i] = uniq_a[i]
        val =  uniq_a[i]

    elif count[i] == max_num : 
        flag = 1
        val_arr[i] = uniq_a[i]


max_c = max(count)
max_flag = 0
last_val = 0

if flag == 1:
    if N != 1:
        for i in range(len(uniq_a)):
            if max_c == count[i]:
                max_flag += 1
            if max_flag == 2:
                last_val = uniq_a[i]
                break
    else :
        last_val = uniq_a[0]    

else : 
    last_val = val

sort_a = sorted(a)

print(round(sum / N))
print(sort_a[int(N/2)])
print(last_val)
print(sort_a[N-1] - sort_a[0])
