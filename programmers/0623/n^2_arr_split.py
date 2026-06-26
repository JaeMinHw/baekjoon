def solution(n, left, right):
    answer = [0] * (right - left + 1)

    c = 0
    check = 0
    for i in range(left, right+1):
        row = i // n
        col = i % n

        if row > col:
            answer[c] = row + 1
        else:
            answer[c] = col + 1
        c += 1


    return answer


solution(3, 2, 5)