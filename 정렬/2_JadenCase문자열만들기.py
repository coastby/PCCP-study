# [programmers] Level.2 JadenCase 문자열 만들기

"""
모든 단어의 첫 문자가 대문자

대문자로 바꾸는 함수
string.upper()
"""

def solution(s):
    strs = s.split()
    for i in range(len(strs)):
        strs[i] = strs[i].capitalize()
    answer = " ".join(strs)
    return answer


print(solution("3people unFollowed me"))

"""
def Jaden_Case(s):
    # 함수를 완성하세요   
    s = ' '.join(((word[0].upper()) + word[1:].lower()) for word in s.split())  
    return s
"""