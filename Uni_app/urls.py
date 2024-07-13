from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<hist_id>/', views.hist, name='hist')
]
