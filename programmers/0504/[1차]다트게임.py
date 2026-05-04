def solution(dartResult):
    answer = 0
    list_dart = list(dartResult)

    a = 0
    b = 0
    c= []
    len_dart = len(list_dart)
    for i in range(len_dart) :
        if list_dart[i] == '1' and list_dart[i+1] == '0' :
            list_dart[i] = '10'
            
            c.append(i+1)
            len_dart -= 1
    if len(c) != 0:

        for index in sorted(c, reverse=True):
            del list_dart[index]
    
    for i in range(len(list_dart)) :
        
        if list_dart[i] == 'S' or list_dart[i] == 'D' or list_dart[i] == 'T':
            if list_dart[i] == 'S' :
                a = a ** 1
            elif list_dart[i] == 'D' :
                a = a ** 2
            elif list_dart[i] == 'T' :
                a = a ** 3
        elif list_dart[i] == '*' or list_dart[i] == '#':
            if list_dart[i] == '#' :
                a = a * -1
            elif list_dart[i] == '*':
                answer -= b
                b = b * 2  # Apply the double score to the previous round as well
                a = a * 2
                answer += b
        elif int(list_dart[i]) >= 0 and int(list_dart[i]) <= 10:
            answer += a
            b = a
            a = int(list_dart[i])
        

    answer += a

    return answer

solution("10D4S10D")