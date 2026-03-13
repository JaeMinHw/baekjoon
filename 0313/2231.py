N = int(input())
i =1
j = 1
sum = 0
result = 0
while i < N:
    sum = 0
    while j > 0 : 
        sum += j
        sum += j%10
        j = j/10


        if sum == N:
            result = sum
            
            j = 0

        j+= 1

    i+= 1

print(sum)



