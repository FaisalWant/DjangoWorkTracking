from django import forms
from django.utils.safestring import mark_safe


class CustomSignUpForm(forms.Form):
	check= forms.BooleanField(required=True, 
		label_suffix="", 
		label=mark_safe("<span class='ml-2'>I accept terms</span> of <a href=http://somerandomlink.com  class ='text-blue-400 hover:text-blue-800'>privacy policy</a>")
		)
		# help_text=mark_safe("<span class='ml-2'>I accept terms</span> of <a href=http://somerandomlink.com  class ='text-blue-400 hover:text-blue-800'>privacy policy</a>"))
	

	field_order=['username', 'email','password1', 'password2', 'check']

	def signup(self, request, user):
		user.check=self.cleaned_data.get('check')
		user.save()
		return user