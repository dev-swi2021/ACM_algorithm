import sys
input = sys.stdin.readline

n = int(input())

n_lst = []
cnt = dict()
for _ in range(n):
    _n = int(input())
    n_lst.append(_n)
    if _n in cnt.keys():
        cnt[_n] += 1
    else:
        cnt[_n] = 1

n_lst.sort()
print(n_lst)
# 산술평균
print("산술평균 :", round(sum(n_lst)/n))
# print(sum(n_lst)//n)
# 중앙값
print("중앙값 :", n_lst[n//2])
# print(sorted(n_lst)[n//2])
# 최빈값
cnt = sorted(cnt.items(), key= lambda x: (-x[1],x[0]))
print(cnt)
# 모든 수가 중복수일 경우
if len(cnt) == 1:
    print("최빈값 :",cnt[0][0])
    # print(cnt[0][0])
# 최빈값이 여러 개 일 경우
elif cnt[1][1] == cnt[0][1]:
    print("최빈값 :",cnt[1][0])
    # print(cnt[1][0])
else:   # 최빈값이 하나일 경우
    print("최빈값 :",cnt[0][0])
    # print(cnt[0][0])
# 범위
print("범위 :", n_lst[-1] - n_lst[0])
# print(max(n_lst) - min(n_lst))

a = [3,7,8,9,2,5,11]
b = [3,7,8,9,2,6,12]
print(round(sum(a)/len(a)))
print(round(sum(b)/len(b)))
