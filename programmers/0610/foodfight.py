def solution(food):
    answer = ''
    lis = []
    for i in range(1, len(food) ) :
        for j in range(food[i] //2 ) :
            answer += str(i)
            lis.append(str(i))
        
    answer += '0'
    
    for i in range(len(lis)):
        answer += lis.pop()
    
    return answer