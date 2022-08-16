# 꼭 필요한 자료구조 기초
- 스택 : First in Last Out 구조
  - stack = [] 처럼, 리스트로 스택 구현
  - 가장 위에 넣고, 가장 위에서 빼야함
    - stack.append(n)
    - stack.pop()

- 큐 : First in First Out 구조
  - queue = deque() 처럼, deque를 사용
     - from collections import deque 를 먼저 해주어야 함
  - 넣은 차례대로 나오게 해야함 (뒤에다가 이어 붙이고, 나올 땐 앞에서부터)
    - queue.append(n)
    - queue.popleft()  # 왼쪽에서 pop 하기
  - deque 객체는 사용을 위해서 list(deque)를 통해 리스트로 자주 바꿈

- 재귀함수
  - 함수 내에서 그 함수를 호출 (예시 : 팩토리얼 구하기)
    - 대신, 너무 많이 재귀가 이루어지면 재귀깊이의 한계로 코드가 작동하지 않음
    - 즉, 코딩테스트에서 너무 깊은 재귀는 시간초과가 발생!
      - 해결을 위해 메모이제이션(Memoization) 기법 등을 활용함
  - "탈출조건" 을 잘 설정해주어야 함 (예시 : 팩토리얼에서는 n = 0이면 f(n) = 1)
  