def solution(new_id):
    id_list = set({'a','b','c','d','e','f','g','h','i','j','k','l',
'm','n','o','p','q','r','s','t','u','v','w','x','y','z',
'1','2','3','4','5','6','7','8','9','0','-','_','.'})
    answer = ''
    new_id = new_id.lower()
    for i in new_id:
        if i not in id_list:
            new_id = new_id.replace(i,'')


    while True :
        if '..' in new_id:
            
            new_id = new_id.replace('..','.')
            print(new_id)
        else :
            break
    
    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id.replace('.','', 1)


    if len(new_id) != 0 and new_id[len(new_id)-1] == '.':
        new_id = new_id[0:len(new_id)-1]
    

    if len(new_id) == 0:
        new_id += 'a'

    if len(new_id) >= 16 :
        new_id = new_id[0:15]

    # 7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
    if len(new_id) != 0 and new_id[len(new_id)-1] == '.':
        new_id = new_id[0:len(new_id)-1]

    if len(new_id) <= 2 :
        while len(new_id) < 3:
            new_id += new_id[len(new_id)-1]

    print(new_id)

    return new_id
# solution("...!@BaT#*..y.abcdefghijklm")
solution("abcd.eeee.")