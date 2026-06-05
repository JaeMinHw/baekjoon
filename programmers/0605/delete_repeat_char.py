def solution(s):
    answer = ['']
    s = list(s)
    lis = []

    for i in range(len(s), 0, -1) :
        if len(lis) == 0:
            lis.append(s[-1])

            s.pop()
        else :
            if lis[-1] == s[-1] :
                s.pop()
                lis.pop()
            else :
                lis.append(s[-1])
                s.pop()
        if len(lis) == 0:
            answer = 1
        else :
            answer = 0
    return answer

print(solution("baabaa"))