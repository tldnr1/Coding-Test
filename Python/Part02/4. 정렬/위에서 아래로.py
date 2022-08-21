# N 입력받기
n = int(input())

# N 개의 정수 입력 후, 리스트에 저장
array = []
for _ in range(n):
  array.append(int(input()))

array.sort(reverse=True)

for i in range(n):
  print(array[i], end=' ')