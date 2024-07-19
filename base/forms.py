from django import forms
from django.forms import ModelForm
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Post,Profile

class PostForm(ModelForm):

	class Meta:
		model = Post
		fields = '__all__'

		widgets = {
			'tags':forms.CheckboxSelectMultiple(),
		}
