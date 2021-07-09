from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from accountapp.models import NewModel


def hello_world(request):
    #request 함수에 method 라는 저장공간이 있음
    if request.method == 'POST':
        temp = request.POST.get('input_text')
        #  요청정보가 request 로 들어가므로 // input_text 를 불러옴

        new_model =NewModel()         # 변수에 정의한 클래스를 가져옴
        new_model.text = temp
        new_model.save()            # DB에 저장

        return  render(request,'accountapp/hello_world.html'
                       ,context={'new_model':new_model })


# return  render(request,'accountapp/hello_world.html'
#                ,context={'new_modeltext':temp })     # 텍스트 창에서 입력한 글자가 바로 밑에 출력이 가능하도록 함
     # HttpResponse 라는 객체를 반환    // 여기에 출력
     # 붉은색 표시일때 alt+enter 눌러서 from.... 누르면 import 할 필요 x


    else:
        return render(request, 'accountapp/hello_world.html',context={'text': 'GET METHOD!'})







