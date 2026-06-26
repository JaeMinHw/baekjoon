def solution(a, b, c, d):
    answer = 0
    lis = []
    che = []

    arr = {1:0, 2:0,3:0,4:0,5:0,6:0}
    arr[a]+=1
    arr[b]+=1
    arr[c]+=1
    arr[d]+=1
    for i in range(1, 6+1):
        if arr[i] == 0 :
            lis.append(i)
        else :
            che.append(i)

    for i in range(len(lis)):
        del arr[lis[i]]

    print(che)
    if len(arr) == 1:
        return a * 1111
    elif len(arr) == 2 :
        if arr[che[0]] == arr[che[1]] :
            return (che[0] + che[1]) * (max(che[0], che[1]) - min(che[0],che[1]))
        else :
            for i in range(2):
                if arr[che[i]] == 3 :
                    a = che[i]
                else :
                    b = che[i]

            return ((10 * a) + b) **2 
    
    elif len(arr) == 3:
        sum = 1
        for i in range(len(che)) :
            if arr[che[i]] == 1 :
                sum *=che[i]
        return sum
    else :
        return min(a,b,c,d)

        
    # for i in range(len(arr)):
    #     if len(arr) == 1:
    #         return arr[0] * 1111
    #     elif len(arr) == 2 :
    #         if arr[0] == arr[1] :
    #             return (arr[0] + arr[1]) * (max(arr[0], arr[1]) - min(arr[0],arr[1]))
    #         else :
    #             return (10 * max(arr[0],arr[1]) + min(arr[0],arr[1])) **2 
    #     elif len(arr) == 3 :
    #         return min(arr[0], arr[1])
    


print(solution(2,2,2,2))
print(solution(1,1,1,4))
print(solution(6,3,3,6))
print(solution(6,4,2,5))
print(solution(2,5,2,6))

