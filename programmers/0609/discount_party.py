
def solution(want, number, discount):
    answer = 0
    for i in range(len(want)):
        if discount.count(want[i]) < number[i] :
            answer = 0

            return answer
    count = 0
    for i in range(len(discount) - 10 +1) : 
        
        arr = discount[i:i+10]
        flag = 0
        for j in range(len(want)):
            if arr.count(want[j]) < number[j] or arr.count(want[j]) > number[j] :
                flag = 1
        if flag == 0 :
            count += 1 
            
    return count