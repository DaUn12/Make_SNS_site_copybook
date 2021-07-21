# func : 함수
def decorator(func):
    def decorated(input_text):          # 여기서 받는 것은 쓰고자 하는 함수안의 변수
     print('함수 시작')
     func(input_text)                  # 받은 함수를 호출
     print('함수 끝')

    return decorated    # 함수 그 자체를 되돌려줌 (호출 x )

@decorator          # 적용하고자 하는 데코레이터 넣음
def hello_world(input_text):

    print(input_text)



hello_world('hello world')




