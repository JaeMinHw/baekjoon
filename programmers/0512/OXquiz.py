def solution(quiz):
    answer = []
    oper = ['+','-','*','/']
    for i in range(len(quiz)):
        a = quiz[i]

        arr = a.split()
        re = 0
        for j in range(len(arr)-3):

            if j %2 == 0:
                re = int(arr[j])
            else :
                if arr[j] == '-' :
                    re = re - int(arr[j+1])
                elif arr[j] == '+' :
                    re += int(arr[j+1])
                elif arr[j] == '*' :
                    re *=int(arr[j+1])
                elif arr[j] == '/' :
                    re /= int(arr[j+1])

        if int(arr[4]) == re :
            answer.append("O")
        else :
            answer.append("X")

    return answer


solution(["3 - 4 = -3", "5 + 6 = 11"])