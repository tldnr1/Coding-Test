# 리스트 차집합 만들기
a = [1, 2, 3, 4, 5]
b = [2, 4]
a_sub_b = [x for x in a if x not in b]