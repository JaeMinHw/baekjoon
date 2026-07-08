import math
def solution(a, b):
    answer = 0
    d = math.gcd(a,b)
    print(d)
    while d != 1 :
        d = math.gcd(a,b)
        if d != 1 :
            b = b // d
            a = a // d
        print(b)
    while 1 :
        if b % 2 == 0:
            b = b // 2
        elif b % 5 == 0 :
            b = b // 5
        else :
            break
    if b != 1 :
        answer = 2
    else :
        answer = 1
    return answer