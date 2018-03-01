from django import forms
from kanap.models import mod1


class mod1Form(forms.ModelForm):
	class Meta:
		model= mod1
		fields=["name","age","date"]