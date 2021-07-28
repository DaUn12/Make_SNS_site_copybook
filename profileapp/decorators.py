
# func : 함수
from django.http import HttpResponseForbidden

from profileapp.models import Profile


def profile_ownership_required(func):
    def decorated(request, *args, **kwargs):
        target_profile = Profile.objects.get(pk=kwargs['pk'])      # 클래스안에있는 변수를 하나만(get) 가져옴
        # objects 는 딕셔너리
        if target_profile.user == request.user:
            return func(request, *args, **kwargs)

        else:
            return HttpResponseForbidden()
            # 로그인이 아닐때 들어가려한다면 '액새스가 거부되도록 함'

    return decorated



