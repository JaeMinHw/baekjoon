import sys

input = sys.stdin.readline

check_arr = ['all','empty']
N = int(input())
S = []
for i in range(N):
    command = input().split()

    
    if command[0] in check_arr:
        if command[0] == "all":
            S =  [i+1 for i in range(20)]
        else :
            
            S = []

    else :
        if command[0] == "add":
            if int(command[1]) not in S:
                S.append(int(command[1]))
        elif command[0] == "remove":
            if int(command[1]) in S:
                del S[S.index(int(command[1]))]
        elif command[0] == "check":
            if int(command[1]) in S:
                print("1")
            else :
                print("0")
        elif command[0] == "toggle":
            if int(command[1]) in S:
                del S[S.index(int(command[1]))]
            else :
                S.append(int(command[1]))