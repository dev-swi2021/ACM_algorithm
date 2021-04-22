# 다익스트라 - dfs
from collections import deque
def bfs(graph, x, visited):
  global nodeNumber
  
  visited[x] = True
  weights = [0 for _ in range(nodeNumber+1)]
  queue = deque([[x, 0]])
  
  while queue:
    _v, w = queue.popleft()
    weights[_v] = w
    for item, weight in graph[_v]:
      if not visited[item]:
        queue.append([item, w+weight])
        visited[item] = True
  return weights      

nodeNumber = int(input())
graph_ = {i:[] for i in range(nodeNumber+1)}

for _ in range(nodeNumber-1):
  n1, n2, c = map(int, input().split())
  graph_[n1].append((n2, c))
  graph_[n2].append((n1, c))


# root에서 제일 거리가 먼 노드 탐색
print("Root 탐색")
visited = [False for _ in range(nodeNumber+1)]
weights = bfs(graph_, 1, visited)
node = weights.index(max(weights))
print("제일 먼 노드는 :", node)

# 제일 먼 노드 찾기
print("결과 찾기")
visited = [False for _ in range(nodeNumber+1)]
weights = bfs(graph_, node, visited)
print(max(weights))