import sys

input = sys.stdin.readline


N = int(input())
if N != 0:

    N15 = round(N * 0.15)
    if int(N * 0.15) %2 == 0:
        N15 += 1

    sum = 0
    arr = [0] * N
    for i in range(N):
        a = int(input())
        arr[i] = a 
   




    sort_arr = sorted(arr)



    del sort_arr[0:N15]


    del sort_arr[len(sort_arr)-N15 : ]

    for i in range(len(sort_arr)):
        sum += sort_arr[i]
    
    # 만약 18.5라면 18로 나오는 상황. 
    print(round(sum / (len(sort_arr))))
    
else:
    print("0")