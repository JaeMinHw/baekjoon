re = 0
a = 0
b = 1
c = 1
while(c < 4000000):
    
    if c < 4000000 and c % 2 == 0:
        re += c
        print(c)
    a = b
    b = c
    c = a+b
    
print(re)
    