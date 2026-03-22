from django import forms
from .models import GLBModel

class GLBUploadForm(forms.ModelForm):
    class Meta:
        model = GLBModel
        fields = ['name', 'file']