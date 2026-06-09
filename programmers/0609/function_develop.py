def solution(progresses, speeds):
    answer = []
    lis = [0] * len(progresses)
    for i in range(len(progresses)):
        lis[i] = (100 - progresses[i]) // speeds[i]
        if (100 - progresses[i]) % speeds[i] != 0:
            lis[i] += 1
    count = 1
    flag = lis[0]
    for i in range(len(lis)-1):
        
        if flag < lis[i+1]:
            answer.append(count)
            count = 1
            flag = lis[i+1]
            
        else :
            count+=1
    answer.append(count)
    return answer