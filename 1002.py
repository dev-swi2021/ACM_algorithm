import sys
import math
input = sys.stdin.readline

T = int(input())

for _ in range(T):
  x1,y1,r1,x2,y2,r2 = map(int, input().split())
  # 두 원의 중심 사이의 거리
  distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
  # 두 원이 같음
  if distance==0 and r1 == r2:
    print(-1)
  
  # 안 만남
  elif distance > r1 + r2 or distance + r1 < r2 or distance + r2 < r1:
    print(0)
  # 한 점에서 만나기
  elif distance == r1 + r2 or r2 == distance + r1 or r1 == distance+r2:
    print(1)
  else:
    print(2)