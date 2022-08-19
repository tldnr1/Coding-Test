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