from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', home, name='home'),
    path('add-question/', add_question, name='add_question'),
    path('login/', login_page, name='login_user'),
    path('logout/', logout_page, name='logout_user'),
    path('register/', register_page, name='register'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
