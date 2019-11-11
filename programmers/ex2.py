def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    q = [begin]
    
    for n,word in enumerate(words):
        cnt = 0
        for i,j in zip(word,begin):
            if i==j:
                cnt += 1
        if cnt == 2:
            q.append(word)
            visited[n] = 1
    print(q,visited)


    while q:
        


            

    return answer


begin = "hit"
target = "cog"
words =	["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin,target,words))