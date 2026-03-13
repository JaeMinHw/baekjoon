N = int(input())

cnt = 0
flag = 0
a= list(map(int, input().split()))

for i in range(N) :
    flag = 0
    if a[i] == 1:
        continue
    
    if a[i] == 2:
        cnt += 1
        continue
    for j in range( int(a[i] / 2) ):

        if  int(a[i]) % (j+2) == 0:

            flag = 1
            
            continue
        
    if flag == 0 :
        cnt += 1

print(cnt)