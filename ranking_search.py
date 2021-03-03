# reference(설명): https://whwl.tistory.com/193
# 문제 : https://programmers.co.kr/learn/courses/30/lessons/72412
from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    info_dict = defaultdict(list)
    for i in info:
        i = i.split()
        info_key = i[:-1]
        info_val = int(i[-1])
        for idx in range(5):
            for c in combinations(info_key, idx):
                tmp_key = ''.join(c)
                info_dict[tmp_key].append(info_val)
    
    for key in info_dict.keys():
        info_dict[key].sort()

    for q in query:
        q = q.split(' ')
        q_score = int(q[-1])
        q = q[:-1]

        for idx in range(3):
            q.remove('and')
    
        while '-' in q:
            q.remove('-')
        tmp_q = ''.join(q)

        # lower bound
        if tmp_q in info_dict:
            scores = info_dict[tmp_q]
            if len(scores) > 0:
                start, end = 0, len(scores)
                while end > start:
                    mid = (start + end) // 2
                    if scores[mid] >= q_score:
                        end = mid
                    else:
                        start = mid + 1
                answer.append(len(scores) - start)
        else:
            answer.append(0)
    return answer

# Test
info=[["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]]
query = [["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]]
result = [[1, 1, 1, 1, 2, 4]]

for i, q, r in zip(info, query, result):
    res = solution(i,q)
    print("{} {} ==> {}".format(r, res, res == r))
