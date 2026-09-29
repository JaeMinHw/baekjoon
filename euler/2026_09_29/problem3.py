def prime_check(k):
    for i in range(2, int(k**0.5)+1):
        if k%i == 0:
            return 0
    return 1


a = 600851475143 
i =2
max_i = 0
while a > i :
    if prime_check(i) ==1 :
        if a % i == 0 :
            a = a /2
            max_i = i
            print(i, max_i)
    i+=1


    

