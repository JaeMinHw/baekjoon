N = int(input())
arr = [''] * N
for i in range(N) :
    a = input()
    arr[i] = a


set_arr = set(arr)
set_arr = list(set_arr)


for i in range(1, 51):
    tem_arr = [''] * N
    for j in range(len(set_arr)):
        if len(set_arr[j]) == i :
            tem_arr[j] = set_arr[j]
    tem_arr = sorted(tem_arr)

    for k in range(len(tem_arr)):
        if len(tem_arr[k]) != 0: 
            print(tem_arr[k])
