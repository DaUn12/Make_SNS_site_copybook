from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile



@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class ProfileCreateView(CreateView):

    model = Profile
# 어떤모델을 만들 것인지
    form_class = ProfileCreationForm
# 어떤 폼을 사용할 것인지
    success_url = reverse_lazy('accountapp:hello_world')
# 어디로 되돌아 갈것인지
    template_name = 'profileapp/create.html'
#  어떤 html 파일로 만들것인지

# 오버라이드 하기
    def form_valid(self, form):
#form_valid : 인증과정을 다하고 나서 검증 완료시 실행되는 함수
        form.instance.user = self.request.user
         # user 식별후 form 안에 있는 user로  할당

        return super().form_valid(form)
        # 부모에있는 form_valid 를 오버라이드 함

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileCreationForm
    context_object_name ='target_profile'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'








