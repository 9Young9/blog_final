from django.urls import path,include    # include는 뭐지?
from . import views  # 여기에 있는 views를 가져온다.


urlpatterns = [
   path('login/', views.login_view, name="login"),    # url을 지정해준다. 뒤에 "/" 꼭 붙이기! name은 중요해! 겹치면 안된다.
   path('logout/', views.logout_view, name="logout"), # views.py에 있는 logout_view 함수랑 연결된다.
   path('register/', views.register_view, name="register"), # login, logout, register
]