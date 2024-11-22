"""
문제
2×n 크기의 직사각형을 1×2, 2×1 타일로 채우는 방법의 수를 구하는 프로그램을 작성하시오.
아래 그림은 2×5 크기의 직사각형을 채운 한 가지 방법의 예이다.

입력
첫째 줄에 n이 주어진다. (1 ≤ n ≤ 1,000)

출력
첫째 줄에 2×n 크기의 직사각형을 채우는 방법의 수를 10,007로 나눈 나머지를 출력한다.

1

1

6


9

55
"""
# import sys

# input = sys.stdin.readline

# n = int(input())

# def solution(n):
#     dp = [0] * (n)
#     dp[0] = 1
#     dp[1] = 2

#     for i in range(2, n):
#         dp[i] = (dp[i - 2] + dp[i - 1]) % 10007

#     return dp[n - 1]

# if n == 1:
#     print(1)
# elif n == 2:
#     print(2)
# else:
#     print(solution(n))


import sys

input = sys.stdin.readline

n = int(input())
def solution(n):
    p, c = 1, 2
    for _ in range(2, n):
        p, c = c, (p + c) % 10007

    return c


if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    print(solution(n))