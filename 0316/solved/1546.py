N = int(input())

score = input().split()
sum = 0
max = 0

for i in range(N):
    if int(score[i]) > max :
        max = int(score[i])

for i in range(N):
    score[i] = float(score[i]) / max *100



for i in range(N) :
    sum += score[i]

print(sum / N )