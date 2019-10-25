import itertools

def solution(numbers):
    answer = 0
    lst = []

    number = list(numbers)
    for i in range(1,len(numbers)+1):
        lst += map(int,(map("".join,itertools.permutations(number,i))))
    a=list(set(lst))
    print(a)

    eratos = [1] * 9999999
    eratos[0] = 0
    eratos[1] = 0

    for i in range(2,int(len(eratos)**0.5)):
        if eratos[i]:
            for j in max(a):
                eratos[j] = 0
    print()

    

    return answer

# numbers = "17"
numbers = "011"
# numbers = "0007000"
solution(numbers)