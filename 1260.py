from collections import deque
from sys import stdin

def dfs(g, v, visited):  # recursion
    visited[v] = True
    print(v, end=' ')
  
    for idx in range(1, len(g[v])):
        if not visited[idx] and g[v][idx] == 1:
            dfs(g, idx, visited)

def bfs(g, start, visited):  # loop
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for idx in range(1,len(g[v])):
            tmp = g[v][idx]
            if tmp == 1 and not visited[idx]:
                queue.append(idx)
                visited[idx] = True

n,m,v = map(int, stdin.readline().split())

# graph를 이차원 배열로 만들기
graphs = [[0 for _ in range(n+1)] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int,input().split())
    graphs[a][b] = graphs[b][a] = 1
visited = [False for _ in range(n+1)]
# dfs
dfs(graphs, v, visited)
print()
visited = [False for _ in range(n+1)]
# bfs
bfs(graphs, v, visited)
