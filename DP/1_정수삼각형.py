#[programmers] Level.3 정수 삼각형

"""
거쳐간 숫자의 합이 가장 큰 경우
숫자 최대값 return
"""



def solution(triangle):
    dp = triangle
    dp[0][0] = triangle[0][0]
    for i in range(len(triangle)):
        for j in range(i+1):
            if j == 0:
                a = 0
            else:
                a = triangle[i-1][j-1]
            if j == i:
                b = 0
            else:
                b = triangle[i - 1][j]
            val = max(a, b)
            dp[i][j] = triangle[i][j] + val
    return max(dp[len(triangle)-1])


arr = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(arr))

"""
def solution(triangle):

    height = len(triangle)

    while height > 1:
        for i in range(height - 1):
            triangle[height-2][i] += max([triangle[height-1][i], triangle[height-1][i+1]])
        height -= 1

    answer = triangle[0][0]
    return answer
"""