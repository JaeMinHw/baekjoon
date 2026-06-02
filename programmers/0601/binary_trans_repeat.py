def solution(s):
    answer = []
    count = 0
    z_count = 0
    while s != "1":
        z_count += s.count('0')
        s = s.replace('0','')
        count += 1
        s = format(len(s), 'b')
        print(s)
    return answer

solution("110010101001")