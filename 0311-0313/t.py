N = int(input())

max_result = [0] * 7
min_result = [0] * 7
min_re = [0] * 3
max_re = [0] * 3

for i in range(N):
    a= []
    a = list(map(int,input().split()))
    if i ==0:
        max_re = a
        min_re = a
        pass
 
    else :

        print(max_result)
        # max_re 구하는 코드
        max_result[0] = max_re[0] + a[0]
        max_result[1] = max_re[0] + a[1]
        max_result[2] = max_re[1] + a[0]
        max_result[3] = max_re[1] + a[1]
        max_result[4] = max_re[1] + a[2]
        max_result[5] = max_re[2] + a[1]
        max_result[6] = max_re[2] + a[2]
        
        print(max_result)
        if max_result[0] > max_result[1] :
            max_re[0] = max_result[0]
        else :
            max_re[0] = max_result[1]

        if max_result[2] > max_result[3] :
            if max_result[2] < max_result[4] :
                max_re[1] = max_result[4]
            elif max_result[2] > max_result[4] :
                max_re[1] = max_result[2]
        else :
            if max_result[3] < max_result[4] :
                max_re[1] = max_result[4]
            elif max_result[3] > max_result[4] :
                max_re[1] = max_result[3]

        if max_result[5] > max_result[6] :
            max_re[2] = max_result[5]
        else :
            max_re[2] = max_result[6]
        
        # max_result 0,1 비교 후 큰 값 구할 때는 큰거 남기기
        # 2,3,4 비교 후 큰 값 구할 때는 큰거 남기기
        # 5,6 비교 후 큰 값 구할 때는 큰거 남기기

        
        #min_re 구하는 코드
        
        # min_result[0] = min_re[0] + a[0]
        # min_result[1] = min_re[0] + a[1]
        # min_result[2] = min_re[1] + a[0]
        # min_result[3] = min_re[1] + a[1]
        # min_result[4] = min_re[1] + a[2]
        # min_result[5] = min_re[2] + a[0]
        # min_result[6] = min_re[2] + a[1]
   
        # if min_result[0] < min_result[1] :
        #     min_re[0] = min_result[0]
        # else :
        #     min_re[0] = min_result[1]

        

        # if min_result[2] < min_result[3] :
        #     if min_result[2] < min_result[4] :
        #         min_re[1] = min_result[2]
        #     elif min_result[2] > min_result[4] :
        #         min_re[1] = min_result[4]
        # else :
        #     if min_result[3] < min_result[4] :
        #         min_re[1] = min_result[3]
        #     elif min_result[3] > min_result[4] :
        #         min_re[1] = min_result[4]
        # if min_result[5] < min_result[6] :
        #     min_re[2] = min_result[5]
        # else :
        #     min_re[2] = min_result[6]




    # min_result 0,1 비교 후 작은 값 구할 때는 작은거 남기기
    # 2,3,4 비교 후 작은 값 구할 때는 작은거 남기기
    # 5,6 비교 후 작은 값 구할 때는 작은거 남기기



# 지금 왜 값이 중복되어서 더해지는거지?