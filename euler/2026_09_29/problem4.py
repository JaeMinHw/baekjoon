max_num = 0
for i in range(900, 1000):
    for j in range(900, 1000):
        a = i*j
        b = str(i*j)

        revers_a = b[::-1]
        if a == int(revers_a) :
            if max_num < a :
                max_num = a 

print(max_num)