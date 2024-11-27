"""
문제
컴퓨터공학과 학생인 영재는 이번 학기에 알고리즘 수업을 수강한다.
평소에 자신의 실력을 맹신한 영재는 시험 전날까지 공부를 하지 않았다.
당연하게도 문제를 하나도 풀지 못하였지만 다행히도 문제가 5지 선다의 객관식 10문제였다.
찍기에도 자신 있던 영재는 3개의 연속된 문제의 답은 같지 않게 한다는 자신의 비법을 이용하여 모든 문제를 찍었다.

이때 영재의 점수가 5점 이상일 경우의 수를 구하여라.
문제의 점수는 1문제당 1점씩이다.

입력
시험의 정답이 첫 줄에 주어진다.

출력
영재의 점수가 5점 이상일 경우의 수를 출력하여라.


1 2 3 4 5 1 2 3 4 5

261622
"""
import sys

input = sys.stdin.readline

answers = list(map(int, input().split()))
exactly_qty = 0

def solution(index, pick, matches):
    global exactly_qty
    
    if index == 10:
        if matches >= 5:
            exactly_qty += 1
        return

    for num in range(1, 6):
        if index >= 2 and pick[-1] == pick[-2] == num:
            continue

        new_matches = matches + 1 if num == answers[index] else matches
        pick.append(num)

        solution(index + 1, pick, new_matches)
        pick.pop()

solution(0, [], 0)
print(exactly_qty)