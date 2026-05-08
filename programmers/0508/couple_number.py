def solution(X, Y):
    answer = ''
    num_dic = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    num_dic2 = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    
    arr_y = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    X = list(map(int,X))
    Y = list(map(int,Y))

    for i in X :
        num_dic[i] += 1

    for i in Y :
        num_dic2[i] += 1

    for i in range(10):
        if num_dic[i] != 0 and num_dic2[i] != 0 :
            arr_y[i] = min(num_dic[i], num_dic2[i])
    print(arr_y)

    

    for i in range(9,-1, -1):

        if arr_y[i] != 0 :
            for j in range(arr_y[i]) :

                answer += str(i)

    if answer == '' :
        answer = "-1"
    elif answer[0] == '0' :
        answer = "0"


    return answer


print(solution("100", "123450"))