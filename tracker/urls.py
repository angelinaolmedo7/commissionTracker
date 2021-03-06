from django.urls import path
from . import views

app_name = 'tracker'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:commission_id>/', views.detail, name='commission detail'),
    path('archive/<int:archivedCommission_id>/', views.archived_detail, name='archived commission detail'),
    path('archive/<int:archivedCommission_id>/like/', views.like, name='like'),
]
