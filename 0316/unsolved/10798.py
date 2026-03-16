import sys

t_d = [''] * 5

for i in range(5):
    t_d[i] = list(map(str, input().split()))



i = 0
j = 0

arr = [0] * 5
max = 0
for i in range(0,5):
    if max < len(t_d[i]) :
        max = len(t_d[i])
    arr[i] = len(t_d[i])

print(max)
i = 0
j = 0
k = 0
falg = 0
while 1:
    a = ''.join(t_d[k])
    if j < arr[k] :
        print("j")
        print(a[j], end = '')
        
    
 
    if i > max and k == 4:
        print("i")
        break
    if k > 4:
        j += 1
        k = 0
        i +=1
    k+= 1
        
# st = ("".join(t_d))

# print(st[1])
# arr = [0] * 5
# max = 0
# for i in range(0,5):
#     if max < len(t_d[i]) :
#         max = len(t_d[i])
#     arr[i] = len(t_d[i])

# print(arr)

# i=0
# j=0
# k = 0
# while True:
#     if(k > 4):
#         k = 0
#     # print("i", i)
#     # print("j",k)
#     # print("arr",arr[k]-1)
#     if(arr[k]-1 > j) :
#         print(t_d[j][i], end = "")
#         j += 1
#     else : # 여기서 i를 바로 증가하면 안되고 다음거까지 한 다음 증가.
#         j = 0
#         i += 1
#         if i > 4:
#             break


#     k+=1
