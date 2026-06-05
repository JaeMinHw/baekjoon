def solution(n):
    answer = 0

    binary_str = bin(n)
    binary_str = binary_str[2:] 
    print(binary_str.count('1'))
    resu = binary_str.count('1')
    while True:
        n = n+1
        binary_str = bin(n)
        binary_str = binary_str[2:] 
        if binary_str.count('1') == resu:
            break
    answer = n
        
    return answer