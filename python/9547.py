"""
문제
대선이 끝난 후 2주가 지났으나 여전히 결과는 발표되지 않았다. 결과가 궁금한 성제는 결과를 직접 미리 알아보기로 했다.
성제는 모종의 방법으로 투표에 참여한 모든 사람들에 대해 한 명도 빠짐없이 선호도 조사를 마쳤다. 성제는 투표에 참여한 사람들이 항상 선호도에 따라 투표했음을 알고 있다.
예를 들어 대통령 후보가 5명이고 어떤 유권자의 선호도가 [3, 2, 5, 1, 4] 인 상태에서 2번 후보와 4번 후보가 경합을 벌인다면, 이 유권자는 2번 후보에게 투표한다.

투표의 전체 규칙은 아래와 같다.
C명의 후보와 V명의 유권자가 있다. 각 후보는 1에서 C까지의 정수로 표현되며, V는 항상 홀수이다.
투표는 2회에 걸쳐 진행된다. 첫 투표에서는 모든 후보가 표를 받을 수 있으며, 만일 이 과정에서 어떤 후보가 모든 표 중 과반수 이상을 획득했다면 그대로 당선되며 투표가 종료된다.
만일 과반수 이상을 획득한 후보가 없다면 가장 많은 표를 받은 두 명만이 2회차에 진출하여 다시 투표를 진행한다. 이 경우엔 2회차에서 과반수 이상의 표를 받은 후보가 최종 당선된다.
1회차 투표에서 2등인 후보와 3등인 후보의 득표수는 항상 다르다.
유권자는 1회차와 2회차 투표 모두에서 후보들에 대해 동일한 선호도를 갖는다.
기권표는 없다.
성제가 조사한 선호도 표에 따라 최종 당선자를 알아내고, 그 당선자가 몇회차 투표에서 당선되었는지 성제에게 알려주도록 하자.

입력
첫 줄에 테스트 케이스의 수 T가 주어진다. ( 1 ≤ T ≤ 100 )

각 테스트 케이스의 첫 줄엔 후보의 수 C와 유권자의 수 V가 주어진다. ( 1 ≤ C, V ≤ 100 )
이어서 V줄에 걸쳐 C개의 정수로 각 유권자의 선호도 표가 주어진다.
가장 처음 주어지는 후보가 가장 선호하는 후보이며, 가장 마지막에 주어지는 후보가 가장 선호하지 않는 후보이다.
선호도 표에는 중복되는 정수가 없으며, 항상 1에서 C까지의 모든 정수를 정확히 한 번씩 포함하고 있다.

출력
각 테스트 케이스마다 당선된 후보의 번호와 투표가 종료된 회차(1 또는 2)를 공백으로 구분하여 출력한다.


2
2 3
2 1
1 2
2 1
3 5
1 2 3
1 2 3
2 1 3
2 3 1
3 2 1

2 1
2 2
"""
import sys

input = sys.stdin.readline

t = int(input())
c_arr = []
v_arr = []
preference_arr = []


for _ in range(t):
    c,v = map(int, input().split())
    c_arr.append(c)
    v_arr.append(v)

    temp = []
    for _ in range(v):
        temp.append(list(map(int, input().split())))
    preference_arr.append(temp)

for ti in range(t):
    winners = [i for i in range(c_arr[ti])]
    vote = [[0 for _ in range(c_arr[ti])] for _ in range(2)]

    for round in range(2):
        preferences = preference_arr[ti]
        
        for preference in preferences:
            index = 0
            while True:
                if preference[index] - 1 in winners:
                    vote[round][preference[index] - 1] += 1
                    break
                index += 1

        if max(vote[round]) > v_arr[ti] // 2:
            print(f"{vote[round].index(max(vote[round])) + 1} {round+1}")
            break

        winners = []
        winner_vote_qty = max(vote[round])
        for i,v in enumerate(vote[round]):
            if v == winner_vote_qty:
                winners.append(i)