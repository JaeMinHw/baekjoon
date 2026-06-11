def solution(priorities, location):
    answer = 0
    i = 0
    count = 0
    while True :

        if priorities[i] == max(priorities):
            priorities.pop(i)
            count +=1
            if i < location :
                location -= 1
            elif i == location :
                break
            
        else :
            i += 1

        
        if i > len(priorities)-1:
            i = 0

    return count


print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))