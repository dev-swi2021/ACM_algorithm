import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())
res = []
for _ in range(T):
  left, right = map(int, input().split())
  
  if left == right:
    res.append(1)
  elif left == 1 or right==1:
    res.append(left if right == 1 else right)
  else:
    range_ = range(left, left-right,-1) if left > right else range(right, right-left, -1)
    up = 1
    for idx in range_:
      up *= idx
    
    range_ = range(1, right+1) if left > right else range(1, left+1)
    down = 1
    for idx in range_:
      down *= idx
    res.append(up//down)

for r in res:
  print(r)

