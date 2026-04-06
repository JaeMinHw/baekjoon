import sys
from collections import deque

input = sys.stdin.readline

loop_N = int(input())




for i in range(loop_N):

    arr = deque()
    num, index = map(int,input().split())

    count = 0
    
    arr = deque(map(int, input().split()))

    index_value = arr[index]
    ch = 0
    max_num = max(arr)
    
    while 1 :
        if max_num != arr[0] :
            arr.rotate(-1)
            index -= 1

            if index <0 :
                index = len(arr) -1

        else :
            if index_value == max_num and index == 0 :
                print(ch+1)
                break
            else :
                ch +=1
                del arr[0]
                max_num = max(arr)
                index -= 1

                if index <0 :
                    index = len(arr) -1
        
    
