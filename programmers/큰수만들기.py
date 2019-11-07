import itertools

def solution(number, k):
    answer = []
    kk = len(number) - k
    lst = list("".join(number))
    print(lst)
    print(max(lst[0:-kk+1]))
    kk -= 1
    m=0
    for i,j in zip(range(len(lst)), lst):
        print('이거',lst[m:-kk+1])
        if max(lst[m:-kk+1]) == j:
            print('여기서젤큰거 : ', (lst[m:-kk+1]))
            print('kk',kk)
            answer.append(j)
            kk = kk - 1
            m = i
            print(m)
            print('답',answer)

    
    
    return answer 

number="4177252841"
k=4
solution(number,k)