from typing import Any
from typing import Dict

from django.views.generic import TemplateView
from django.views.generic.list import ListView

from chat.handlers import ChatHandler


class ChatView(TemplateView):
    template_name = "chat/chat.html"

    def get_context_data(self, *args, **kwargs):
        ctx: Dict[str, Any] = super().get_context_data(*args, **kwargs)
        ctx["messages"] = ChatHandler.get_messages_data()

        return ctx
