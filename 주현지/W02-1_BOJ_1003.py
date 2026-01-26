# https://www.acmicpc.net/problem/1003
# 1003 피보나치 함수
# 알고리즘: dp
# 핵심: 재귀로 구현하니까 시간초과남

'''
0 -> 1 0
1 -> 0 1
2 -> 1 1
3 -> 1 2
4 -> 2 3
5 -> 3 5
6 -> 5 8
7 -> 8 13
'''

import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    # a: 0이 출력되는 횟수, b: 1이 출력되는 횟수
    a, b = 1,0

    # n번 반복하며 피보나치 수열 계산 (Bottom-Up 방식)
    # n=1: (1, 0) -> (0, 1)
    # n=2: (0, 1) -> (1, 1)
    # n=3: (1, 1) -> (1, 2)
    for _ in range(n):
        a, b = b, a+b
    print(a,b)