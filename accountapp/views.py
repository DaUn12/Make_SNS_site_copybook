from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    return HttpResponse('Hello World!')     # HttpResponse 라는 객체를 반환    // 여기에 출력
                                            # 붉은색 표시일때 alt+enter 눌러서 from.... 누르면 import 할 필요 x







