def solution(topping):
    answer = 0
    lis = {}
    for i in range(len(topping)):
        if topping[i] not in lis :
            lis[topping[i]] = 1
        else :
            lis[topping[i]] += 1
            
    arr1 = set()
    ri_count = len(lis)
    for i in range(len(topping) -1) :
        arr1.add(topping[i])
        lis[topping[i]] -= 1
        if lis[topping[i]] == 0:
            ri_count -=1
        
        if len(arr1) == ri_count :
            answer += 1
        
        

    return answer



