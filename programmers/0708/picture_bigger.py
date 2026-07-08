def solution(picture, k):
    answer = []
    for j in range(len(picture)) :
        for i in range(k):
        
            a = ''
            for q in range(len(picture[j])):
                for l in range(k) :
                    a += picture[j][q]
            print(a)
    return answer

print(solution([".x.x.", "x.x.x", ".x.x."], 2))