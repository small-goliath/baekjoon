from itertools import product
import sys

input = sys.stdin.readline

n = int(input())
s = input().strip()

binary_numbers = [''.join(bits) for bits in product('01', repeat=n)]
binary_numbers.sort(key=lambda x: (x.count('1'), x[::-1]))

print(binary_numbers.index(s))
