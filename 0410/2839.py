import sys

input = sys.stdin.readline

N = int(input())

loop_num = int(N / 5)

result = 0
rest = 0

while loop_num > -1 :

    rest = N - loop_num * 5
    if rest % 3 == 0:
        result = loop_num + int(rest / 3)
        break
    else :
        loop_num -= 1

if result != 0:
    print(result)
else :
    print("-1")