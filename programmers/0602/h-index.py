# def solution(citations):
#     answer = 0
#     citations = sorted(citations)
#     print(citations)
#     len_citations = len(citations)
#     for i in citations:
#         print(i, len_citations - citations.index(i))
#         if i == len_citations - citations.index(i) :
#             answer = i

#     return answer

def solution(citations):
    answer = 0
    max_for = max(citations)
    
    for i in range(1, max_for+1):
        count = 0
        for j in range(len(citations)):
            if i <= citations[j] :
                count += 1
        if i <= count :
            answer = i
    return answer



print(solution([4,4,4,4,4]))