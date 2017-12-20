from django import forms 
from django.core import validators
from app2.models import User

# def check_for_z(value):
# 	if value[0].lower() != 'z':
# 		raise forms.ValidationError('nama membutuhkan dimulai dengan Z')
class UserBaruForm(forms.ModelForm):
	class Meta():
		model = User
		fields = '__all__'

class FormName(forms.Form):
	# name = forms.CharField(validators=[check_for_z])
	name = forms.CharField()
	email = forms.EmailField()
	verify_email = forms.EmailField(label='masukkan email anda lagi:')
	text = forms.CharField(widget=forms.Textarea)

	# botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)]) #membuat input hidden untuk security

	def clean(self):
		print('coba', self)
		# all_clean_data = super().clean()
		all_clean_data = super(FormName, self).clean() #django 1.8
		email = all_clean_data.get('email')
		vmail = all_clean_data.get('verify_email')

		if email != vmail :
			raise forms.ValidationError('email tidak sama')

	#ga harus pake ini pake aja django.core import validators
	# def clean_botcatcher(self):
	# 	botcatcher = self.cleaned_data['botcatcher']
	# 	if len(botcatcher) > 0:
	# 		raise forms.ValidationError("BOT tertangkap")
	# 	return botcatcher
	#cara ceknya input lalu tambahkan value='test' di input hiddennyanya lalu submit


