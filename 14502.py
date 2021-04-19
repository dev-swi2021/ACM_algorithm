# https://www.acmicpc.net/problem/14502
import sys
import copy
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def virus(graph, x,y, virus, visited):
  queue = deque(virus)

  dx, dy = [1,-1, 0, 0], [0, 0, 1, -1]
  while queue:
    y,x = queue.popleft()
    visited[y][x] = True

    for _x, _y in zip(dx, dy):
      new_x, new_y = x+_x, y+_y
      if new_x < 0 or new_x > len(graph[0])-1 or new_y < 0 or new_y > len(graph)-1:
        continue
      if not visited[new_y][new_x]:
        if graph[new_y][new_x] == 0:
          graph[new_y][new_x] = 2
          queue.append([new_y, new_x])
          visited[new_y][new_x] = True
  
  count = 0
  for g in graph:
    count += g.count(0)
  global max_num
  max_num = max(count, max_num)


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]
combination = list(combinations(range(n*m), 3))
max_num = 0

for comb in combination:
  tmp_maps = copy.deepcopy(maps)
  visited = [[False for _ in range(m)] for _ in range(n)]
  cnt = 0
  for c in comb:
    y,x = c//m, c%m
    if tmp_maps[y][x] == 0:
      tmp_maps[y][x] = 1
      cnt += 1
  if cnt < 3:
    continue
  # virus 찾기
  virus_lst = []
  for y in range(n):
    for x in range(m):
      if tmp_maps[y][x] == 2:
        virus_lst.append([y,x])

  virus(tmp_maps, x, y, virus_lst, visited)

print(max_num)