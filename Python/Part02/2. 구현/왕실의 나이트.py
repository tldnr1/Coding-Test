''' 내가 쓴 코드 '''
pos = input() # a1
row = int(pos[1]) # 1
col = int(ord(pos[0]) - ord('a')) + 1 # a

steps = [(2,-1), (2,1), (-2,-1), (-2,1), (-1,2), (1,2), (-1,-2), (1,-2)]

cnt = 0
for step in steps:
  nrow = row + step[1]
  ncol = col + step[0]
  
  if nrow < 1 or nrow > 8 or ncol < 1 or ncol > 8:
    continue
  else:
    cnt += 1

print(cnt)


''' 책의 코드 '''
# 동일함
# 처음에는 dx, dy로 하려했다가 묶어서 정리함

# 1. dx dy로 나누어 정리 - 상하좌우 이렇게 자주 하는듯
# 2. (dx, dy)로 묶어서 정리 - 깔끔하게 정리하려면 이렇게 하는듯