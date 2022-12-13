# [Programmers] 입국 심사

"""
모든 사람이 심사받는데 걸리는 시간을 최소로

입국심사 사람 1 ~ 10,000,000,000
한 명 심사하는데 걸리는 시간 1 ~ 10,000,000,000
심사관 1 ~ 100,000

최소 시간 = math.ceil(min * n / len(times))
최대 시간 = max * n

answer

answer//times[0] + answer//times[1] + .. = n

"""
from math import ceil


def soultion (n, times):
    answer = 0
    lo = ceil(min(times) * n / len(times))
    mx = ceil(max(times) * n / len(times))
    while lo < mx:
        mid = (lo + mx)//2
        sum = 0
        for i in range(len(times)):
            sum += mid // times[i]
        if sum > n:
            mx = mid - 1
        elif sum < n:
            lo = mid + 1
        else:
            answer = mid
    return answer