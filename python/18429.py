"""
3 4
3 7 5

4
"""

import sys
N, K = map(int, sys.stdin.readline().split())
kit = list(map(int,sys.stdin.readline().split()))
visited = [0] * N
count = 0

def search(w: int, n: int):
    global count

    if w < 500:
        # print(f"Failed!!!")
        return
    if n == N:
        count += 1
        # print(f"counting!!! {count}")
        return

    w -= K
    for i in range(N):
        # print(f"{n}일 째, {w+K}kg에 {kit[i]}사용")
        w += kit[i]
        if not visited[i]:
            visited[i] = 1
            search(w, n + 1)
            visited[i] = 0

search(500, 0)
print(count)