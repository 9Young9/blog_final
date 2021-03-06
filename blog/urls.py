from django.contrib import admin
from django.urls import path,include
# from . import views   # 현재 경로에 있는 views 파일을 가져온다.
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name = "detail"), # int -> 객체 번호가 따로 주어진다
    path('new', views.new, name = "new"),
    path('create',views.create, name = "create"),
    path('edit/<int:blog_id>', views.edit, name = "edit"),
    path('update/<int:blog_id>', views.update, name = "update"),
    path('delete/<int:blog_id>', views.delete, name = "delete"),
    path('commenting/<int:blog_id>', views.commenting, name='commenting'),
    path('like/<int:blog_id>', views.like, name='like'),
]