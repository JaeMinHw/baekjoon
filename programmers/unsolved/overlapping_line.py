def solution(lines):
    answer = 0
    arr = []
    for i in range(len(lines)-1):
        for j in range(i+1, len(lines)):
            print(lines[i], lines[j])
    return answer

print(solution([[0, 1], [2, 5], [3, 9]]))