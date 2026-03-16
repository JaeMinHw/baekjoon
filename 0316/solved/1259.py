while 1:
    N = input()
    if int(N) == 0:

        break


    flag = 0
    for i in range(int(len(N) / 2)):
        if N[i] == N[len(N) - i-1] :
            pass
        else :
            flag = -1
            continue

    if flag == -1:
        print("no")
    else :
        print("yes")