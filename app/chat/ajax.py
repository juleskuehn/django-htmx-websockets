from django.http import HttpResponse
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import CreateView
from django.views.generic import FormView
from django.views.generic import TemplateView
from django.views.generic.list import ListView

from chat.forms import ChatMessageForm
from chat.handlers import ChatHandler, ChatMessage


class ChatAjax(FormView):
    template_name = "chat/partials/chat_messages_form.html"
    http_method_names = ["post"]
    form_class = ChatMessageForm

    def form_valid(self, form):
        message: ChatMessage = ChatMessage(
            text=form.cleaned_data["text"],
        )
        ChatHandler.save_message(message=message)

        return HttpResponse(status=204)
