from django import forms
from rooms.models import Rooms


class RoomForm(forms.ModelForm):
    class Meta:
        model = Rooms
        fields = ('name', 'description', 'address', 'phone', 'photo', 'contacts')
