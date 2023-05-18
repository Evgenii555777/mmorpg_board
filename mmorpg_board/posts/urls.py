from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/create_comment/', views.create_comment, name='create_comment'),
    path('post/new/', views.new_post, name='new_post'),
    path('private-page/', views.private_page, name='private_page'),
    path('comment/delete/<int:pk>/', views.delete_comment, name='delete_comment'),
    path('comment/accept/<int:pk>/', views.accept_comment, name='accept_comment'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
