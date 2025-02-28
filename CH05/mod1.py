# 함수 선언 : 네임스페이스 등록 -> 실행된다.
def sum_(a, b):
    return a + b

def safe_sum(a,b):
    if type(a) != type(b):
        print('타입이 동일하지 않다')
        return None
    else : # 타입 동일 경우
        result = sum_(a,b)
        return result

# 위 함수들을 테스트 코드
# 주의사항 : mod2에 mod1을 import하게되면 아래의 테스트 코드가 mod2 실행할때 같이 실행되버린다.
# print(sum_(1,6))    
# print(safe_sum(1,'a'))

# mod1을 단독 실행할 떄는 main 작동한다.
#__name__ : 어떻게 실행한 것인지를 저장 변수
#__name__ = '__main__' 이 대입된다.

# mod1이 단독 실행될 때만 테스트 코드 실행되게 하고 싶다.
# import 했을 때는 아래의 테스트 코드가 실행이 안된다.
if __name__ == '__main__':
    print(sum_(1,6))    
    print(safe_sum(1,'a'))
