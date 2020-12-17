#매핑정보 여기서 읽어서 처리
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),      #이미 pybo/로 시작되는 URL이 매핑되어 있기 때문에 그냥 ''로 시작
    path('<int:question_id>/', views.detail)
]
