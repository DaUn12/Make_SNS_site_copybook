from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView

from django.contrib.auth.views import LoginView, LogoutView

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),       #hello world 의 경로

    path('login/', LoginView.as_view(template_name= 'accountapp/login.html'),
         name= 'login'  ),
    #path (어떤주소로 들어올건지, 함수(클래스시: 클래스이름.as_view), 우리가 쓸 라우트의 이름)

    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', AccountCreateView.as_view(), name = 'create'),
    #path ( 파일 이름, 함수(클래스시: 클래스이름.as_view), 우리가 쓸 이름을 설정)
    # 어떤 url 로 가야 회원가입 로직으로 가는지


    # detailView 만든 후 라우팅
    path('detail/<int:pk>', AccountDetailView.as_view(), name = 'detail' ),
    # 어떤주소로 접글할때 로직을 실행할건지 / 로직  / 라우트의 이름
    # int : pk  = 인티저 형태를 받는데 이름은 pk 이다

    path('update/<int:pk>', AccountUpdateView.as_view(), name ='update'),
    # 어떤주소로 접근할지 / 로직 / 라우트의 이름


]
# 앱 네임이 accountapp 인걸로 가서 url이 hello_world 로 가라


