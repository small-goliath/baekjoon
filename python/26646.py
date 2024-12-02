"""
문제
( 그림 )

ALPS 부원들은 친목 도모를 위해 다 같이 알프스 산맥으로 여행을 떠났다!
알프스 산맥은 N개의 산이 겹치거나 빈 부분 없이 일렬로 나열된 형태이며, 왼쪽에서부터 i번째에 위치한 산은 빗변을 아래로 하며 높이가 H_i인 직각 이등변 삼각형이다.

ALPS 부원들은 체력이 좋지 않기 때문에 1번 산에서 시작해 N번 산에서 끝나는 케이블카 노선을 설치해 산을 오르려 한다.
노선을 설치하는 법은 다음과 같다.

1번 산의 정상과 다른 산의 정상을 직선으로 잇는 와이어를 설치하고, 다시 그 산의 정상에서 다른 산의 정상으로 와이어를 설치한다.
이 때 와이어는 산을 가로질러 설치될 수 있다.
이를 N번 산을 끝으로 할 때까지 자유롭게 반복한다.
각 와이어의 설치 비용은 설치해야 할 와이어 길이의 제곱과 같으며 노선의 설치 비용은 사용한 와이어의 설치 비용의 합이다.
ALPS 부원들을 위해 1번 산에서 시작해 N번 산에서 끝나는 노선을 설치하기 위한 최소 비용을 구해보자.

입력
첫 번째 줄에 알프스 산맥을 이루는 산의 수 N이 주어진다. 
(2 <= N <= 50,000)

두 번째 줄에 각 산의 높이 H_1, H_2, ..., H_N이 공백으로 구분되어 정수로 주어진다. 
(1 <= H_i <= 100)

출력
1번 산에서 시작해 N번 산에서 끝나는 노선을 설치하기 위한 최소 비용을 출력한다.


4
4 2 3 4

116


2
1 1

4
"""
import sys
from functools import reduce

input = sys.stdin.readline

n = int(input())
h = list(map(int, input().split()))

# def get_wire_price(index1: int, index2: int):
#     from_loc = reduce(lambda x, y: x + y, h[0:index1+1]) * 2 - h[index1]
#     to_loc = reduce(lambda x, y: x + y, h[0:index2+1]) * 2 - h[index2]
#     return ((to_loc - from_loc) ** 2) + ((h[index2] - h[index1]) ** 2)

def solution(n: int, h: list):
    total_price = 0
    for i in range(1, n):
        total_price += (h[i-1] + h[i]) ** 2 + (h[i-1] - h[i]) ** 2

    return total_price

print(solution(n,h))