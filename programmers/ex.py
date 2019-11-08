def solution(scoville, k):
    answer = 0
    
    while min(scoville) < k:
        scoville=sorted(scoville)
        print(scoville)
        a = scoville.pop(0) + (scoville.pop(0) * 2)
        scoville.append(a)
        answer += 1
        if len(scoville) == 1:
            scoville[0] < K
            break


    print(answer)
    
    return answer

# sco = [1, 2, 3, 9, 10, 12]
# sco = [1, 1, 1, 1, 1, 1, 1]
sco = [7,1,2,3,3]

print(solution(sco,9))