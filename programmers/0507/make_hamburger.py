def solution(ingredient):
    answer = 0
    i = len(ingredient)-3
    ingredient = ingredient[::-1]
    arr=  []
    while ingredient :
        arr.append(ingredient.pop())

        if len(arr) > 3 :
            if arr[-1] == 1 :
                if arr[-2] == 3 :
                    if arr[-3] == 2 :
                        if arr[-4] == 1 :
                            answer += 1
                            arr.pop()
                            arr.pop()
                            arr.pop()
                            arr.pop()

                            i = len(arr)-3
        
                    
        i -=1
    
    return answer
