from django import forms


class ChatMessageForm(forms.Form):
    text = forms.CharField()
