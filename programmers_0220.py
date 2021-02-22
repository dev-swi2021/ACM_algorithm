import re
def solution(dartResult):    
    pow_ = {'S':1, 'D':2, 'T':3}
    lenResult = len(dartResult)
    answer = []
    tmp = 0
    check = False # 숫자가 10인지 아닌지를 판단하는 변수 -> re.compile로 변경할 수 있음.
    for idx in range(lenResult):    
        if check:
            check = False
            continue
        if dartResult[idx] in pow_.keys():
            answer.append(tmp**(pow_[dartResult[idx]]))
        elif dartResult[idx] == '*':
            if len(answer) > 1:
                answer[len(answer)-2] = answer[len(answer)-2]*2
            answer[len(answer)-1] = answer[len(answer)-1]*2
                
        elif dartResult[idx] == '#':
            answer[-1] = -answer[-1]
        else:
            tmp = int(re.match('[0-9]+',dartResult[idx:]).group())
            check = True if tmp == 10 else False
            
    
    return sum(answer)
    

# Test 용
dartResult = ['1S2D*3T', '1D2S#10S', '1D2S0T','1S*2T*3S', '1D#2S*3S', '1T2D3D#', '1D2S3T*']
result = [37, 9, 3, 23, 5, -4, 59]

for dart, r in zip(dartResult, result):
    print("dart = {}  ".format(dart), end=' ')
    res = solution(dart)
    print("{} {} --> {}".format(res, r, res==r))
