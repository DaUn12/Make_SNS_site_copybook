from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    #request 함수에 method 라는 저장공간이 있음
    if request.method == 'POST':
        return  render(request,'accountapp/hello_world.html'
                       ,context={'text':'POST METHOD!'})
     # HttpResponse 라는 객체를 반환    // 여기에 출력
     # 붉은색 표시일때 alt+enter 눌러서 from.... 누르면 import 할 필요 x


    else:
        return render(request, 'accountapp/hello_world.html',context={'text': 'GET METHOD!'})







