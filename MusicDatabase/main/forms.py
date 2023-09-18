from .models import Tracks
from django.forms import ModelForm, Select, TextInput, CheckboxInput

class TracksForm(ModelForm):
    class Meta():
        model = Tracks
        fields = '__all__'

        widgets = {
            "title": Select(attrs={
                'class': "form-select",
                'id': "title"
            }),
            "artist": Select(attrs={
                'class': "form-select",
                'id': "artist"
            }),
            "album": Select(attrs={
                'class': "form-select",
                'id': "album"
            }),
            "track_number": TextInput(attrs={
                'type': "number",
                'class': "form-control",
                'id': "track_number",
                'placeholder': "1"
            }),
            "tempo": TextInput(attrs={
                'type': "number",
                'class': "form-control",
                'id': "tempo",
                'placeholder': "120"
            }),
            "duration": TextInput(attrs={
                'type': "number",
                'class': "form-control",
                'id': "duration",
                'placeholder': "180"
            }),
            "isrc_code": TextInput(attrs={
                'type': "text",
                'class': "form-control",
                'id': "isrc_code",
                'placeholder': "XXXX00000000",
                'maxlength': "12"
            }),
            "explict": CheckboxInput(attrs={
                'class': "form-check-input",
                'id': "explict"
            })
        }