def solution(sides):
    answer = 0
    set_list = set()
    
    max_s = max(sides[0], sides[1])
    min_s = min(sides[0], sides[1])
    a = max_s - min_s
    for i in range(1, max_s):
        if min_s + i > max_s :
            set_list.add(i)
    for i in range(max_s, max_s+min_s):
        if min_s + max_s > i :
            set_list.add(i) 
    answer = len(set_list)
    return answer