from django.urls import path
from blog.views.post_view import PostView, PostDetail

urlpatterns = [
    path('', PostView.as_view(), name='home'),
    path('<slug:slug>/', PostDetail.as_view(), name='post_detail'),
]
