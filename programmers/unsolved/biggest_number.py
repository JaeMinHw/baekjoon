def quick_sort_pythonic(arr):
    # 배열이 하나 이하의 원소만을 담고 있다면 이미 정렬된 상태이므로 그대로 반환
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # 첫 번째 원소를 피벗으로 설정
    tail = arr[1:]  # 피벗을 제외한 나머지 리스트

    # 리스트 컴프리헨션을 사용해 분할
    left_side = []  # 피벗보다 작은 그룹
    right_side = [] # 피벗보다 크거나 같은 그룹
    
    for x in tail :

        a = str(x) + str(pivot)
        b = str(pivot) + str(x)
        if a > b :
            left_side.append(x)
        else :
            right_side.append(x)


    # 분할된 왼쪽과 오른쪽 리스트를 각각 다시 퀵정렬(재귀)하고, 전체를 병합
    return quick_sort_pythonic(left_side) + [pivot] + quick_sort_pythonic(right_side)

def solution(numbers):
    
    answer = ''.join(map(str, quick_sort_pythonic(numbers)))
    if answer.count('0') == len(answer) :
        answer = '0'
    return answer
