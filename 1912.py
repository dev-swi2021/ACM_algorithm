import sys
from collections import defaultdict
input = sys.stdin.readline

number = int(input())
arr_lst = list(map(int, input().split()))

# 1. 가장 큰 합 구하기
l_arr = len(arr_lst)

dp = [arr_lst[0]]

for idx in range(l_arr-1):
  dp.append(max(dp[idx]+ arr_lst[idx+1], arr_lst[idx+1]))