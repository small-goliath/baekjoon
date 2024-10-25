"""
3
7
2
10
0
20
29
31
0
42
41
40
37
20
0

134
17744
Too expensive
"""

T = int(input())
testcase = []
testcases = []
count = 0

while True:
    if count == T:
        break

    case = int(input())
    if case == 0:
        count += 1
        testcases.append(testcase)
        testcase = []

    else:
        testcase.append(case)

my = 5 * (10 ** 6)
for cases in testcases:
    cases = list(cases)
    cases.sort(reverse=True)
    total = 0
    for i, c in enumerate(cases):
        total += 2 * (c ** (i+1))

    if total > my:
        print("Too expensive")
    else:
        print(total)