def solution(n):
    ans = 1
    
    while n > 1:
        if n %2 != 0 :
            ans += 1
            n = int(n//2)
        else :
            n = int(n/2)
            
    return ans