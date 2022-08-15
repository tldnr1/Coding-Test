''' 내가 쓴 코드 '''
n = int(input())

# 1시간 = 60분 = 3600초
# n은 최대 23, 23*3600 <= 10만
# 따라서 그냥 반복문을 작성 (제한시간 2초)

cnt = 0
for h in range(n+1):
  for m in range(60):
    for s in range(60):
      if '3' in str(h)+str(m)+str(s):
        cnt += 1

print(cnt)


''' 책의 코드 '''
# 동일함
# 12번재 줄의 str 합치기 아이디어 중요
#  ㄴ 문자열 합치기를 통해 한 번에 비교하기