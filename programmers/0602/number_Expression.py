def solution(n):
    answer = 0


    for i in range(1, n+1):
        j = i
        sum = 0
        while sum <= n:
            sum += j
            j+=1
            if sum == n :
                answer += 1
        print(sum)
        
    return answer

print(solution(15))