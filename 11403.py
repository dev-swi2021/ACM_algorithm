import sys
input = sys.stdin.readline

n = int(input())
adj_matrix = [list(map(int, input().split())) for _ in range(n)]

# 플로이드 와샬 알고리즘 -> 경유하는 비용이 직접가는 비용보다 싼 경우
# k: 경유지
for k in range(n):
  # i: 출발지
  for i in range(n):
    # j: 도착지
    for j in range(n):
      if adj_matrix[i][j] == 1 or (adj_matrix[i][k] == 1 and adj_matrix[k][j]==1):
        adj_matrix[i][j] = 1
      
for row in adj_matrix:
  for col in row:
    print(col, end=' ')
  print()