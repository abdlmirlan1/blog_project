from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogCreateView, name='post_new'),
    path('', BlogListView.as_view(), name='home'),
    path('detail/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),
]