"""
학생들은 1번부터 N번까지 번호표를 가지고 있다. 학생들은 번호표에 따라 순서대로 줄을 서려고 한다. 
1번 번호표를 가진 학생은 줄에 처음으로 서게 되고, 이때 만족도는 s_1이다. 2번 번호표를 가진 학생부터는 다음 두 가지 행동 중 하나를 선택해 줄을 선다.

맨 앞에 서기: 줄의 맨 앞에 서게 되고, 이때 i번 학생의 만족도는 s_i이다.
맨 뒤에 서기: 줄의 맨 뒤에 서게 되고, 이때 i번 학생의 만족도는 0이다.
또한 줄을 서는 방법에 따라 기존 학생의 만족도가 변화할 수 있다.

만약 i번 학생 앞에 j(j > i)번 학생이 있다면 새치기를 당했기 때문에 i번 학생의 만족도가 −s_i로 변한다.
기존 만족도가 0이었더라도 -s_i로 변할 수 있음에 유의하라.
만약 i번 학생 앞에 j(j > i)번 학생이 없다면 새치기를 당하지 않았기 때문에 i번 학생의 만족도는 변하지 않는다.
식당 도우미인 여러분은 문득 각 학생의 만족도 총합을 최대화하는 방법이 궁금해졌다. 만족도 총합의 최댓값을 구해보자.

2
1 10

9


3
10 1 1

10


4
1 2 4 1

1

4
3 2 4 8
"""

import sys

N = int(sys.stdin.readline())
s = list(map(int,sys.stdin.readline().split()))

