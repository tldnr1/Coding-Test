''' 내가 쓴 코드 '''
n, m, k = map(int, input().split())
num = list(map(int, input().split()))

# num 정렬을 통해 max값 찾기
num.sort()
max1 = num[-1] # 가장 큰 수
max2 = num[-2] # 두번째로 큰 수, n>=2 이므로 오류 안생김

result = 0

cnt = 0
for i in range(1, m+1):
  if i-cnt*k >= k:
    result += max2
    cnt += 1
  else:
    result += max1

print(result)


''' 책의 코드 (입력이 매우 클 때 고려) '''
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort() # 입력받은 수 정렬
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

# 가장 큰 수가 더해지는 횟수 계산
count = int(m / (k+1)) * k  # 가장 큰 수 k번 + 두 번째 큰 수 1번 => k+1 개의 묶음
count += m % (k+1)  # k+1 개의 묶음을 돌고 남은 나머지 => 가장 큰 수를 마지막으로 더해줄 횟수

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m-count) * second # 두 번재로 큰 수 더하기

print(result)