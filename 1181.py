# 단어 정렬
"""
  알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

  1. 길이가 짧은 것부터
  2. 길이가 같으면 사전 순으로
"""

import sys
input = sys.stdin.readline
n = int(input())

words = list()
for idx in range(n):
  w = input().rstrip()  # 문장의 끝에 들어오는 개행문자를 제거하기 위함.
  if w in words:
    continue
  words.append(w)

words = sorted(words, key=lambda x:(len(x), x)) # 정렬 함수를 사용함 (정렬 기준, 1. 단어 길이, 2. 사전순)

for w in words:
  print(w)

# Test용
n = 13
words = ['but', 'i', 'wont', 'hesitate', 'no', 'more', 'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']
