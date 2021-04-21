# 15649
from itertools import permutations, combinations

def problem15649():
  n,m = map(int, input().split())

  for perm in permutations(range(1,n+1),m):
    for p in perm:
      print("".join(str(p)), end=' ')
    print()

# 15650
def problem15650():
  n,m = map(int, input().split())
  for comb in combinations(range(1, n+1), m):
    for c in comb:
      print("".join(str(c)), end=' ')
    print()

# 15651
result = []
def dfs(depth, n,m):
  global result
  if depth == m:
    print(" ".join(map(str, result)))
    return
  else:
    for i in range(n):
      result.append(i+1)
      dfs(depth+1, n, m)
      result.pop()

def problem15651():
  n, m = map(int, input().split())
  dfs(0, n, m)

result = []
def dfs15652(depth, idx, n, m):
  global result
  if depth == m:
    print(" ".join(map(str, result)))
    return
  else:
    for i in range(idx, n+1):
      result.append(i)
      dfs15652(depth+1, i, n, m)
      result.pop()

def problem15652():
  n, m = map(int, input().split())
  dfs15652(0, 1, n, m)
  


if __name__ == '__main__':
  problem = int(input())
  if problem == 15649:
    problem15649()
  elif problem == 15650:
    problem15650()
  elif problem == 15651:
    problem15651()
  else:
    problem15652()