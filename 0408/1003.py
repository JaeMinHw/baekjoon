import sys

input = sys.stdin.readline

n = int(input())

dp_arr_0 = [0] * (3)
dp_arr_1 = [0] * (3)

dp_arr_0[0] = 1
dp_arr_1[1] = 1

for j in range(n):
    k = int(input())
    dp_arr_0 = [0] * (3)
    dp_arr_1 = [0] * (3)

    dp_arr_0[0] = 1
    dp_arr_1[1] = 1
    if k == 0:
        print(dp_arr_0[0], dp_arr_1[0])
    elif k == 1:
        print(dp_arr_0[1], dp_arr_1[1])
    else :
        for i in range(2, k+1):

            dp_arr_0[2] = dp_arr_0[1] + dp_arr_0[0]
            dp_arr_1[2] = dp_arr_1[1] + dp_arr_1[0]
            dp_arr_0[0] = dp_arr_0[1]
            dp_arr_0[1] = dp_arr_0[2]
            dp_arr_1[0] = dp_arr_1[1]
            dp_arr_1[1] = dp_arr_1[2]


        print(dp_arr_0[2], dp_arr_1[2])

