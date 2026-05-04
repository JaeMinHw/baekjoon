from collections import Counter
def solution(participant, completion):
    answer = ''

    set_participant = set(participant)
    counter_participant = Counter(participant)

    
    for i in range(len(completion)):
        if completion[i] in counter_participant :
            counter_participant[completion[i]] -= 1
        if counter_participant[completion[i]] == 0 :
            del counter_participant[completion[i]]
    

    return  (' '.join(counter_participant))

solution(["emily", "james","michael", "sophia", "michael"], ["michael", "emily", "james"])
