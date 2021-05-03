import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, x, visited):
  q = deque([x])
  visited[x] = True

  while q:
    v = q.popleft()
    for val in graph[v]:
      if not visited[val]:
        q.append(val)
        visited[val] = True

n,m = map(int, input().split())

v_dict = {idx:[] for idx in range(1, n+1)}
for _ in range(m):
  u,v = map(int, input().split())
  v_dict[u].append(v)
  v_dict[v].append(u)

visited = [False for _ in range(n+1)]
cnt = 0
for idx in range(1, n+1):
  if not visited[idx]:
    bfs(v_dict, idx, visited)
    cnt += 1
print(cnt)