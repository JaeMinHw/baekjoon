def solution(polynomial):
    answer = ''
    poly = polynomial.split(' ')
    print(poly[0].replace('x',''))
    x_count = 0
    num_count = 0
    for i in range(len(poly)):
        if 'x' in poly[i]:
            if len(poly[i]) == 1 :
                x_count +=1
            else :
                x_count += int(poly[i].replace('x',''))
        elif poly[i] != '+' :
            num_count += int(poly[i])

    if num_count != 0:
        if x_count > 1 :
            answer += str(x_count)+'x' + ' + ' + str(num_count)
        elif x_count == 1 :
            answer = 'x' + ' + ' + str(num_count)
        else :
            answer = str(num_count)
    else :
        if x_count != 1 :
            answer += str(x_count)+'x'
        else :
            answer += 'x'
    return answer