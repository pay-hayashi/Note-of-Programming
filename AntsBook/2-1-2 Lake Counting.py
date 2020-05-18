n, m = map(int, input().split())
garden = [list(input()) for _ in range(n)]

def dfs(x,y):
    garden[y][x] = '.'
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            newx, newy = x + dx, y + dy
            if 0 <= newx < m and 0 <= newy < n and garden[newy][newx] == 'W':
                dfs(newx, newy)
    return

ans = 0

for i in range(n):
    for j in range(m):
        if garden[i][j] == 'W':
            dfs(j, i)
            ans += 1
print(ans)
