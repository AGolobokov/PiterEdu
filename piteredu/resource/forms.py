from django import forms
from resource.models import Resource


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ('name', 'description','photo', 'contacts')