import re
import sys
input = sys.stdin.readline

a = input()
# p = re.compile('([0-9]+)([-+])?')
lst = re.findall('([0-9]{1,5}|[-+]?)', a)
op_cnt = lst.count('-')+ lst.count('+')
print(lst)

for i in range(op_cnt):
  for l in lst[:-2]:
    if l == '':
      continue
  
  