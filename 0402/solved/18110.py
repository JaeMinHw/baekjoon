import sys

input = sys.stdin.readline

def half_num(num):
    if num - int(num) ==0.5:

        if int(num ) %2 == 0:

            return round(num) +1
    return round(num) 


N = int(input())

N15 = round(N * 0.15)
if N != 0:


    if N * 0.15 - N15 ==0.5:
        if int(N15) %2 == 0:
            N15 += 1

    sum = 0
    arr = [0] * N
    for i in range(N):
        a = int(input())
        arr[i] = a 
   

    sort_arr = sorted(arr)
    if N == 1:
        print(arr[0])
        exit()
    elif N == 2:
        print(half_num((sort_arr[0] + sort_arr[1]) / 2))
        exit()




    a = len(sort_arr)
    del sort_arr[0:N15]
    

    del sort_arr[len(sort_arr)-N15 : ]

    for i in range(len(sort_arr)):
        sum += sort_arr[i]
    
    # print(round(sum / (len(sort_arr))))
    # 만약 18.5라면 18로 나오는 상황. 
    print(half_num(sum / (len(sort_arr))))
    
else:
    print("0")