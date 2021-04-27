# 안전한 영역의 최대 개수를 계산하는 프로그램
import sys
import copy
import math
from collections import deque
input = sys.stdin.readline
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def bfs(graph, x,y, visited):
  queue = deque([[x,y, 1]])
  visited[y][x] = True
  while queue:  
    x,y,c = queue.popleft()
    for _x, _y in zip(dx,dy):
      nx, ny =x+_x, y+_y
      if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph):
        continue
      if not visited[ny][nx] and graph[ny][nx]==1:
        queue.append([nx,ny, c+1])
        visited[ny][nx] = True

n = int(input())
area = [list(map(int, input().split())) for _ in range(n)]

min_ = math.inf
max_ = 0

for _area in area:
  min_ = min(min_, min(_area))
  max_ = max(max_, max(_area))

max_cnt = 0
max_idx = min_-1
for k in range(min_-1, max_+1):
  visited = [[False]*n for _ in range(n)]
  tmp = copy.deepcopy(area)
  for i in range(n):
    for j in range(n):
      if tmp[i][j] - k <= 0:
        tmp[i][j] = 0
      else:
        tmp[i][j] = 1
  cnt = 0
  for i in range(n):
    for j in range(n):
      if tmp[i][j] == 1 and not visited[i][j]:
        bfs(tmp, j,i,visited)
        cnt += 1

  max_cnt = max(cnt, max_cnt)

print(max_cnt)
    