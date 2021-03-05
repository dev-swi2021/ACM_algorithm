import heapq
def djkstra(graph, n):
  cost = [[]]
  for i in range(1,n+1):
    dist = [float('inf') for _ in range(n+1)]
    dist[i] = 0
    queue = []
    heapq.heappush(queue, [0, i])
    while queue:
      c, v = heapq.heappop(queue)
      if dist[v] < c:
        continue

      for idx in range(1,len(graph[v])):
        if c+graph[v][idx] < dist[idx]:
          dist[idx] = c+graph[v][idx]
          heapq.heappush(queue, [c+graph[v][idx],idx])
    cost.append(dist)
  return cost

def solution(n, s, a, b, fares):
  # make graph
  graph = [[float('inf') for _ in range(n+1)] for _ in range(n+1)]
  for start,dest, f in fares:
    graph[start][dest] = graph[dest][start] = f
    graph[start][start] = graph[dest][dest] = 0
  
  # make djkstra
  graph = djkstra(graph, n)
  
  # calculate cost
  min_ = float('inf')
  for i in range(1, n+1):
    min_ = min(min_, graph[s][i]+graph[i][a]+graph[i][b])
  return min_


# Test용 예시
n = [6,7,6]
s = [4,3,4]
a = [6,4,5]
b = [2,1,6]
fares = [[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]], [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]], [[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]]
result = [82, 14, 18]
print()
print()
for _n, _s, _a, _b, f, r in zip(n,s,a,b, fares, result):
  res = solution(_n,_s,_a,_b,f)
  print("{} {} ==> {}".format(res, r, res==r))
