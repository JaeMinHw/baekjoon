
def solution(sequence, k):
    answer = []

    for i in range(len(sequence)) :
        if sequence[i] == k :
            answer.append(i)
            answer.append(i)
            return answer


    for i in range(2, len(sequence)+1):
        a = sequence[0:i]

        su = 0
        for q in range(len(a)):
            su += a[q]
        # print(q, su)
        if su == k:
            answer.append(0)
            answer.append(i-1)
            return answer
        

        for j in range(1, len(sequence) -i +1) :
            
            su -= sequence[j-1]
            su += sequence[j+i]

            if su == k:
                answer.append(j)
                answer.append(j+i-1)

                return answer
            
            
        
    return answer


print(solution([1, 2, 3, 4,5], 7))