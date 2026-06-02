def solution(k, tangerine):
    answer = 0
    tangerine_dict = {}
    for i in range(max(tangerine)):
        tangerine_dict[i+1] = 0

    for i in range(len(tangerine)):
        if tangerine_dict[tangerine[i]] >0:
            tangerine_dict[tangerine[i]] += 1
        else :
            tangerine_dict[tangerine[i]]= 1
            
    tangerine_dict = sorted(tangerine_dict.items(), key= lambda item:item[1], reverse = True)
    sum = 0
    
    for i in range(len(tangerine_dict)):
        sum += tangerine_dict[i][1]
        answer += 1
        if sum >= k :
            break
    return answer

solution(6, [1, 3, 2, 5, 4, 5, 2, 3])