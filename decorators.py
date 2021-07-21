# func : 함수
# def decorator(func):
#     def decorated(input_text):          # 여기서 받는 것은 쓰고자 하는 함수안의 변수
#         print('함수 시작')
#         func(input_text)                  # 받은 함수를 호출
#         print('함수 끝')
#
#     return decorated    # 함수 그 자체를 되돌려줌 (호출 x )
#
# @decorator          # 적용하고자 하는 데코레이터 넣음


def decorator(func):
    def decorated(m, h):
        print((m * h) / 2)
    return  decorated

def decorators(func):
    def decorated(m, h):
        print((m * h))
    return  decorated

@decorator
def aa(m,h):
    if m>0 and h>0:
        print()
    else:
        print('error')

@decorators
def bb(m,h):
    if m>0 and h>0:
        print()
    else:
        print('error')


aa(3, 7)
bb(4,5)
# def hello_world(input_text):
#
#     print(input_text)
#
#
#
# hello_world('hello world')

#  raise PermissionError()  : 에러 시 달아주는 문구














