"""
문제
시흠이는 군대에 가기 전까지 자신과 놀아준 친구 N(1 ≤ N ≤ 1000)명에게 선물을 주려고 한다.
시흠이는 돈을 B(1 ≤ B ≤ 1,000,000,000)원 가지고 있다.
i번째 친구가 받고 싶어하는 선물의 가격은 P(i)원이고, 배송비는 S(i)원이다. 즉, 시흠이가 i번째 친구에게 선물을 보내려면 돈이 P(i)+S(i)원 필요하다.
시흠이는 물건 가격을 절반으로 할인받을 수 있는 쿠폰을 하나 가지고 있다. 이 쿠폰을 i번째 친구에게 사용한다면, ⌊P(i)/2⌋+S(i)원만 있으면 선물을 보낼 수 있다.
시흠이가 선물을 최대 몇 명에게 보낼 수 있는지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 B가 주어진다.
둘째 줄부터 N개 줄에는 P(i)와 S(i)가 주어진다. (0 ≤ P(i), S(i) ≤ 1,000,000,000)

출력
첫째 줄에 시흠이가 선물을 최대 몇 명에게 보낼 수 있는지 출력한다.

힌트
1, 2, 4번 친구의 선물을 구매하고, 3번 친구의 선물을 쿠폰을 써서 구매하면 된다. (4+2)+(2+0)+(4+1)+(6+3) = 22 이기 때문에, B원으로 모두 구매하고 배송보낼 수 있다.
또, 1번이나 4번 친구에게 쿠폰을 써도 된다.


5 24
4 2
2 0
8 1
6 3
12 5

4


5 24
4 2
2 0
8 9
5 3
12 0

4
"""
import sys

input = sys.stdin.readline

n, b = map(int, input().split())
prices = [list(map(int, input().split())) for _ in range(n)]
qtys = []

for i in range(n):
    one_by_one = []

    for j in range(n):
        if i == j:
            one_by_one.append(prices[j][0] // 2 + prices[j][1])
        else:
            one_by_one.append(prices[j][0] + prices[j][1])

    one_by_one.sort()
    qty = 0
    total = 0

    for j in range(n):
        total += one_by_one[j]

        if total > b:
            break
        
        qty += 1
    qtys.append(qty)

print(max(qtys))