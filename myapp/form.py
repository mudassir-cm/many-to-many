from django import forms
from .models import Cast, Movie


class CastForm(forms.ModelForm):
    class Meta:
        model = Cast
        fields = '__all__'


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'