# [programmers] Level.2 가장 큰 수

"""
재배치하여 만들 수 있는 가장 큰 수

앞자리가 큰 순서대로 정렬
기수 정렬

numbers : 0 ~ 1000
첫번째 자리 9: 9 900 909 90 91
-> 9 91 909 90 900
445 455 453 45

첫째 자리 -> 둘째 자리 -> 셋째 자리
9 | 91 | 909 90 900
9 | 91 | 909 90 900

1000 > 0

못 풀었다. 다시 풀기.
1) comparator 기준 재설정하기 -> 자바에 적합
2) 3번 반복해서 비교하기
"""

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x : x * 3, reverse = True)
    answer="".join(numbers)
    return answer


numbers = [3, 30, 34, 5, 9]
print(solution(numbers))

"""
1.로 풀이
import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) #  t1이 크다면 1  // t2가 크다면 -1  //  같으면 0

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer
    

또는
from functools import cmp_to_key

def solution(numbers):
    numbers = list(map(lambda x: str(x), numbers))
    numbers = sorted(numbers, key=cmp_to_key(lambda a, b: -1 if a+b >= b+a else 1))
    answer = ''.join(numbers)

    return str(int(answer))
"""