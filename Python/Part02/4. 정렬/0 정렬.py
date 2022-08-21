# '오름차순' 코드만 적혀있음
# 내림차순은 reversed를 통해 O(N)의 시간복잡도로 구현할 수 있기 때문!

def selection_sort(arr):
  for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
      if arr[min_index] > arr[j]:
        min_index = j
      arr[i], arr[min_index] = arr[min_index], arr[i] # Swap
  print(arr)

def insertion_sort(arr):
  for i in range(len(arr)):
    for j in range(i, 0, -1): # i부터 1까지 감소하며 반복
      if arr[j] < arr[i-1]: # 한 칸씩 왼쪽으로 이동
        arr[j], arr[j-1] = arr[j-1], arr[j]
      else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
        break
  print(arr)

def quick_sort(arr):
  # 리스트가 하나 이하의 원소만을 담고 있다면 종료
  if len(arr) <= 1:
    return arr

  pivot = arr[0] # 피벗은 첫 번째 원소
  tail = arr[1:] # 피벗을 제외한 리스트

  left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
  right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

  # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
  return quick_sort(left_side) + [pivot] + quick_sort(right_side)


def counting_sort(arr):
  # 모든 원소의 값이 0보다 크거나 같다고 가정 (계수 정렬의 조건!)

  # 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
  count = [0] * (max(arr) + 1)

  for i in range(len(arr)):
    count[arr[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

  for i in range(len(count)): # 리스트에 기록된 정렬 정보 확인
    for j in range(count[i]):
      print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력



print('-----------')
print('1. 선택 정렬')
print('2. 삽입 정렬')
print('3. 퀵 정렬')
print('4. 계수 정렬')
print('5. sorted()')
print('-----------')
print('선택 번호 : ', end='')
n = int(input())

array = [7,5,9,0,3,1,6,2,4,8]

if n == 1:
  selection_sort(array)
elif n == 2:
  insertion_sort(array)
elif n == 3:
  print(quick_sort(array))
elif n == 4:
  counting_sort(array)
elif n == 5:
  a = [(1,3), (0,3), (1,4), (1,5), (0,1), (2,4)]

  # 아이템 첫 번째 인자를 기준으로 '오름차순으로 먼저 정렬'하고,
  # 그리고 그 안에서 다음 '두 번재 인자를 기준'으로 '내림차순'으로 정렬
  res = sorted(a, key = lambda x : (x[0], -x[1]))
  print(res)
else:
  print('잘못된 입력입니다.')