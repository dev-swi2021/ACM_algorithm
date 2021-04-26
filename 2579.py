import sys
input = sys.stdin.readline

number = int(input())
stairs = [int(input()) for _ in range(number)]
stairs.insert(0, 0)

# dp => k번째에서 계단에서 얻을 수 있는 최대 값
dp = [0 for _ in range(number+1)]

# 규칙 
# 1. 계단은 한번에 한 개 혹은 두 개씩 오를 수 있음
# 2. 연속 세개는 안됨(출발점은 제외)
# 3. 마지막 도착 계단은 반드시 밟기
for idx in range(1,number+1):
  if idx == 1:
    dp[idx] = stairs[idx]
  elif idx == 2:
    dp[idx] = max(dp[idx-1]+stairs[idx], stairs[idx])
  else:
    dp[idx] = max(dp[idx-3]+stairs[idx-1], dp[idx-2])+stairs[idx]
print(dp[number])