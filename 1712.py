import sys

# a : 노트북 만드는 데 필요한 고정 비용 (임대료, 재산세, 보험료, 급여 등)
# b : 노트북 만드는 데 필요한 가변 비용 (재료비, 인건비 등)
# c : 노트북 가격

a,b,c = map(float, sys.stdin.readline().split())

# 계산 a + b*x < c * x -> a < (c-b)*x -> x > a / (c-b)

breaking_even_point = int(a / (c-b)) + 1 if c > b else -1
print(breaking_even_point)


