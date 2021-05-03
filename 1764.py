import sys
from collections import Counter
input = sys.stdin.readline

n,m = map(int, input().split())
no_n_lst = [input().rstrip('\n') for _ in range(n)]
no_m_lst = [input().rstrip('\n') for _ in range(m)]

res = Counter(no_n_lst)
for val in no_m_lst:
  if val in res:
    res[val] += 1
  else:
    res[val] = 1
result = []
for val, cnt in res.items():
  if cnt > 1:
    result.append(val)
print(len(result))
print("\n".join(sorted(result)))
