import sys

input = sys.stdin.readline

T = int(input())

arr = [''] * T

check = [0,1]

for i in range(T):
    a = input()
    arr[i] = a
    arr_n = [0] * (len(a)-1)
    flag = 0
    for j in range(len(a)):
        k = a[j]
        if k == '(':
            arr_n[j] = 0
        elif k == ')':
            arr_n[j] = 1
        
    
    # arr_n.count(0)
    if arr_n.count(0) != arr_n.count(1) :
        flag = 1
    else :
        # 여기에 이제 매칭을 하는 코드 작성
        while flag == 0 and len(arr_n) != 0:
            arr_n_index_0 = arr_n.index(0)
            arr_n_index_1 = arr_n.index(1)
 
            if arr_n_index_1 == 0 or arr_n_index_0 == (len(arr_n) -1):

                flag = 1
                break
            else :

                if arr_n[(arr_n_index_1 -1)] == 0 :
                    del arr_n[arr_n_index_1]
                    del arr_n[arr_n_index_1-1]

                else :

                    flag = 1
                    break
                    

    if flag == 0 :
        print("YES")
    else :
        print("NO")

        
