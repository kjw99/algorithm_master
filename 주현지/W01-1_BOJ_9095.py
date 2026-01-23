# https://www.acmicpc.net/problem/9095
# 9095 1, 2, 3 더하기
# 알고리즘: 다이나믹 프로그래밍 (DP)
# 핵심: n을 만드는 방식을 이전단계의 값으로 표현 (점화식)

'''
<1>
1
<2>
11 2
<3>
111 21 / 12 3
<4>
1111 211 121 31 / 112 22 / 13
<5>
11111 2111 1211 311 1121 221 131 / 1112 212 122 32 / 113 23

dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
'''

import sys
input = sys.stdin.readline

# 초기값 설정
dp = [0] * 12
dp[1] = 1
dp[2] = 2
dp[3] = 4

# n이 최대 11로 작아서 미리 계산해둠
for i in range(4, 11):
    dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
