from collections import deque

deq = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]

def BFS(x, y):
  deq.append((x, y))

  while deq:
    x, y = deq.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue

      if maze[nx][ny] == 0:
        continue

      if maze[nx][ny] == 1:
        maze[nx][ny] = maze[x][y] + 1
        deq.append((nx, ny))
    
  return maze[n-1][m-1]

print(BFS(0,0))