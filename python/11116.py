"""
문제
승민이는 마포대교의 교통량이 얼마인지를 측정하고있다.
승민이는 도로 맞은 편을 잇는 두개의 끈을 일정 간격 사이로 매달아 놓았다. 그리고 자동차가 끈위로 지나갈때 끈 끝에 있는 작은 박스에는 그 때 의 시간이 기록된다. 

예를 들어, 자동차가 왼쪽에서 올 때 네 번의 기록을 얻게 된다.

왼쪽 줄 위로 앞 바퀴가 지나 간 시간 t
왼쪽 줄 위로 뒷 바퀴가 지나 간 시간 t + 500
오른쪽 줄 위로 앞 바퀴가 지나 간 시간 t + 1000
오른쪽 줄 위로 뒷 바퀴가 지나 간 시간 t + 1500
자동차가 오른쪽에서 올 때도 같은 규칙으로 오른쪽과 왼쪽을 바꾸어 측정하면 된다.
주어진 두개의 시간 기록으로 왼쪽에서 얼마나 많은 차가 왔는지 알아내면 된다.
한 끈 위에는 많아야 한 대의 차량이 지나가고 있다.

입력
첫 번째 줄에 n (1 ≤ n ≤ 100) 까지의 테스트 케이스의 개수를 입력 한다.
각각의 테스트 케이스에는 박스에서 측정 된 시간 기록의 개수 m (m ≤ 200)을 입력한다.
다음 줄에는 왼쪽 박스에서 측정된 10**9 보다 작은 시간 기록 m개를 입력한다.
그 다음 줄에는 오른쪽 박스에서 측정된 10**9 보다 작은 시간 기록 m개를 입력한다.

출력
각각의 테스트케이스에 대해 왼쪽에서 오는 차의 숫자를 출력한다.



2
4
17 517 1432 1932
432 932 1017 1517
6
235 451 735 951 2351 2851
1235 1351 1451 1735 1851 1951

1
2
"""
import sys

input = sys.stdin.readline
n = int(input())

left_box = []
right_box = []

for _ in range(n):
    m = int(input())
    left_box.append(list(map(int, input().split())))
    right_box.append(list(map(int, input().split())))


result = 0
def solution(t=0, n_index=0, index=0):
    global result

    if index == len(left_box[n_index]):
        print(result)
        return

    t = left_box[n_index][index]
        
    if t+500 in left_box[n_index] and t+1000 in right_box[n_index] and t+1500 in right_box[n_index]:
        result += 1


    solution(t,n_index, index+1)

for i in range(n):
    solution(0,i,0)
    result = 0