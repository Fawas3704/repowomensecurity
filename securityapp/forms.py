from django.forms import ModelForm
from .models import ComplaintTable

class Addreplyform(ModelForm):
    class Meta:
        model=ComplaintTable
        fields=['Reply']