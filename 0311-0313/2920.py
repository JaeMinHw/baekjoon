N = list(map(int, input().split()))

old_cnt = 0
new_cnt = 0
flag = 0
for i in range(7):



    if(N[i] - N[i+1] > 0) :
        new_cnt = 1
    elif (N[i] - N[i+1] < 0):
        new_cnt = -1
    
    if(i != 0 and old_cnt != new_cnt) :
        flag = 2
        

    old_cnt = new_cnt

if old_cnt == 1 and flag == 0:
    print("descending")
elif old_cnt == -1 and flag == 0:
    print("ascending")
if flag == 2:
    print("mixed")