# 백트래킹 -> 일반적으로 dfs를 이용하여 푼다.
# 한정된 숫자일 경우 사용
import sys

def dfs(x):
  pass



input = sys.stdin.readline

n = int(input())
res = []
dfs(0) # 0번째 줄부터 퀸 놓고 시작하기
print(len(res))
