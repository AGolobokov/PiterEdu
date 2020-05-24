from django import forms
from rooms.models import Rooms


class RoomForm(forms.ModelForm):
    #room = forms.ModelChoiceField(queryset=Rooms.objects.all(), widget=forms.HiddenInput)
    class Meta:
        model = Rooms
        fields = ('name', 'description', 'address', 'phone', 'photo', 'contacts')
