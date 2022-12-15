# [programmers] Level.2 올바른 괄호

def solution(s):
    cnt = 0
    for i in s:
        if cnt < 0:
            return False
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
    return cnt == 0