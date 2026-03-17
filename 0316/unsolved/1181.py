N = int(input())
arr = [''] * N
for i in range(N) :
    a = input()
    arr[i] = a


set_arr = set(arr)
set_arr = sorted(set_arr)
list_arr = list(set_arr)
for i in range(len(list_arr)):
    print(list_arr[i])