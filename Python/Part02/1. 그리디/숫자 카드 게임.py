''' 내가 쓴 코드 '''
# N, M을 공백으로 구분하여 입력받기
n, m = map(int, input().split())

result = 0
for i in range(n):
  # 카드 한 행 공백으로 구분하여 입력받기
  card = map(int, input().split())

  # 입력받은 행에서 최솟값 구하기
  temp = min(card)

  # 행의 최솟값이 전체의 최댓값인지 확인
  if temp > result: result = temp

print(result)


''' 책의 코드 '''
# 동일함
# 변수 이름을 조금 다듬으면 좋을 듯
#  ㄴ 책에서는 card 대신 data를 썼는데
#     일반적이면 data로 하고, 지금처럼 의미가 있으면 의미있는 이름으로 하는것도 괜찮을 듯
#  ㄴ 그리고 temp 대신에 최솟값을 의미하는 min_value 로 이름을 지었으면 좀 더 좋았을 듯