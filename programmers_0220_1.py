def solution(n, arr1, arr2):
    answer = []
    
    for a1, a2 in zip(arr1, arr2):
        b1, b2 = bin(a1).replace('0b',''), bin(a2).replace('0b','')
        if len(b1)!= n:
            b1 = '0'*(n-len(b1))+b1
        if len(b2)!= n:
            b2 = '0'*(n-len(b2))+b2
        tmp = ''
        for _b1, _b2 in zip(b1,b2):
            if (int(_b1) | int(_b2)):
                tmp +='#'
            else:
                tmp += ' '
        answer.append(tmp)
    
    return answer

# Test
n = [5, 6]
arr1 = [[9, 20, 28, 18, 11], [46, 33, 33 ,22, 31, 50]]
arr2 = [[30, 1, 21, 17, 28], [27 ,56, 19, 14, 14, 10]]

result = [["#####","# # #", "### #", "#  ##", "#####"], 
        ["######", "### #", "## ##", " #### ", " #####", "### # "]]

for _n, a1,a2,r in zip(n, arr1, arr2,result):
    res = solution(_n, a1,a2)
    print("{} {} --> {}".format(res, r, res==r))
