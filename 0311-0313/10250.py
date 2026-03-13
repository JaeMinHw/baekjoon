T = int(input())
ch = 0
ho = 0
for i in range(T) :
    H, W, N = list(map(int, (input().split())))

    if N%H ==0 :
        ho = int(N/H)
        ch = int(H)
    else :
        ho = int(N/H) +1
        ch = int(N%H)
    
    if ho <10 :
        print(str(ch)+"0"+ str(ho))

    else :
        print(str(ch)+ str(ho))