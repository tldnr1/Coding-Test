def solution(name):
    # name -> 'AAA..' 에 필요한 조작 횟수 찾기
    res = 0
    only_A = "A" * len(name)
    
    # cursor을 통해 좌우 탐색하면서 방향 정하기
    cursor = 0    
    for _ in range(len(name)):
        if name == only_A:
            break
        
        # 좌우로 A가 가까운 방향 탐색
        x = name[cursor]
        f = cursor
        b = cursor
        cnt = 0  # 좌우 이동 거리 확인
        while name[f] != 'A' or name[b] != 'A':
            f -= 1
            b += 1
            # 인덱스 범위 밖 조정
            if f < 0: f += len(name)
            if b >= len(name): b -= len(name)
            cnt += 1
        
        if name[f] == name[b]:  # A까지의 거리가 동일한 경우
            cursor += cnt
        elif name[f] != 'A':  # 앞쪽이 더 가까운 경우
            cursor -= cnt
        elif name[b] != 'A':  # 뒤쪽이 더 가까운 경우
            cursor += cnt
        
        # 인덱스 범위 밖 조정
        if cursor < 0: cursor += len(name)
        if cursor >= len(name): cursor -= len(name)
        
        # 좌우 이동 횟수 반영
        res += cnt
        
        # x -> A 필요한 횟수
        col = ord(x) - ord('A')
        if col > 13:  # up보다 down이 가까운지 확인
            col = 26 - col
        res += col
        
        # x -> A 로 교체
        name[cursor] = 'A'

    return res


x = solution('JAN')
print(x)