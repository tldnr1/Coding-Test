''' 내가 쓴 코드 '''
n = int(input())

coins = [500, 100, 50, 10]

cnt = 0
for coin in coins:
  cnt += n//coin
  n %= coin

print(cnt)


''' 책의 코드 '''
# 동일함, 근데 주석을 달아주면 좋을듯

# 그리고 '동전의 종류' 이니까 coins 대신에 coin_types 로 이름 정해주는게 더 어울리는 것 같음