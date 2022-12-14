#[Programmers] Level.1 체육복
"""
근처 학생에게만 체육복을 빌릴 수 있음
체육 수업을 들을 수 있는 학생의 최댓값 return

lost 학생 근처가 reserve에 있으면 배열에서 제외
만약 24 35 이렇게 있다면??
1 1 0 2 0 2 1
1 1 2 0 2 0 1 0 2 0 1
"""

def solution(n, lost, reserve):
    arr = [1] * (n+1)
    for s in lost:
        arr[s] -= 1
    for s in reserve:
        arr[s] += 1
    str_num = ""
    for a in arr:
        str_num += str(a)
    str_num = str_num.replace("0202", "1")
    str_num = str_num.replace("2020", "1")
    str_num = str_num.replace("20", "1")
    str_num = str_num.replace("02", "1")
    answer = n- str_num.count("0")
    return answer

#답에 가까운 풀이
#앞에 애가 빌려보고 없으면 뒤에 애한테 어차피 빌려야한다.
def solution(n, lost, reserve):
    arr = [1] * (n+1)
    for s in lost:
        arr[s] -= 1
    for s in reserve:
        arr[s] += 1
    for i in range(n+1):
        if(arr[i] == 0 and arr[i-1] == 2):
            arr[i] = 1;
            arr[i-1] = 1;
        elif (i != n and arr[i] == 0 and arr[i+1] == 2):
            arr[i] = 1
            arr[i+1] = 1
    answer = n - arr.count(0)
    return answer