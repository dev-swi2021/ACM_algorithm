from collections import deque
import sys

def show_board(board):
  for i in board:
    for j in i:
      print(j, end=' ')
    print()

def bfs(graph, x, y, dest):
"""
  params graph: 체스 판
  params x: 말(나이트) 시작 x 위치
  params y: 말(나이트) 시작 y 위치
  params dest : 도착해야하는 x,y 위치
  
  return: 도착 위치까지 움직이는 횟수
"""
  queue = deque([[x,y]])
  while queue:
    x,y = queue.popleft()
    if x==d_x and y==d_y:
      show_board(graph) # 움직인 횟수 확인을 위함
      reutnr graph[d_x][d_y]
    
    # 나이트가 한번에 움직일 수 있는 위치 
    dx = [2, 2, -2, -2, 1, 1, -1, -1]
    dy = [1, -1, 1, -1, 2, -2, 2, -2]
    
    for _x, _y in zip(dx,dy):
      if ((x+_x) >= 0 and (x+_x)<len(graph)) and ((y+_y) >= 0 and (y+_y) <len(graph)) and graph[x+_x][y+_y] == 0:
        queue.append([x+_x,y+_y])
        graph[x+_x][y+_y] = graph[x][y] + 1 # 움직인 횟수 update
