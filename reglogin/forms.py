from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile


# Create your forms here.
genderChoices = [('F','Female'), ('M','Male')]
class NewUserForm(UserCreationForm):
	# contact = forms.IntegerField()
	# hobby = [('music','Music'),('art','Art'),('dance','Dance'),('singing','Singing'),('reading','Reading')]
	# hobby = forms.MultipleChoiceField(required=False, widget=forms.CheckboxSelectMultiple, choices=hobby)
	# genderOption = [('female','Female'), ('male','Male')]
	# gender = forms.CharField(label='gender', widget= forms.RadioSelect(choices=genderOption))

	class Meta:
		model = User
		fields = ("username", "email")


class ProfileUpdateForm(forms.ModelForm):
	gender = forms.ChoiceField(choices=genderChoices, widget=forms.RadioSelect())


	class Meta:
		model = Profile
		fields = ['contact', 'gender']