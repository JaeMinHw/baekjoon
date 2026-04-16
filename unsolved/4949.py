import sys
input = sys.stdin.readline

while 1 :
    answer = input().replace("\n","")
    queue = []
    if answer == ".":
        break
    for i in range(len(answer)):
        if answer[i] == "[" or answer[i] == "]" or answer[i] == "(" or answer[i] == ")":
            queue.append(answer[i])

    if len(queue) %2 != 0:
        print("no")
    else :
        print(queue)