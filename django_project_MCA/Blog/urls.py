from django.urls import path, include
from .views import PostListView, PostDetailView, about  # Import all views you need

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),  # Home page showing posts
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),  # Detail view for each post
    path('about/', about, name='blog-about'),  # About page
    path('register/', include('Register.urls')),  # Include Register app URLs
]
