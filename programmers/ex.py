import heapq

def solution(scoville, K):
    scoville = sorted(scoville)
    print(scoville)
    s_list = scoville[1:]
    answer = 0
    sco_result = 0
    result = 0
    heap = []
    
    if len(scoville)==1:
        if scoville[0] >= K:
            return 0
        else:
            return -1

    for i in s_list:
        heapq.heappush(heap, i)
    print(heap)
       
    result = scoville[0]
    while True:
        print(heap)        
        if sco_result >= K:
            return answer
        else :
            if len(heap) == 0:
                return -1
            a = heapq.heappop(heap)
            sc = [result, a]
            sco_result = min(sc) + ( max(sc) * 2 )
            print(sco_result)
            result = sco_result
            heap.append(sco_result)
            answer += 1

    return -1

sco = [1, 2, 3, 9, 10, 12]
sco = [1, 1, 1, 1, 1, 1, 1]
sco = [7,1,2,3,3]

print(solution(sco,9))