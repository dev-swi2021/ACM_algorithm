import sys
input = sys.stdin.readline

length, width, height = map(int, input().split())
n = int(input())
answer = -1

# cube ->
cubes = [list(map(int, input())) for _ in range(n)]

