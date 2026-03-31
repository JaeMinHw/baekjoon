S = input()
arr= [0,3,6,9,12,15,18,21,24,27]
sum = 0
count = 0
for i in range(0,13):
    if S[i] != '*':
        if i % 2 != 0 :
            sum += int(S[i]) * 3
        else :
            sum += int(S[i])
    else :
        count = i


if count %2 != 0:
    # 여기서 3의 배수로 구해지는 방법.
    for i in range(len(arr)):
        if (int(sum + arr[i] ) % 10) == 0:
            print(int(arr[i] / 3))
else :
    a = int(sum /10) + 1
    # print(a)
    a = a*10
    a = a - sum
    if a == 10 :
        print(a-10)
    else :
        print(a)