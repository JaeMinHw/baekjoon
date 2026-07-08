def solution(message, spoiler_ranges):
    answer = 0
    set_key = set()
    sp_mess = message.split(' ')
    sp_arr = []
    c = 0
    for i in range(len(sp_mess)) :
        sp_arr.append((c, c+len(sp_mess[i])-1))
        c = c + len(sp_mess[i]) + 1
    print(sp_arr)
    for i in range(len(spoiler_ranges)) :
        for j in range(spoiler_ranges[i][0], spoiler_ranges[i][1]+1) :
            print(message[j])
    return answer

print(solution("here is muzi here is a secret message", [[0, 3], [23, 28]]))