# 풀이 1 --> 시간 : 72ms
import sys
input = sys.stdin.readline

number = int(input())
count = 0
for n in range(number):
    word = input()
    stack_lst = []
    for w in word:
        if len(stack_lst) == 0:
            stack_lst.append(w)
        else:
            if stack_lst[-1] == w:
                continue
            stack_lst.append(w)
    res = True
    for s_lst in stack_lst:
        if stack_lst.count(s_lst) > 1:
            res = False
            break
    count = count + 1 if res else count
print(count)


# 풀이 2 --> 시간 : 84ms
import sys
input = sys.stdin.readline

number = int(input())
count = 0
for n in range(number):
    error = False
    word = input()
    for index in range(len(word)-1):
        if word[index] != word[index+1]:
            new_word = word[index+1:]
            if new_word.count(word[index]) > 0:
                error = True    
    if not error:
        count += 1
print(count)


# Test1
# number = 3
# word = ["happy", "new", "year"]
# 답 : 3

# Test2
# number = 4
# word = ["aba", abab", "abcabc", "a"]
# 답 : 1
