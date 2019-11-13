def solution(begin, target, words):
    answer = 0
    visited = [0] * len(words)
    q = [begin]
    print(words)

    while q:
        print(q)
        text = q.pop(0)
        print(visited)
        for n,word in enumerate(words):
            if visited[n] == 0:
                cnt = 0
                for i,j in zip(text,word):
                    if i==j:
                        cnt += 1
                        if cnt==3:
                            return answer
                if cnt==2:
                    q.append(word)
                    visited[n] = 1
                    answer += 1
    return answer


begin = "hit"
target = "cog"
words =	["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(begin,target,words))