from django.urls import path

from chat.ajax import ChatAjax
from chat.views import ChatView

app_name = "chat"
urlpatterns = [
    # Ajax
    path("ajax/chat", ChatAjax.as_view(), name="chat-ajax"),
    # Views
    path("", ChatView.as_view(), name="chat"),
]
