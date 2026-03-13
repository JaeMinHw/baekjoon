while 1:
    S = list(map(int, input().split()))

    if S[0] ==0 and S[1] == 0 and S[2] == 0 :
        break
    S = sorted(S)
    if(S[2] * S[2] == S[0] * S[0] + S[1] * S[1]):
        print("right")
    else :
        print("wrong")
