"""
4
3
0
4
0

0


10
1
3
5
4
0
0
7
0
0
6

7
"""

N = int(input())
numbers = []
p = []
for _ in range(N):
    numbers.append(int(input()))

for i in numbers:
    if i == 0:
        p.pop()
    else:
        p.append(i)

print(sum(p))
