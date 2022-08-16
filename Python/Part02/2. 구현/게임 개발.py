''' 내가 쓴 코드 '''
import sys
input = sys.stdin.readline

# N, M을 입력받기
n, m = map(int, input().split())

# 이동 경로 측정
tracking = [[0] * m for _ in range(n)]
x, y, d = map(int, input().split())
tracking[x][y] = 1  # 현위치 방문 기록

# 맵 생성
world = []
for _ in range(n):
  world.append(list(map(int, input().split())))

print(world)
print(tracking)

# 북, 동, 남, 서 이동
dx = [-1, 0, 1, 0]  # 행의 변화 = 세로 이동
dy = [0, 1, 0, -1]  # 열의 변화 = 가로 이동


# 왼쪽 방향 찾기
def turn_left(d):
  if d == 0:
    return 3
  else:
    return d - 1

cnt = 1
turn_cnt = 0
while True:
  d = turn_left(d)
  nx = x + dx[d]
  ny = y + dy[d]

  # 왼쪽 방향에 길이 있는 경우
  if world[nx][ny] == 0 and tracking[nx][ny] == 0:
    x, y = nx, ny
    tracking[nx][ny] = 1
    turn_cnt = 0
    cnt += 1
    continue
  # 왼쪽 방향에 길이 없는 경우
  else:
    turn_cnt += 1

  # 4 방향을 모두 확인한 경우
  if turn_cnt == 4:
    nx = x - dx[d]
    ny = y - dy[d]
    # 뒤로 갈 수 있다면 이동
    if world[nx][ny] == 0:
      x, y = nx, ny
    else:
      break
    turn_cnt = 0

print(cnt)


''' 책의 코드 '''
# 책 코드 참고해서 작성함
# 다시 풀어봐야 할 문제!

# 1. 맵이랑 이동경로 따로 저장해서 풀지 않았음
# 2. 4번 회전한 걸, 어떻게 표기할지 몰라서 잘 못했음
# 3. 이동 상에서 turn_cnt를 어떻게 설정해줘야 할지 잘 몰랐음