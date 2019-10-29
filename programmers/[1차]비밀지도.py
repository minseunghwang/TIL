def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1,arr2):
        a = str(format(i|j, 'b'))
        a = a.rjust(n,'0')
        a = a.replace('1','#').replace('0',' ')
        answer.append(a)

    return answer


# solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28])
print(solution(6, [46, 33, 33, 22, 31, 50], [27, 56, 19, 14, 14, 10]))
# ["#####","# # #", "### #", "# ##", "#####"]

    
    # print(format((9),'#b'))
    # print(int('0b11100',2))
    # print("후우")


'''
    a = "123"
    a = a.rjust(6,'#')
    하면은 ~ ###123

'''