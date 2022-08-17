from django.urls import path

from apps.blog.views import CategoryViewSet, BlogListView, BlogItemView, BlogCreatView, BlogCommentsView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    path('blog/create/', BlogCreatView.as_view(), name='blog_create'),
    path('blog/comments/', BlogCommentsView.as_view(), name='blog_comments'),
]
