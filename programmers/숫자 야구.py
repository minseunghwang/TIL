import itertools

def solution(baseball):
    answer = 0

    mo = [1,2,3,4,5,6,7,8,9]
    lst = list(itertools.permutations(mo,3))
    
    for i in lst[:]:
        print(i)


    return answer

solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]])