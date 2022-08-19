# N, M 입력받기
n, m = map(int, input().split())

# 미로 입력받기
maze = []
for _ in range(n):
  maze.append(list(map(int, input())))

# 상하좌우 이동 정의
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
  
# bfs 기반 미로탈출 함수
from collections import deque
def bfs(x, y):
  # 처음 시작위치 큐에 저장
  queue = deque([(x,y)])

  # 인접 노드 탐색시작
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 상하좌우 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]   
      # 범위 밖의 경우 제외
      if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
        continue
      # 괴물이 있는 부분 무시
      if maze[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if maze[nx][ny] == 1:
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx,ny))
        
  # 가장 오른쪽 아래까지의 최단거리 반환
  return maze[n-1][m-1]
    
print(bfs(0,0))

