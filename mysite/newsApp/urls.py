from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:headline_id>', views.detail, name='detail'),
    path('<int:headline_id>/results/', views.results, name='results'),
    path('<int:headline_id>/vote/', views.vote, name='vote'),
]