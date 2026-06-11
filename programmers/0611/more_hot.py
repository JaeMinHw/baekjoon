import heapq
def solution(scoville, K):
    answer = 0
    count = 0
    for i in range(len(scoville)):
        if scoville[i] >= K :
            count += 1
            
    for i in range(len(scoville) - 1, -1, -1):
        if scoville[i] >= K and count > 1:
            del scoville[i]
            count -= 1

        if count == 1:
            break
    heapq.heapify(scoville)
    while scoville[0] < K :

        
        if len(scoville) == 1 :
            answer = -1
            break
            
        x1 = heapq.heappop(scoville)
        x2 = heapq.heappop(scoville)
        heapq.heappush(scoville,x1 + x2 * 2)
        answer += 1

    return answer

print(solution([1, 2, 3, 9, 10, 12], 7))