"""
문제
선영이는 계산기와 컴퓨터에 매우 의존하는 학생이다. 따라서, 암산을 전혀 하지 못한다. (이건 사실이다)
하지만 선영이만 이런 것이 아니다. 상근이, 창영이, 종수 할아버지, 등등 많은 선영이의 친구도 간단한 계산을 전자기기의 도움 없이는 하지 못한다.

이런 까닭으로 어리석은 친구들이 이르고자 할 바가 있어도 마침내 제 뜻을 실어 펴지 못하는 사람이 많으니라.
나 선영이는 내 이를 위하여 가엾이 여거 새로 집합론을 기반으로 한 덧셈을 방법을 만들었다. 사람마다 하여 쉬이 익혀 날로 씀에 편안케 하고자 할 따름이니라.

이 방법은 음이 아닌 정수의 덧셈을 할 수 있다.
먼저, 음이 아닌 정수를 아래와 같이 집합으로 표현해야 한다.

0은 빈 집합 {} 이다.
0보다 큰 수 n은, n보다 작은 수를 모두 포함하는 집합으로 나타낸다.

아래 예는 0부터 3까지를 선영이의 방법으로 나타낸 것이다.
0 => {}
1 => {{}}
2 => {{},{{}}}
3 => {{},{{}},{{},{{}}}}
4 -> {{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}

집합의 원소의 개수는 그 수가 나타내는 값과 같다.
집합에 포함되어 있는 원소는 순서가 없다.
선영이는 사람들이 혼란스러워 하는 것을 막기 위해서 원소의 순서는 항상 그 원소(집합)의 크기가 증가하는 순서대로 쓴다고 정했다.
선영이의 집합 숫자 표기법으로 나타낸 두 수가 주어졌을 때, 두 수의 합을 다시 집합 숫자 표기법으로 나타내는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 두 줄로 이루어져 있고, 집합 숫자 표기법으로 나타낸 수가 주어진다. 두 수의 합은 항상 15보다 작거나 같다.

출력
각 테스트 케이스에 대해서 입력으로 주어진 두 수의 합을 집합 숫자 표기법으로 출력한다.


3
{}
{}
{{}}
{{},{{}}}
{{},{{}},{{},{{}}}}
{{}}

{}
{{},{{}},{{},{{}}}}
{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}

0
0
1
2
3
1

1
{{},{{}},{{},{{}}}}
{{},{{}}}

{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}},{{},{{}},{{},{{}}},{{},{{}},{{},{{}}}}}}
"""
import sys

input = sys.stdin.readline

t = int(input())

arr = ["{}", "{{}}"]
def get_hash(n):
    for i in range(2, n+1):
        arr.append("{" + arr[i-1][1:-1] + "," + arr[i-1] + "}")
    return arr[-1]

def to_num(s: str):
    s = s[1:-1]
    result = []
    count = 0
    temp = ""

    for char in s:
        if char == ",":
            continue

        temp += char
        if char == '{':
            count += 1
        elif char == '}':
            count -= 1
            
        if count == 0 and temp:
            result.append(temp)
            temp = ""
    return len(result)

x,y = [],[]

for _ in range(t):
    x.append(str(input().strip()))
    y.append(str(input().strip()))

for i in range(t):
    sum = to_num(x[i]) + to_num(y[i])

    if sum == 0:
        print("{}")
        continue
    elif sum == 1:
        print("{{}}")
        continue
    else:
        arr = ["{}", "{{}}"]
        print(f"{get_hash(sum)}")