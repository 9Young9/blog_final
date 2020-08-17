from django.contrib import admin
from django.urls import path,include
import blog.views   # blog 앱에 있는 views 파일을 가져온다.
import blog.urls
import account.urls # import account.views는 필요 없는걸까? account 앱에 있는 views 파일도 필요하잖아!
# 아래는 미디어 할 때 쓰는 것들
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.list, name = "list"),
    path('blog/<int:blog_id>', blog.views.detail, name = "detail"), # int -> 객체 번호가 따로 주어진다
    path('blog/new', blog.views.new, name = "new"),
    path('blog/create',blog.views.create, name = "create"),
    path('blog/edit/<int:blog_id>', blog.views.edit, name = "edit"),
    path('blog/update/<int:blog_id>', blog.views.update, name = "update"),
    path('blog/delete/<int:blog_id>', blog.views.delete, name = "delete"),
    path('account/', include(account.urls)),    # 이렇게 짧게 하는 건 앞에서 배운 걸까? 무슨 뜻이지
    path('blog/commenting/<int:blog_id>', blog.views.commenting, name = "commenting"),
    path('blog/like/<int:blog_id>', blog.views.like, name="like"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# python manage.py createsuperuser -> admin 페이지 계정 생성