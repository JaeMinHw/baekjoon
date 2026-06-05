
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    sqrt = yellow ** (1/2) 
    # 정사각형 처리 완료
    if sqrt == int(sqrt) :
        sqrt +=2
        answer.append(sqrt)
        answer.append(sqrt)
        
    else :
        for i in range(3, int(total/2)):
            print(i)
            if total % i == 0 :
                if (i-2) * (int(total/i)-2) == yellow :
                    answer.append(i)
                    answer.append(int(total/i))
                    break

    answer.sort(reverse=True)
    return answer

print(solution(10, 2))