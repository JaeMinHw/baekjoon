arr = set(list([]))

for i in range(10001):
    a= i
    while i > 0:
        a += int(i%10)
        i = int(i/10)

    arr.add(a)
# arr= sorted(arr)

# print(arr)


for i in range(10001):
    if i not in arr :
        print(i)