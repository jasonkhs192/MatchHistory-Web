from django import forms

class TestForm(forms.Form):
    summoner_name = forms.CharField()
    match_number = forms.IntegerField()