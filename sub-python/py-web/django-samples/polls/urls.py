from django.urls import path

from . import views

# 给 url 添加命名空间
app_name = 'polls'
urlpatterns = [
  path('', views.index, name='index'),
  path('<int:question_id>/', views.details, name='detail'),
  path('<int:question_id>/results', views.results, name='results'),
  path('<int:question_id>/vote/', views.vote, name='vote'),
]