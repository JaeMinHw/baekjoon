# def solution(strArr):
#     answer = 0
#     max_si = 0
#     a = 1
#     b = 0
#     for i in range(len(strArr)-1):
#         a = len(strArr[i])
#         for j in range(i, len(strArr)  ):
#             if a == len(strArr[j]) :
#                 b += 1
#         if max_si < b :
#             max_si = b
#             print(max_si)
#         b = 0
#     return max_si


def solution(strArr):
    answer = 0
    arr = []
    ar = dict()
    for i in range(len(strArr)):
        arr.append(len(strArr[i]))
        ar[len(strArr[i])] = ar.get(len(strArr[i]), 0) + 1
    print(max(ar.values()))
    return answer


print(solution(["a","bc","d","efg","hi"]))