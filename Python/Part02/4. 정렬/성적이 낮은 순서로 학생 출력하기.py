# N 입력
n = int(input())

# N개의 (이름, 성적) 입력받아 리스트에 저장
array = []
for _ in range(n):
  name, score = input().split()
  array.append((name, int(score)))

array.sort(key = lambda x : x[1])

for i in range(n):
  print(array[i][0], end=' ')