from django import forms
from django.forms import Select,Textarea,TextInput
from .models import Room

BLOCKS= [
    ('GH5', 'GH5'),
    ('GH4', 'GH4'),
    ('GH3', 'GH3'),
    ('GH1', 'GH1'),
    ]

FLOORS= [
    (0,'Ground'),
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    ]

class BlockForm(forms.Form):
    block= forms.CharField(
        label='Block',
        widget=forms.Select(choices=BLOCKS)
    )

class FloorForm(forms.Form):
    floor= forms.IntegerField(
        label='Floor',
        widget=forms.Select(choices=FLOORS)
    )
class RoomForm(forms.Form):
    room_no = forms.IntegerField()