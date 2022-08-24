def solution(n, lost, reserve):
    reserve.sort()
    _reserve = [r for r in reserve if r not in lost]  # 여벌을 잃지 않은 학생
    _lost = [l for l in lost if l not in reserve]  # 여벌이 없으나 잃은 학생

    for r in _reserve:
        f = r - 1  # 앞 번호
        b = r + 1  # 뒷 번호
        if f in _lost:  # 여벌 있는 r 기준, f가 여벌이 없다면 삭제
            _lost.remove(f)
        elif b in _lost:
            _lost.remove(b)
    return n - len(_lost)