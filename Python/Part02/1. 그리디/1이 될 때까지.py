''' 내가 쓴 코드 '''
# N, K를 공백으로 구분하여 입력받음
n, k = map(int, input().split())

cnt = 0

# K로 나누어 떨어지게 만드는게 가장 횟수가 적음
while n%k != 0:
  n -= 1
  cnt += 1

while n != 1:
  n /= 5
  cnt += 1

print(cnt)


''' 책의 코드 '''
# 동일함 (코드만 다르고, 이론이 같음)