import sys

input = sys.stdin.readline

N, M = map(int, input().split())

chess_arr = []
chess_arr_2 =[]

for i in range(8):
    
    line = []
    line2 = []
    if i %2 == 0:
            
        for j in range(8):
            if j %2 == 0:
                line.append("W")
                line2.append("B")
            else :
                line.append("B")
                line2.append("W")

    else :
        for j in range(8):
            if j %2 == 0:
                line.append("B")
                line2.append("W")
            else :
                line.append("W")
                line2.append("B")
    
    line = ''.join(line)
    line2 = ''.join(line2)
    chess_arr.append(line)
    chess_arr_2.append(line2)
    



answer = []
for i in range(N):
    answer.append(input().replace("\n",""))


max = N * M
for i in range(N-7):
    for j in range(M-7):
        count = 0
        count2 = 0
        for q in range(i, i+8):
            for k in range(j, j+8):
                if answer[q][k] == chess_arr[q-i][k-j] :
                    count += 1
                elif answer[q][k] == chess_arr_2[q-i][k-j] :
                    count2 += 1

        min_count = min(count, count2)
        if min_count < max :
            max = min_count

print(max)

# min_num = 64
# for i in range(N-7):

    
#     for j in range(M-7):
#         count = 0
#         count2=  0
#         for o in range(8):
#             for k in range(8):
#                 if answer[o+i][k+j] != chess_arr[o][k]:
#                     count+= 1
#                 elif answer[o][k+j] != chess_arr_2[o][k]:
#                     count2 += 1

#         print(count)
    
#         if min_num > min(count, count2):
#             min_num = min(count, count2)


# print(min_num)