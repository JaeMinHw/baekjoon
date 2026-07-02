def solution(babbling):
    answer = 0
    check_li = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)) :
        flag = 0
        sum = 0
        set_li = set()
        for j in range(4):
            if check_li[j] in babbling[i] and check_li[j] not in set_li:
                sum += len(check_li[j])
                print(check_li[j])
                set_li.add(check_li[j])
                flag += 1
            else :
                flag += 0
        if flag != 0 and sum == len(babbling[i]):
            answer +=1
        # print(flag, sum)
    return answer