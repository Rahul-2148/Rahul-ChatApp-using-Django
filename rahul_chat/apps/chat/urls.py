
from django.urls import path
from . import views

urlpatterns = [
    path('<str:username>', views.chatRoom, name='chatRoom'),
    path('get_messages/<str:username>', views.get_messages, name='get_messages'),
    path('<str:username>/send_message/', views.send_message, name='send_message'), 
    
    # path('chat/delete_message/', views.delete_message, name='delete_message'),
    # path('chat/delete_selected_messages/', views.delete_selected_messages, name='delete_selected_messages'),
    # path('chat/clear_chat/<str:username>', views.clear_chat, name='clear_chat'),
]

