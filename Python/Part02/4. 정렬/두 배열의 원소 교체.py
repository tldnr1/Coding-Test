# N, K 입력받기
n, k = map(int, input().split())

# 배열 A, B 입력받기
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

# k번 a 최대값과 b 최대값 비교 후 교체
for i in range(k):
  if a[i] < b[i]:
    a[i], b[i] = b[i], a[i]

print(sum(a))