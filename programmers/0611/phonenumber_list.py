def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book)

    
    for i in range(len(phone_book) -1) :
        len_b = len(phone_book[i])
        if phone_book[i] in phone_book[i+1][:len_b] :
            answer = False
            break
    return answer

print(solution(["119", "97674223", "1195524421"]))