# 2020 카카오 인턴쉽 코딩 테스트 문제
"""
키패드 누르기 문제(쉬움)
왼손 오른손 엄지 손가락을 가지고 키패드를 어떻게 누를까 푸는 문제.
키패드 사이의 거리를 유클리디안 거리로 구해 직관적으로 문제를 풀었지만, 더 쉬운 방법이 있을 수 있음.
"""

from collections import deque
def e_distance(d1, d2):
    return abs(d1[0] - d2[0]) + abs(d1[1] - d2[1])
    
def solution(numbers, hand):
    answer = ''
    number_pos = {'1':[0,0], '2':[0,1], '3':[0,2], '4':[1,0], '5':[1,1], '6':[1,2], '7':[2,0], '8':[2,1], '9':[2,2], '*':[3,0], '0':[3,1], '#':[3,2]}
    
    cur_lhand = number_pos['*']
    cur_rhand = number_pos['#']
    
    for num in numbers:
        str_num = str(num)
        if str_num in ['1','4','7']:
            cur_lhand = number_pos[str_num] 
            answer += 'L'
            
        elif str_num in ['3','6','9']:
            cur_rhand = number_pos[str_num]
            answer += 'R'
            
        else:   # [2,5,8,0]
            l_dis = e_distance(number_pos[str_num], cur_lhand)
            r_dis = e_distance(number_pos[str_num], cur_rhand)
            if l_dis == r_dis:
                answer += hand[0].upper()
                cur_rhand = number_pos[str_num] if answer[-1] == 'R' else cur_rhand
                cur_lhand = number_pos[str_num] if answer[-1] == 'L' else cur_lhand
            elif l_dis > r_dis:
                answer += 'R'
                cur_rhand = number_pos[str_num]
            else:
                answer += 'L'
                cur_lhand = number_pos[str_num]
    return answer
