def solution(num_list, n):
    answer = [[] for _ in range(len(num_list) // n)]
    k = 0
    for i in range(len(num_list) // n) :
        for j in range(n) :
            print(answer)
            answer[i].append(num_list[k])
            k += 1
    return answer

print(solution([1, 2, 3, 4, 5, 6, 7, 8], 2))