"""
브실이는 집에 들어가고 싶지만, 도어락의 비밀번호를 까먹어버렸다.
도어락의 비밀번호는 1부터 9까지의 숫자가 최대 1번씩 들어간 N자리의 정수이다. 브실이는 비밀번호를 한 번 입력할 때마다 X초가 걸린다.
도어락에 비밀번호를 연속하여 3번 입력해 모두 실패할 때마다, Y초 동안 비밀번호를 입력할 수 없게 된다. 
Y초를 기다린 후에는 비밀번호 입력 횟수가 초기화된다.

집에 최대한 빨리 들어가고 싶었던 브실이는 곰곰이 생각해 본 결과, 다행히 비밀번호의 일부 정보를 기억해 냈다.
브실이는 가진 정보를 활용하여 입력에 실패한 횟수가 현재 0회인 도어락에 가능한 비밀번호를 모두 한 번씩 입력해 보기로 했다.
브실이가 집에 들어가는데 걸리는 최대 시간을 구해보자.

첫 번째 줄에 비밀번호의 자릿수 N과 브실이가 비밀번호에 대해 기억하는 정보의 수 M이 공백으로 구분되어 주어진다. 
( 3 <= N <= 9;  0 <= M <= N )

두 번째 줄에 비밀번호를 입력하는 데 걸리는 시간을 나타내는 정수 X, 비밀번호를 입력할 수 없는 시간을 나타내는 정수 Y가 공백으로 구분되어 주어진다. 
( 1 <= X, Y <= 10 )

세 번째 줄부터 M개의 줄에 걸쳐 비밀번호에 대한 정보를 뜻하는 정수 a, b가 공백으로 구분되어 주어진다. 
( 0 <= a <= N; 1 <= b <= 9 )


a != 0이면, 비밀번호의 a번째 자리의 값이 b라는 것을 의미한다.
a = 0이면, 비밀번호 중 한 자리의 값이 b라는 것을 의미한다.
단, 같은 자리나 같은 숫자에 대한 정보가 여러 번 주어지지 않는다.

가진 정보를 활용하여 브실이가 집에 들어가는데 걸리는 최대 시간을 초 단위로 출력한다.


4 4
3 10
1 2
0 1
0 3
4 8

6


4 0
3 10

19142

4 4
3 10
1 1
2 2
3 3
4 4

3

4 4
1 1
1 1
2 2
3 3
0 4

c 1
r 1

4 4
1 1
1 1
2 2
0 3
0 4

c 2
r 2

4 4
1 1
1 1
0 2
0 3
0 4

c 6
r 7


4 4
1 1
0 1
0 2
0 3
0 4

c 24
r 31


4 3
1 1
1 1
0 2
0 3

c 12
r 15
"""
import sys
from math import comb, factorial, prod, perm

N, M = map(int, sys.stdin.readline().split())
X, Y = map(int, sys.stdin.readline().split())
guess_qty = 0
confirm_qty = 0
password_bundle = []

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    if a != 0:
        confirm_qty += 1
    if a == 0:
        guess_qty += 1

def get_count(guess_qty: int, confirm_qty: int, n: int):
    if guess_qty == 0:
        return perm(9 - confirm_qty, n - confirm_qty)
    
    if confirm_qty != 0:
        if guess_qty + confirm_qty == n:
            return factorial(guess_qty)
        
        possible_qty = 9 - confirm_qty - guess_qty
        
        if guess_qty == 1:
            return (n - confirm_qty) * perm(possible_qty, n - (confirm_qty + guess_qty))
        return comb(n-confirm_qty, guess_qty) * factorial(guess_qty) * perm(possible_qty, n - (confirm_qty + guess_qty))
    
    if confirm_qty == 0:
        if guess_qty + confirm_qty == n:
            return factorial(guess_qty)
        
        possible_qty = 9 - confirm_qty - guess_qty
        return comb(possible_qty, n - guess_qty) * factorial(n)

def get_result(n: int, m: int, x: int, y: int, password_bundle: list) -> int:
    count = get_count(guess_qty, confirm_qty, n)
    print(f"count: {count}")
    wait = count * x

    if count > 3:
        if count % 3 == 0:
            wait += (y * ((count // 3) - 1))
        else:
            wait += (y * (count // 3))
            
    return wait

print(get_result(N,M,X,Y,password_bundle))