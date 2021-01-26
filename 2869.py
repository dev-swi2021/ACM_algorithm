import sys
import math

a,b,v = map(int, sys.stdin.readline().split())

# n-1일 밤에 달팽이가 있는 위치 (v-a)이상 --> n일 낮에 목표지점에 도달 가능
# 1일부터 n-1일 까지 달팽이가 가야하는 위치 v-a, 하루에 달팽이가 갈 수 있는 거리 a-b
# 달팽이가 올라가는 시간 (v-a) / (a-b)
date = math.ceil((v-a)/ (a-b)) + 1  # 그 다음날 도착하기 때문에 +1
print(date)
