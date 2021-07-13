from django.urls import path

from accountapp.views import hello_world

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),       #hello world 의 경로


    path('create/', AccountCreateView.as_view(),name = 'create')
    #path ( 파일 이름, 함수(클래스시: 클래스이름.as_view), 우리가 쓸 이름을 설정)

]
# 앱 네임이 accountapp 인걸로 가서 url이 hello_world 로 가라


# 어떤 url 로 가야 회원가입 로직으로 가는지