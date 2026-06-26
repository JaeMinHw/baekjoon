def solution(numbers):
    answer = [-1] * len(numbers)
    st = [0]
    for i in range(1, len(numbers)):
        print(st)
        j = 0
        flag = 0
        while j < len(st):
            if numbers[i] > numbers[st[j]] :
                answer[st[j]] = numbers[i]
                del st[j]
                
            elif numbers[i] < numbers[st[j]]:
                flag = 1
            st.append(i)
            j += 1
        
    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
