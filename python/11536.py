"""
5
JOE
BOB
ANDY
AL
ADAM

DECREASING


11
HOPE
ALI
BECKY
JULIE
MEGHAN
LAUREN
MORGAN
CARLI
MEGAN
ALEX
TOBIN

NEITHER


4
GEORGE
JOHN
PAUL
RINGO

INCREASING
"""

N = int(input())
names = []
for _ in range(N):
    names.append(input())

print(reversed(names))
if sorted(names) == names:
    print("INCREASING")
elif sorted(names, reverse=True) == names:
    print("DECREASING")
else:
    print("NEITHER")