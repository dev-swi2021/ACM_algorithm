import sys
import heapq
input = sys.stdin.readline

def djk(graph, start, end):
  global n
  distance = [float('inf') for _ in range(n+1)]
  distance[start] = 0
  
  queue = []
  heapq.heappush(queue, (0, start))

  while queue:
    dist, v  = heapq.heappop(queue)
    # 이미 거리비용이 작음
    if distance[v] < dist:
      continue
    
    for next_cost, next_node in graph[v]:
      if dist + next_cost < distance[next_node]:
        distance[next_node] = dist + next_cost
        heapq.heappush(queue, (dist + next_cost,next_node))
  
  print(distance[end])
  

n = int(input())
m = int(input())
bus_info = [[] for _ in range(n+1)]
bis_info = []
for _ in range(m):
  s, e, c = map(int,input().split())
  bus_info[s].append((c,e))

start, end = map(int, input().split())
djk(bus_info, start, end)
