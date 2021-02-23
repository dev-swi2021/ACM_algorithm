import sys
input = sys.stdin.readline

n = int(input())

n_lst = []
cnt = dict()
for _ in range(n):
    _n = int(input())
    n_lst.append(_n)
    cnt[_n] = cnt[_n] + 1 if _n in cnt.keys() else 1
n_lst.sort()

# 산술평균
print("산술평균 :", round(sum(n_lst)/n))

# 중앙값
print("중앙값 :", n_lst[n//2])

# 최빈값
cnt = sorted(cnt.items(), key= lambda x: (-x[1],x[0]))
print(cnt)
# 모든 수가 중복수일 경우
if len(cnt) == 1:
    print("최빈값 :",cnt[0][0])
# 최빈값이 여러 개 일 경우
elif cnt[1][1] == cnt[0][1]:
    print("최빈값 :",cnt[1][0])
else:   # 최빈값이 하나일 경우
    print("최빈값 :",cnt[0][0])
# 범위
print("범위 :", n_lst[-1] - n_lst[0])


# Test 용
n = [5, 5]
number_lst = [[1,3,8,-2,2], [2,7,9,7,6]]
result = [[2,2,1,10],[6,7,7,7]]
