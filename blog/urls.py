from django.contrib import admin
from django.urls import path
# from . import views   # 현재 경로에 있는 views 파일을 가져온다.
import blog.views   

urlpatterns = [
    path('<int:blog_id>', blog.views.detail, name = "detail"), # int -> 객체 번호가 따로 주어진다
    path('new', blog.views.new, name = "new"),
    path('create',blog.views.create, name = "create"),
    path('edit/<int:blog_id>', blog.views.edit, name = "edit"),
    path('update/<int:blog_id>',blog.views.update, name = "update"),
    path('delete/<int:blog_id>', blog.views.delete, name = "delete"),
]