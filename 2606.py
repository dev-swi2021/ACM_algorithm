from collections import deque
# 1번을 통해 바이러스가 전파된 컴퓨터 대수 구하기(컴퓨터 대수에서 1번 컴퓨터 제외)
def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    count = -1
    while queue:
        v = queue.popleft()
        count += 1
    
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
    return count

n = int(input())
m = int(input())

# 그래프 만들기
computers = {}
visited = [False] * (n+1)
for i in range(m):
    x1,x2 = map(int, input().split())
    if x1 in computers.keys():
        computers[x1].append(x2)
    else:
        computers[x1] = [x2]
  
    if x2 in computers.keys():
        computers[x2].append(x1)
    else:
        computers[x2] = [x1]
# 실행
print(bfs(computers, 1, visited))
