
N = int(input())

p = [[0] * 2 for _ in range(N)]

for i in range(N):
    p[i][0], p[i][1] = map(str, input().split())
    


tem_age = ' '
tem_name = ' '
for i in range(N) :
    for j in range(i, N-i-1):
        if int(p[j][0]) > int(p[j+1][0]) :
            
            tem_age = p[j][0]
            p[j][0] = p[j+1][0]
            p[j+1][0] = tem_age

            tem_name = p[j][1]
            p[j][1] = p[j+1][1]
            p[j+1][1] = tem_name


for i in range(N):
    print(p[i][0], p[i][1])