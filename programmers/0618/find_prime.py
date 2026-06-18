import itertools
import math
def solution(numbers):
    answer = 0
    numbers = list(map(str,numbers))
    numbers_set = set()
    for i in range(1, len(numbers)+1):
        check = list(itertools.permutations(numbers, i))
        count = len(check)
        # print(count, check)
        for j in range(count):
            if int(''.join(check[j])) > 1:
                numbers_set.add(int(''.join(check[j])))

    numbers_set = list(numbers_set)

    for i in range(len(numbers_set)):
        flag = 0
        for j in range(2, int(math.sqrt(int(numbers_set[i]))) +1) :
            if int(numbers_set[i]) % j == 0 :
                flag = 1
                print(i)
                break
        if flag == 0 :
            answer += 1

    return answer



print(solution("17"))