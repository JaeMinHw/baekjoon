import sys

t_d = [''] * 5
tra_t_d = [[-1]*15 for _ in range(15)]
for i in range(5):
    t_d[i] = input()
    for j in range(len(t_d[i])) :
        tra_t_d[j][i] = t_d[i][j]
        
        
# print(tra_t_d)



for i in range(15):
    for j in range(len(tra_t_d[i])) :
        if tra_t_d[i][j] != -1:
            print(tra_t_d[i][j], end = '')
