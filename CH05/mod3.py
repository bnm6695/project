# 같은 directory (현재 ch05에 있음)에 있을때는 그냥 import해도됨
# 다른 directory일 경우 python library에 등록해서 써야됨 => modetest.ipynb 파일에 상세
import mod3_1

# PI 출력
print(mod3_1.PI)

# class => object 생성
a = mod3_1.Math()
print(a.solv(2))

# function 실행
print(mod3_1.sum(1,2))