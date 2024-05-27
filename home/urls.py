from django.urls import path
from .views import homeView, rootView, startpageView

urlpatterns = [
    path('', rootView, name='root'),
    path('start/', startpageView, name='start'),
    path('home/', homeView, name='home'),
    path('index/', homeView, name='home')
]
