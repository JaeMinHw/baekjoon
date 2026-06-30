

def solution(dots):
    answer = 0
    dots = sorted(dots)
    max2 = -256
    min2 = 256
    min1 = 256
    max1 = -256
    for i in range(4):
        if max2 < dots[i][0] :
            max2 = dots[i][0]
        if min2 > dots[i][0] :
            min2 = dots[i][0]
            
    print(max2, min2)
    for i in range(4):
        if max1 < dots[i][1] :
            max1 = dots[i][1]
        if min1 > dots[i][1] :
            min1 = dots[i][1]
    
    answer = (max2- min2) * (max1 - min1)
    return answer