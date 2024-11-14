"""
문제
어느 날, 타노스는 0과 1로 이루어진 문자열 S를 보았다.
신기하게도, S가 포함하는 0의 개수와 S가 포함하는 1의 개수는 모두 짝수라고 한다.

갑자기 심술이 난 타노스는 S를 구성하는 문자 중 절반의 0과 절반의 1을 제거하여 새로운 문자열 S'를 만들고자 한다.
S'로 가능한 문자열 중 사전순으로 가장 빠른 것을 구하시오.

입력
문자열 S가 주어진다.

출력
S'로 가능한 문자열 중 사전순으로 가장 빠른 것을 출력한다.

제한
S의 길이는 2 이상 500 이하이다.
S는 짝수 개의 0과 짝수 개의 1로 이루어져 있다.

서브태스크 1 (25점)
S의 길이는 4의 배수이다.
S의 홀수 번째 문자는 1, 짝수 번째 문자는 0이다.

서브태스크 2 (75점)
추가적인 제약 조건이 없다.

1010

01


000011

001
"""
import sys

s = str(sys.stdin.readline())

zero_qty = s.count("0") // 2
one_qty = s.count("1") // 2

# for _ in range(zero_qty // 2):
#     print(0, end='')
# for _ in range(one_qty // 2):
#     print(1, end='')

result = []
try_qty = 0

for num in s:
    if num == '\n':
        break
    if try_qty == one_qty:
        result.append(num)
        continue

    if num == '1':
        try_qty += 1
    else:
        result.append(num)

s_prime = "".join(map(str, result))
try_qty = 0
result = []

for num in s_prime[::-1]:
    if num == '\n':
        break
    if try_qty == zero_qty:
        result.append(num)
        continue

    if num == '0':
        try_qty += 1
    else:
        result.append(num)

print("".join(map(str, reversed(result))))
