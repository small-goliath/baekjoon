"""
토리는 운동을 하고있는 모임에 참여하려고한다.
모임은 서로다른 운동 종목으로 구성된 운동 종목 리스트에 등록된 순서에 따라 진행하며 무제한 반복한다.
모든 종목은 각각의 수행 시간만큼 진행합니다.

운동 종목 리스트의 각 수행 시간(분)을 담은 exercise_list가 주어질 때, 총 exercise_time분 동안 운동을 수행할 때, 수행할 수 있는 운동 종목의 최댓값을 구하시오.
단, 각 종목을 1분만이라도 수행했어도 수행 개수에 포함시킵니다.


2 3 1 4
3

3


1 2 3 4
5

4


1 2 3 4
20

4
"""
from bisect import bisect_right

def solution(exercise_list: list, exercise_time: int) -> int:
    exercise_length = len(exercise_list)
    total = sum(exercise_list)

    if exercise_time >= total:
        return exercise_length

    extended_exercise_list = [0] * (2 * exercise_length + 1)
    for i in range(exercise_length):
        extended_exercise_list[i + 1] = extended_exercise_list[i] + exercise_list[i]

    for i in range(exercise_length + 1, 2 * exercise_length + 1):
        extended_exercise_list[i] = extended_exercise_list[i - exercise_length] + total

    max_exercise = 0
    for i in range(exercise_length):
        exercise = extended_exercise_list[i]
        minute = exercise_list[i]

        for off in range(minute):
            left = exercise + off
            light = left + exercise_time
            
            j = bisect_right(extended_exercise_list[i:i + (exercise_length + 1)], light - 1) + i - 1
            if j > i + exercise_length:
                j = i + exercise_length

            count = j - i + 1
            if count > exercise_length:
                count = exercise_length

            max_exercise = max(max_exercise, count)
            if max_exercise == exercise_length:
                break

        if max_exercise == exercise_length:
            break

    return max_exercise

exercise_list = [2,3,1,4]
exercise_time = 3
answer = solution(exercise_list, exercise_time)

print(answer == 3)

exercise_list = [1,2,3,4]
exercise_time = 5
answer = solution(exercise_list, exercise_time)

print(answer == 4)

exercise_list = [1,2,3,4]
exercise_time = 20
answer = solution(exercise_list, exercise_time)

print(answer == 4)