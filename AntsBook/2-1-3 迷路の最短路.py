from queue import Queue

n, m = map(int, input().split())
sx, sy = map(int, input().split())
gx, gy = map(int, input().split())
maze = [list(input()) for _ in range(n)]

vec = [(1, 0), (0, 1), (-1, 0), (0, -1)]

q = Queue()
d = [[float('inf')] * m for _ in range(n)]

q.put((sx, sy))
d[sx][sy] = 0

while (q.qsize()):
    x, y = q.get()
    if (x == gx and y == gy):
        break
    for v in vec:
        newx, newy = x + v[0], y + v[1]
        if 0 <= newx < n and 0 <= newy < m and maze[newx][newy] != '#' and d[newx][newy] == float('inf'):
            q.put((newx, newy))
            d[newx][newy] = d[x][y] + 1
print(d[gx][gy])
