def solution(s):
    stack = []
    if len(s) < 2:
        return 0
    
    for _s in s:
        if len(stack) == 0:
            stack.append(_s)
        else:
            if stack[-1] == _s:
                stack.pop()    
            elif stack[-1] != _s:
                stack.append(_s)
            
    if len(stack) > 0:
        answer = 0
    else:
        answer = 1        
    return answer

# 테스트용
sen = ["baabaa", "cdcd"]
for _s in sen:
  print(solution(_s))
