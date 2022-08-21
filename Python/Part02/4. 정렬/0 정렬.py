def selection_sort(arr):
  pass

def insertion_sort(arr):
  pass

def quick_sort(arr):
  pass

def counting_sort(arr):
  pass


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
  quick_sort(array)
elif n == 4:
  counting_sort(array)
else:
  print('잘못된 입력입니다.')