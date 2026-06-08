def solution(n):
    answer = 1
    for i in range(1, int(n/2)+1):
        di = n - (2*i)
        di_plus = di + i
        min_div = min(i, di)
        a = 1
        for j in range(min_div):
            a *= di_plus
            di_plus -= 1
        
        b = 1
        for k in range(1, min_div+1):
            b *= k
        answer += int(a//b)
        answer = answer %1234567
    return answer