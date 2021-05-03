# 촌수 계산하는 프로그램
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, dest):
  visited=[False for _ in range(n+1)]
  q = deque([[start, 0]])
  visited[start] = True
  while q:
    v, cnt = q.popleft()
    if v == dest:
      return cnt

    for val in graph[v]:
      if not visited[val]:
        q.append([val, cnt+1])
        visited[val] = True
  return -1

n = int(input())
p1, p2 = map(int, input().split())
m = int(input())
p_dict = {idx:[] for idx in range(1,n+1)}
for _ in range(m):
  # 부모, 자식 순
  x,y = map(int, input().split())
  p_dict[x].append(y)
  p_dict[y].append(x)

res = bfs(p_dict, p1, p2)
print(res)

