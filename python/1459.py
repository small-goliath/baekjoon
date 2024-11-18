"""
문제
세준이는 학교에서 집으로 가려고 한다.
도시의 크기는 무한대이고, 도시의 세로 도로는 모든 정수 x좌표마다 있고, 가로 도로는 모든 정수 y좌표마다 있다.
세준이는 현재 (0, 0)에 있다. 그리고 (X, Y)에 위치한 집으로 가려고 한다.
세준이가 걸을 수 있는 방법은 두가지 인데,
하나는 도로를 따라서 가로나 세로로 한 블록 움직여서 이번 사거리에서 저 사거리로 움직이는 방법이고,
블록을 대각선으로 가로지르는 방법이 있다.

세준이가 집으로 가는데 걸리는 최소시간을 구하는 프로그램을 작성하시오.

입력
첫째 줄에 집의 위치 X Y와 걸어서 한 블록 가는데 걸리는 시간 W와 대각선으로 한 블록을 가로지르는 시간 S가 주어진다.
X와 Y는 1,000,000,000보다 작거나 같은 음이 아닌 정수이고, W와 S는 10,000보다 작거나 같은 자연수이다.
X Y W S

출력
첫째 줄에 세준이가 집에가는데 걸리는 최소시간을 출력한다.


4 2 3 10

18
(4 + 2) * 3


4 2 3 5

16
(x-y) * s + y * w


4 3 3 5

18
3 * 5 + 1 * 3


2 0 12 10

20
2 * 10 + 0 * 12


25 18 7 11

247
18 * 11 + 7 * 7


24 16 12 10

240


10000000 50000000 800 901

41010000000


135 122 43 29

3929

"""
import sys

input = sys.stdin.readline

x,y,w,s = map(int, input().split())

if x < y:
    temp = x
    x = y
    y = temp

if 2 * w < s:
    print((x + y) * w)
else:
    if s > w:
        print((y * s) + (x - y) * w)
    else:
        if (x - y) % 2 == 0:
            print(x * s)
        else:
            print((x - 1) * s + w)