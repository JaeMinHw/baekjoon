N = int(input())
cnt = 0
i = 1
while 1:
    if N-6 * i >1 :
        cnt += 1
        N = N-6 * i
    
    else :
        if N == 1:
            cnt += 1
        else :
            cnt += 2
        break
    i+= 1

print(cnt)
