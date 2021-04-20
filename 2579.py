# https://www.acmicpc.net/problem/2579 -> dp
import sys
input = sys.stdin.readline

number = int(input())
stairs = [int(input()) for _ in range(number)]
# dp => k번째에서 계단에서 얻을 수 있는 최대 값
dp = [0 for _ in range(number+1)]


for idx in range(1,number+1):
  if idx == 1:
    dp[1] = stairs[0]
  else:
    dp[idx] = max(dp[idx-1]+stairs[idx-1], dp[idx-2]+stairs[idx-1])
print(dp)
