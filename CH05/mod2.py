# ctrl + f5 debug run

# import mod1

# print(mod1.safe_sum(3,'a'))
# print(mod1.safe_sum(3,4))
# print(mod1.safe_sum('a','b'))

# 함수를 직접 import 처리
# import 할때 () 붙이지않는다 이름만 기입
# from mod1 import * => mod1에서 있는 모든걸 다 가져와라. 메모리 낭비가 될수있으니 적절하게 사용해야된다.
from mod1 import safe_sum #,sum_ 해서 추가로 import한다.

# # print(safe_sum(3,'a'))
# print(safe_sum(3,4))
# print(safe_sum('a','b'))
# # print(sum_(3,8)) sum_ import 안해서 에러다 에러내지않으려면