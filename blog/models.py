# models.py에 변경사항 생기면 python manage.py makemigrations -> migrations 폴더에 변경사항 저장함
# DB에 알려주는 건 python manage.py migrate -> OK OK

from django.db import models

from django.conf import settings

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=200)    # max_length는 CharField의 필수 인자이고, 줄 길이를 200으로 제한한다는 뜻
    pub_date = models.DateTimeField()   # 인자 없어도 됨!
    body = models.TextField()   # 본문  # CharField는 TextField보다 작은 값을 담는다!(데이터 절약)
    image = models.ImageField(upload_to="blog/", blank=True, null=True) # 이미지 받는 필드  # media/blog/파일이름 -> 이렇게 저장 된다
    # pip install pillow 라는 파이썬 패키지 깔아야함(이미지 하려면!)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name = 'likers', blank=True, null=True)
    # like 기능

    def __str__(self):  # 문자열로 보여준다.
        return self.title

    def summary(self):  # body 길 때를 대비해 만들었다
        return self.body[:120]  # 120글자만 딱 나오도록

class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='comments')
    body = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.author}님이 {self.blog}에 단 댓글"