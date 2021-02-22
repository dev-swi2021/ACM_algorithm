# sol1
import re
def solution(s):
    answer = []
    
    s = s.lstrip("{").rstrip("}").split("},{")

    tmp = []
    for _s in s:
        tmp.append(list(map(int, _s.split(','))))
    tmp = sorted(tmp, key=lambda x: len(x))
    if len(tmp) == 1:
        answer = tmp[0]
    else:
        for item in tmp:
            for i in item:
                if i in answer:
                    continue
                answer.append(i)
    
    return answer


# sol2
import re
from collections import Counter
def solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))
  
  
 
# Test
sentence = ["{{2},{2,1},{2,1,3},{2,1,3,4}}", "{{1,2,3},{2,1},{1,2,4,3},{2}}", "{{20,111},{111}}", "{{123}}", "{{4,2,3},{3},{2,3,4,1},{2,3}}"]

result = [[2, 1, 3, 4], [2, 1, 3, 4], [111, 20], [123], [3, 2, 4, 1]]

for s, r in zip(sentence, result):
    res = solution(s)
    print("{} {} --> {}".format(res, r, res==r))
