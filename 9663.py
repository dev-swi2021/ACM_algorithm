# 백트래킹 -> 일반적으로 dfs를 이용하여 푼다.
# 한정된 숫자일 경우 사용

def check(x):
  for i in range(x):
    if row[x] == row[i]:
      return False
    if abs(row[x]-row[i]) == x-i:
      return False
  return True

def dfs(x):
  global result
  if x == n:
    result += 1
  else:
    for i in range(n):
      row[x] = i
      if check(x):
        dfs(x+1)

n = int(input())
row = [0]*n
result = 0
dfs(0)
print(result)