"""goHome URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),        # 장고가 기본적으로 준 주소 (관리자 페이지)
    path('accounts/', include('accountapp.urls')),         #path = 장고에서 제공하는 기능 , 경로를 accounts
    path('profiles/', include('profileapp.urls')),
    # profiles 로가는 겨올를 설정
    path('articles/', include('articleapp.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT )
# 이미지 모양을 되기 위해 media 에 static 을 가져옴
# 경로로 왔을 때, 미디어를 제공
