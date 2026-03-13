arr = [0] * 42
cnrt = 0
for i in range(3):
    A = int(input())
    arr[A%42] = 1


for i in range(0,42):
    if arr[i] == 1:

        cnrt +=1

print(cnrt)