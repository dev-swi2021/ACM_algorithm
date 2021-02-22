import re
def solution(str1, str2):
    str1 = [str1[i:i+2].upper() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    
    str2 = [str2[i:i+2].upper() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]
    
    total_lst = set(str1) | set(str2)
    print(total_lst, end=' ')
    if total_lst:
        union_ = 0
        intersection_ = 0
        for tl in total_lst:
            union_ += max(str1.count(tl), str2.count(tl))
            intersection_ += min(str1.count(tl), str2.count(tl))
    
        return int((intersection_/union_)*65536)
        
    return 65536
    
# Test
str1 = ['FRANCE', 'handshake', 'aa1+aa2', 'E=M*C^2', 'ABDDD']
str2 = ['french', 'shake hands', 'AAAA12', 'e=m*c^2', 'DDEFGHH']
answer = [16384, 65536, 43690, 65536, 7281]

for s1, s2, a in zip(str1, str2, answer):
    res = solution(s1, s2)
    print("{} {} --> {}".format(res, a, res == a))
    
    
str1 = ['aa1+aa2', 'ABDDD']
str2 = ['AAAA12', 'DDEFGHH']
answer = [43690, 7281]

for s1, s2, a in zip(str1, str2, answer):
    res = solution(s1, s2)
    print("{} {} --> {}".format(res, a, res == a))
