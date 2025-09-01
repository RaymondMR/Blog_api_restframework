#posts/urls.py
from django.urls import path
from .views import PostListCreateView, PostRetrieveUpdateDestroyView


urlpatterns = [
    path('posts/<int:pk>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
]