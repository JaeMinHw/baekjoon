def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        # a = str(bin(arr1[i])[2:])
        # d = str(bin(arr2[i])[2:])
        # if len(a) != n :
        #     b = n-len(a)
        #     c = ''
        #     for j in range(b):
        #         c += '0'
        #     a = c+a
        # if len(d) != n :
        #     b = n-len(d)
        #     c = ''
        #     for j in range(b):
        #         c += '0'
        #     d = c+d
        q = int(arr1[i]) | int(arr2[i])
        
        
        q = str(bin(q)[2:])
        if len(q) != n :
            b = n-len(q)
            c = ''
            for j in range(b):
                c += '0'
            q = c+q
        ar = ''
        for k in range(n):
            
            if q[k] == '1':
                ar += '#'
            else :
                ar += ' '
        answer.append(ar)
    return answer