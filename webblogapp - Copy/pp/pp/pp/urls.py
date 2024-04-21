from django.contrib import admin
from django.urls import path
from blogpp import views  # Импорт views из вашего приложения
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.signup, name='signup'),  # Использование views.signup вместо signup
    path('login/', views.user_login, name='login'),  # Использование views.user_login вместо user_login
    path('post_list/', views.post_list, name='post_list'),  # Использование views.post_list вместо post_list
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Использование views.post_detail вместо post_detail
    path('admin/', admin.site.urls),
    path('chat/', views.chat_room, name='chat_room'),  # Использование views.chat_room вместо chat_room
    path('post/<int:pk>/like/', views.like_post, name='like_post'),  # Использование views.like_post вместо like_post
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),  # Использование views.add_comment_to_post вместо add_comment_to_post
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
