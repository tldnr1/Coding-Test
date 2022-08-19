''' 내가 쓴 코드 '''
import sys
input = sys.stdin.readline

# N, M 입력받기
n, m = map(int, input().split())

# 얼음 틀 입력받기
graph = []
for _ in range(n):
  graph.append(list(map(int, input().rstrip())))

  
# dfs 기반, 아이스크림 탐색 함수
def find_ice(i,j):
  # 범위 밖을 탐색하는 경우 즉시 종료
  if i<=-1 or i>=n or j<=-1 or j>=m:
    return False

  # 아직 방문하지 않은 노드인 경우
  if graph[i][j] == 0:
    # 해당 노드 방문 처리
    graph[i][j] = 1
    # 상하좌우 탐색
    find_ice(i-1,j)
    find_ice(i+1,j)
    find_ice(i,j-1)
    find_ice(i,j+1)
    return True
  return False

cnt = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 dfs 수행
    if find_ice(i,j) == True:
      cnt += 1

print(cnt)


''' 책의 코드 '''
# 약간 다름

# readline으로 받아서 rstrip()으로 뒤에 공백 제거해주어야 함
# 그리고 입력에서 끝이 0으로 끝나는게 있으므로 split()은 사용하면 안됨

# 처음에 생각하지 못했던 부분은
# 얼음 덩어리 개수를 판단할 때, 처음시작에서 True처리한 뒤 나머지 붙은건 그냥 방문만 하면 된다는 아이디어였음
# 이걸 떠올리기 전에는 cnt 등을 쓸 생각이였음