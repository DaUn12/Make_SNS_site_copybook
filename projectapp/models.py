from django.db import models

# Create your models here.


class Project(models.Model):
    name = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=200, null=False, blank=True)
    image = models.ImageField(upload_to='project/', null=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'
        # migration 을 안해줘도 됨
        # migration -> 모델에서 반영한 것에 DB에도 반영하게끔하려한 것
        # str 은 파이썬 내부에서 사용하는 방식이기 때문에 안해도 됨