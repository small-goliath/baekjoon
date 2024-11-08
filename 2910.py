"""
5 2
2 1 2 1 2

2 2 2 1 1


9 3
1 3 3 3 2 2 2 1 1

1 1 1 3 3 3 2 2 2


9 77
11 33 11 77 54 11 25 25 33

11 11 11 33 33 25 25 77 54

이 메시지는 숫자 N개로 이루어진 수열이고, 숫자는 모두 C보다 작거나 같다. 창영이는 이 숫자를 자주 등장하는 빈도순대로 정렬하려고 한다.
만약, 수열의 두 수 X와 Y가 있을 때, X가 Y보다 수열에서 많이 등장하는 경우에는 X가 Y보다 앞에 있어야 한다. 만약, 등장하는 횟수가 같다면, 먼저 나온 것이 앞에 있어야 한다.
이렇게 정렬하는 방법을 빈도 정렬이라고 한다.
수열이 주어졌을 때, 빈도 정렬을 하는 프로그램을 작성하시오.
"""
import sys
from collections import Counter


N, C = map(int, sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split()))


frequencies = Counter(arr)
first_index = {num: idx for idx, num in reversed(list(enumerate(arr)))}

sorted_arr = sorted(set(arr), key=lambda x: (-frequencies[x], first_index[x]))

result = [num for num in sorted_arr for _ in range(frequencies[num])]

print(' '.join(map(str, result)))