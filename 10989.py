# 10989 수 정렬하기 3

# Count Sort 이해하기
# 시간, 메모리 제한이 있는 상황에서 Count Sort를 쓸 생각을 할 수 있는지 확인해보자

import sys
n = int(sys.stdin.readlin())

n_cnt = [0 for _ in range(10001)]

for _ in range(n):
  n_cnt[int(sys.stdin.readline())] += 1

for idx in range(1, 10001):
  for _ in range(n_cnt[idx]):
    print(idx)
