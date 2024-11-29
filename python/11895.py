"""
문제
승현이는 남을 속이는 것을 참 좋아합니다. 오늘 승현이는 수열을 가지고 우리를 속여 보려고 합니다.

승현이는 길이가 n인 자연수로 구성된 수열 a1, a2, ⋯, an을 들고 왔습니다.
그러더니 갑자기 이 수열의 각 원소를 두 그룹 X나 Y 중 하나에 넣으라고 합니다.
편의상 X의 모든 원소를 X1, X2, ⋯, Xk, Y의 모든 원소를 Y1, Y2, ⋯, Yn−k로 둡시다. (단 k > 0,n−k > 0)

승현이는 X1 ⊕ X2 ⊕ ⋯ ⊕ Xk의 값과 Y1 ⊕ Y2 ⊕ ⋯ ⊕ Yn−k의 값이 같으면 우리에게 X1 + X2 + ⋯ + Xk원을 준다고 합니다.
승현이에게 너무 많이 속은 여러분은 믿기지 않지만, 돈을 잃을 일은 없으니 한 번 시도해 보기로 했습니다.
승현이가 제시한 수열 a가 주어질 때, 여러분이 돈을 받을 수 있는지, 돈을 받을 수 있다면 최대 얼마나 받을 수 있는지 구하는 프로그램을 작성하세요.

참고: ⊕는 배타적 논리합(XOR)를 뜻합니다. 자세한 설명은 여기와 여기를 참고하세요.

입력
첫 번째 줄에 n (1 ≤ n ≤ 1,000)이 주어지고,
두 번째 줄에 a1, a2, ⋯ ,an (1 ≤ a1, a2, ⋯, an ≤ 106)이 공백을 사이로 두고 주어집니다.

출력
첫 번째 줄에 여러분이 받을 수 있는 돈의 최댓값을 출력합니다. 만약 돈을 받을 수 없다면 0을 출력합니다.


3
1 2 3

5


4
1 2 3 4

0
"""
import sys
from functools import reduce

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

total_xor = reduce(lambda x, y: x ^ y, arr)

arr.sort()

if total_xor != 0:
    print(0)
else:
    print(sum(arr[1:]))