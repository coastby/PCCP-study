# [programmers] Level.2 폰켓몬

"""
가장 많은 폰켓몬을 선택하는 방법
최대로 다양하게 고를 때 그 폰켓몬 종류의 수

폰켓몬 종류가 200,000
"""


def solution(nums):
    s = set()
    for n in nums:
        s.add(n)
    if len(s) >= (len(nums)//2):
        return len(nums)//2
    else:
        return len(s)