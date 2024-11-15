"""
4 4
1 2 2 3
2 2 1 1
3 2 1 2
1 2 2 2

1
2

6 5
3 1 1 2 1
4 2 1 3 1
4 1 1 3 3
4 3 3 1 2
5 1 1 2 2
3 2 3 3 3

3
2 3 4

5 6
5 2 3 3 1 1
4 2 2 1 1 3
3 1 2 2 1 3
5 3 2 1 1 2
3 2 3 3 3 2

0


"""

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
star = []
xs = set()

def not_valid(x: int, y: int) -> bool:
    return x < 0 or x >= N or y < 0 or y >= M
    
def is_visited(x: int, y: int, s: int, w: str) -> bool:
    loc = f"{x}{y}{w}"

    if loc in star:
        xs.add(s + 1)
        return True
    return False
    
def main():
    for i in range(N):
        star.clear()
        x = i
        y = 0
        w = "r"
        loc = f"{x}{y}{w}"
        star.append(loc)

        while True:
            w = "d"
            y = y + grid[x][y]
            if not_valid(x, y) or is_visited(x, y, i, w):
                break
            loc = f"{x}{y}{w}"
            star.append(loc)

            w = "l"
            x = x + grid[x][y]
            if not_valid(x, y) or is_visited(x, y, i, w):
                break
            loc = f"{x}{y}{w}"
            star.append(loc)

            w = "u"
            y = y - grid[x][y]
            if not_valid(x, y) or is_visited(x, y, i, w):
                break
            loc = f"{x}{y}{w}"
            star.append(loc)

            w = "r"
            x = x - grid[x][y]
            if not_valid(x, y) or is_visited(x, y, i, w):
                break
            loc = f"{x}{y}{w}"
            star.append(loc)
    print(len(xs))
    if xs:
        print(' '.join(map(str, sorted(xs))))

if __name__ == "__main__":
	main()