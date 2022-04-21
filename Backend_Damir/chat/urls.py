from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views
app_name = 'chat'


urlpatterns = (

    path('load_chats/',views.load_chats),
    path('start_chat/',views.create_chat),

)
