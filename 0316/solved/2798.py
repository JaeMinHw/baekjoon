N, M = map(int, input().split())

A = list(map(int, input().split()))


max = 0
sum = 0
result = 0

for i in range(len(A)-2) :
    for j in range(i+1,len(A)-1 ):
        for k in range(j+1, len(A)):
            sum = A[i] + A[j] + A[k]
            if sum < M+1 :
                if sum > max:
                    max = sum
                    result = sum


print(result)
