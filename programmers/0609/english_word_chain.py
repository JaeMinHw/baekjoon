def solution(n, words):
    answer = []
    flag = 0
    duplicate_check = {}
    kick = 0
    for i in range(1, len(words)):

        if words[i-1][-1] != words[i][0] :
            flag = i + 1
            kick = 1
            
        if words[i-1] in duplicate_check :
            flag = i
            kick = 1
            
        if kick == 1 :
            break
        else :
            duplicate_check[words[i-1]] = 1

    if kick != 1 :
        if words[-1] in duplicate_check :
            flag = len(words)

        else :
            duplicate_check[words[-1]] = 1
    if flag != 0:
        if flag%n != 0:
            b = flag//n + 1
        else :
            b = flag//n
        a = flag%(n)
        if a == 0 :
            a = n
        answer = [a,b]
    else :
        answer = [0,0]
    return answer

print(solution(3, ["aba", "aba", "bba"]))