N = int(input())
result = 0

str_N = str(N)
for i in range(N) :
    cal = 0
    if i < 10:
        cal = i *2
    else :
        str_i = str(i)
        cal += i
        for j in range(len(str_i)):
            cal += int(str_i[j])
            

    if N == cal :
        result = i

        break

print(result)