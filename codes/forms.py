from django import forms
from .models import Code
class CodeForm(forms.ModelForm):
    number = forms.CharField(label='Code', help_text='Tasdiqlash kodini kiriting...')
    class Meta:
        model = Code
        fields = ['number']