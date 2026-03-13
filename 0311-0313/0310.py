import sys
t_d = [list(map(str, input().split())) for _ in range(5)]

arr = [0] * 5
max = 0
for i in range(0,5):
    if max < len(t_d[i]) :
        max = len(t_d[i])
    arr[i] = len(t_d[i])

print(arr)

i=0
j=0
k = 0
while True:
    if(k > 4):
        k = 0
    # print("i", i)
    # print("j",k)
    # print("arr",arr[k]-1)
    if(arr[k]-1 > j) :
        print(t_d[j][i], end = "")
        j += 1
    else : # 여기서 i를 바로 증가하면 안되고 다음거까지 한 다음 증가.
        j = 0
        i += 1
        if i > 4:
            break


    k+=1
