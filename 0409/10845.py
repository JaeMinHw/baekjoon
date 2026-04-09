import sys

input = sys.stdin.readline

command_list = ['front','back', 'size','empty','pop',]

N = int(input())
arr = []
for i in range(N):

    command = list(input().split())

    if command[0] in command_list :
        len_arr = len(arr)
        if command[0] == 'front' :
            if len_arr != 0 :
                print(arr[0])
            else :
                print("-1")

        elif command[0] == 'back' :
            if len_arr != 0 :
                print(arr[len_arr - 1])
            else :
                print("-1")

        elif command[0] == 'size' :
            print(len_arr)
        elif command[0] == 'empty':
            if len_arr != 0 :
                print("0")
            else :
                print("1")
        elif command[0] == 'pop':
            if len_arr != 0 :
                pop_arr = arr.pop(0)
                print(pop_arr)
            else :
                print("-1")


    else :
        arr.append(command[1])

