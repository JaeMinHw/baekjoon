N = int(input())

arr = [0] * (N+1)

arr[0] = 0
arr[1] = 0
# arr[2] = 1
# arr[3] = 1
# arr[4] = 2
# arr[5] = 3
# arr[6] = 2
# arr[7] = 3
# arr[8] = 3
# arr[9] = 2
# arr[10] = 3
# arr[11] = 4
# arr[12] = 3
# arr[13] = 4
# arr[14] = 4
# arr[15] = 4
# arr[16] = 4
# arr[17] = 5
# arr[18] = 3
# arr[19] = 4
# arr[20] = 4
# arr[21] = 4
# arr[22] = 5
# arr[23] = 6
# arr[24] = 4
# arr[25] = 5
# arr[26] = 5
# arr[27] = 3
# arr[28] = 4
# arr[29] = 5
# arr[30] = 4


if N > 1:
    for i in range(2, N+1):
        
        if arr[i] == 0:
            if i %2 == 0:
                a = arr[int(i/2)] +1
                b = arr[i-1] +1
                c = min(a,b)
                if i%3 == 0:
                    a = arr[int(i/3)] +1
                    
                    d = min(a,c)
                else :
                    d = c
                
                arr[i] = d
            elif i%3 == 0:
                a = arr[int(i/3)] +1
                b = arr[i-1] +1
                d = min(a,b)
                arr[i] = d
            else :
                e = arr[i-1] +1
                arr[i] = e

print(arr[N])
# print(arr[int(int(N/2)/2)])

# 0부터 채워가는데 본인의 2를 곱한 수와 3을 곱한 수는 +1이 되는 방식으로 올라가기

# 소수의 경우 1을 뺀 숫자의 +1