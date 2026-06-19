def solution(record):
    answer = []
    user_list = {}
    for i in range(len(record)):
        a = record[i].split()
        if (record[i][0] == "C") :
            user_list[a[1]] = a[2]
            pass
        elif record[i][0] == "E" :
            user_list[a[1]] = a[2]

    
    for i in range(len(record)) :
        a = record[i].split()
        name = user_list[a[1]]
        if (record[i][0] == "L") :
            answer.append(str(name)+"님이 나갔습니다.")
        elif record[i][0] == "E" :
            answer.append(str(name)+"님이 들어왔습니다.")

    return answer


print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))