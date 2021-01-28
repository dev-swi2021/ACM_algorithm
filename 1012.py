import sys
# 가로, 세로 매핑 잘하기
def dfs(graph, x,y, visited):
    if (x < 0 or x >= m) or (y < 0 or y >= n):
        return 0
    if visited[y][x]:
        return 0
    visited[y][x] = True
    if graph[y][x] == 0:
        return 0
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    count = 1
    for _x, _y in zip(dx,dy):
        count += dfs(graph, x+_x,y+_y, visited)
    return count

T = int(sys.stdin.readline())
for test_case in range(T):
    m,n,k = map(int, sys.stdin.readline().split())
    
    b = [[0 for _ in range(m)] for _ in range(n)]
    
    for e in range(k):
        x,y = map(int, sys.stdin.readline().split())
        b[y][x] = 1

    visited = [[False for _ in range(m)] for _ in range(n)]
    c = 0
    for y in range(n):
        for x in range(m):
            if dfs(b, x, y, visited):
                c += 1
    print(c)
