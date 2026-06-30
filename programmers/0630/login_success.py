def solution(id_pw, db):
    answer = 'fail'
    flag = 0
    for i in range(len(db)):
        if db[i][0] == id_pw[0]:
            if db[i][1] == id_pw[1]:
                return "login"
            else :
                flag = 1
                return "wrong pw"
                
        else :
            answer = "fail"
    return answer