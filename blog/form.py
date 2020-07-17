# form은 장고로부터 기본적으로 제공받는 기능

from django import forms
from .models import Blog    # model에 있는 Blog를 기반으로 정보를 받아오니까 import 해준다.

class BlogForm(forms.ModelForm):
    class Meta: #meta class를 지정해준다.
        model = Blog    # model은 Blog를 기반으로 만들 것이다
        fields = ['title', 'body', 'image']  # 원하는 값