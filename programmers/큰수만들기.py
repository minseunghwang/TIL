def solution(number, k):
    lst = []
    answer = ""
    print(number)
    
    for i,num in enumerate(number):
        while len(lst) > 0 and k != 0 and num > lst[-1] :
            lst.pop()
            k -= 1
        if k == 0:
            lst += list(number[i:])
            break
        lst.append(num)
    lst = lst[:-k] if k > 0 else lst

    answer = "".join(lst)
    print(answer)
    return answer

number="1924"
k=3
solution(number,k)