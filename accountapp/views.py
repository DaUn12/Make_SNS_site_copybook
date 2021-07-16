from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView

from accountapp.models import NewModel


def hello_world(request):
    #request 함수에 method 라는 저장공간이 있음
    if request.method == 'POST':
        temp = request.POST.get('input_text')
        #  요청정보가 request 로 들어가므로 // input_text 를 불러옴

        new_model =NewModel()         # 변수에 정의한 클래스를 가져옴
        new_model.text = temp
        new_model.save()            # DB에 저장

        # data_list = NewModel.objects.all()
        # 뉴모델 안에있는 모든 값들이 data_list 에 저장됨

        return  HttpResponseRedirect(reverse('accountapp:hello_world'))
                #  이 주소로 가라


# return  render(request,'accountapp/hello_world.html'
#                ,context={'new_modeltext':temp })     # 텍스트 창에서 입력한 글자가 바로 밑에 출력이 가능하도록 함
     # HttpResponse 라는 객체를 반환    // 여기에 출력
     # 붉은색 표시일때 alt+enter 눌러서 from.... 누르면 import 할 필요 x


    else:
        data_list = NewModel.objects.all()
        # 뉴모델 안에있는 모든 값들이 data_list 에 저장됨
        return render(request, 'accountapp/hello_world.html'
                      , context={'data_list': data_list})





# 클래스 선언
# 회원가입 로직 만들기
class AccountCreateView(CreateView):            # 장고의 create 를 사용함
    model = User         # 계정을 받는거는 특별한 작업이이때문에 장고가 기본적으로 제공해주는 user을 사용
    form_class = UserCreationForm
    # 일반적으로 제공하는sign up 화면폼이라 생각하자

    success_url =  reverse_lazy('accountapp:hello_world')
    # 회원가입이 성공시 가야하는 url
    #( 함수에서 불러오는 방식 = reverse // 클래스에서 불러오는 방식 = reverse_lazy)
    # 클래스에서 리버스 쓸때는 에러가 생김
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):    # 장고의 디테일 뷰를 상속받는 클래스를 생성
    model = User
    context_object_name = 'target_user'     # 상세 계정을 뽑아낼 변수를 추출
    template_name = 'accountapp/detail.html' # 상세정보를 할때 어떤 걸로 랜더링할지




