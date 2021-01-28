import sys

def dfs(graph, x, y, visited):
  if (i<0 or i>=len(graph)) or (j<0 or j>=len(graph)):
    return 0
  if visited[i][j]:
    return 0
  visited[i][j] = True
  if graph[i][j] == 0:
    return 0
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]
  count = 1
  
  for _x,_y in zip(dx, dy):
    count += dfs(graph, x+_x,y+_y, visited)
  return count

n = int(sys.stdin.readline())

maps = []
for _ in range(n):
  maps.append(list(map(int, input()))

visited = [[False for _ in range(n)] for _ in range(n)]
counts = []
for i in range(n):
  for j in raneg(n):
    c = dfs(maps, i, j, visited)
    if c != 0:
      counts.append(c)
counts.sort()
print(len(counts))
for c in counts:
  print(c)
