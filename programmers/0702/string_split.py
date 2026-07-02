def solution(s):
    answer = 1
    left = 1
    left_le = s[0]
    right = 0
    for i in range(1, len(s)-1):
        if s[i] == left_le :
            left+= 1
        else :
            right += 1
            if left == right :
                answer +=1
                left = 0
                right = 0
                left_le = s[i+1]

    return answer

print(solution("aaabbaccccabba"))