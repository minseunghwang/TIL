import itertools

def solution(numbers):
    count = 0
    num = []
    number = list(numbers)
    for i in range(1,len(numbers)+1):
        num += list(map(''.join,itertools.permutations(number,i)))
    print(num)
    numm = list(set(map(int,num)))
    numm.sort()
    print(numm)

# 에라토스테네스의 채
    eratos = [1] * 9999999
    eratos[0] = 0
    eratos[1] = 0
    for i in range(2, int((len(eratos)) ** 0.5)):
        if eratos[i]:
            for j in range(i + i, max(numm)+1, i):
                eratos[j] = 0
    for i in numm:
        if eratos[i] == 1:
            print(i)
            count += 1

    return count


# numbers = "17"
numbers = "011"
# numbers = "0007000"
solution(numbers)