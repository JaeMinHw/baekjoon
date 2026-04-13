N = int(input())
x_arr = [0] *N
y_arr = [0] * N
rank = [N] * N

count = 0
for i in range(N):
    x_arr[i], y_arr[i] = map(int, input().split())


for i in range(N):
    for j in range(N):
        if i != j :
            if x_arr[i] > x_arr[j] and y_arr[i] > y_arr[j] :
                rank[i] -= 1

            elif x_arr[i] > x_arr[j] and y_arr[i] < y_arr[j] :
                rank[i] -= 1
            #     rank[j] -= 1
            elif x_arr[i] < x_arr[j] and y_arr[i] > y_arr[j] :
                rank[i] -= 1
            elif x_arr[i] == x_arr[j] or y_arr[i] == y_arr[j]:
                rank[i] -= 1

flag = 0        
for i in range(N):
    if(rank[i] == N) :
        flag += 1

if flag != 5 :
    for i in range(len(rank)):
        print(rank[i], end = ' ')
else :
    for i in range(len(rank)):
        print(1, end = ' ')