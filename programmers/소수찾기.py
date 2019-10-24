import itertools

def solution(numbers):
    answer = 0
    count = 0
    num = []
    number = list(numbers)
    for i in range(1,len(numbers)+1):
        num += list(map(''.join,itertools.permutations(number,i)))
    print(num)
    numm = list(set(map(int,num)))
    numm.sort()
    print(numm)

    for i in numm:
        if i < 2:
            pass
        elif i == 2:
            count += 1
        elif i > 2:
            for j in range(2,i):
                if i % j == 0:
                    break
                elif j == i-1:
                    print("소수:", i)
                    count +=1

    print("호이", count)
                
    

    # eratos = [1] * limit
    # limit = 999999
    # for i in range(2,limit):
    #     if eratos[i]:
    #         for j in range(i+i, limit):
    #             eratos[j] = 0
     



    return answer

# numbers = "17"
# numbers = "011"
numbers = "123"
solution(numbers)