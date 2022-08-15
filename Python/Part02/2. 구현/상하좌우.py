''' 내가 쓴 코드 '''

# N 입력받기
n = int(input())

# 이동 계획 입력
x, y = 1, 1
plans = input().split()

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move = ['L', 'R', 'U', 'D']

for plan in plans:
  i = move.index(plan)
  nx = x + dx[i]
  ny = y + dy[i]
  print(i, nx, ny)
  
  if nx > n or ny > n or nx < 1 or ny < 1:
    continue
  else:
    x, y = nx, ny

print(x, y)


''' 책의 코드 '''
# 동일함
# 처음에 작성했을 때, x랑 y가 바뀌어 있었는데 이런거 잘 보고 작성하기