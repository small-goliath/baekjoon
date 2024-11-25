"""
문제
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- N개의 자연수 중에서 M개를 고른 수열
- 고른 수열은 비내림차순이어야 한다.
- 길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

입력
첫째 줄에 N과 M이 주어진다. (1 ≤ M ≤ N ≤ 8)
둘째 줄에 N개의 수가 주어진다. 입력으로 주어지는 수는 10,000보다 작거나 같은 자연수이다.

출력
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력한다. 중복되는 수열을 여러 번 출력하면 안되며, 각 수열은 공백으로 구분해서 출력해야 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.



3 1
4 4 2

2
4


4 2
9 7 9 1

1 7
1 9
7 9
9 9


4 4
1 1 2 2

1 1 2 2
"""
import sys

input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()

temp = [0] * m
result = []

def solution(v, index):
    if v == m:
        t = " ".join(map(str, temp))
        if not t in result:
            result.append(t)
        return

    for i in range(index, n):
        temp[v] = arr[i]
        solution(v+1, i+1)

solution(0, 0)

for r in result:
    print(r)