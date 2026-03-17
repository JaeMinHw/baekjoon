arr = [''] * 3
index = 0
cnt = 0
index_arr = [0] * 3


def check(a) :
    # 그 숫자를 배수 확인해서 출력
    if a % 3 == 0 and a %  5 == 0:
        print("FizzBuzz")
    elif a %3 == 0 and a  %  5 != 0:
        print("Fizz")
    elif a%3 != 0 and a  %  5 == 0:
        print("Buzz")
    elif a%3 != 0 and a  %  5 != 0:
        print(a)

        
for i in range(3) :
    arr[i] = input()

    if arr[i].isnumeric():
        index_arr[i] = 1
        index = i
        cnt += 1


if cnt == 2:
    # index_arr에서 0 인 값 찾아서 앞에 있는 값에 +1 하고 배수 확인
    # for i in range(3) :
    #     if index_arr[i] == 0:
    #         index = i

    a = 0
    if index == 2 :
        a= int(arr[index])+1

    elif index == 1 :
        a= int(arr[index])+2


    check(a)

elif cnt == 1 :
    # 그 숫자를 배수 확인해서 출력
    if (int(arr[index]) + 3-index) % 3 == 0 and (int(arr[index]) + 3-index) %  5 == 0:
        print("FizzBuzz")
    elif (int(arr[index]) + 3-index)% 3 == 0 and (int(arr[index]) + 3-index)  %  5 != 0:
        print("Fizz")
    elif (int(arr[index]) + 3-index)% 3 != 0 and (int(arr[index]) + 3-index)  %  5 == 0:
        print("Buzz")
    elif (int(arr[index]) + 3-index)% 3 != 0 and (int(arr[index]) + 3-index)  %  5 != 0:
        print((int(arr[index]) + 3-index))



