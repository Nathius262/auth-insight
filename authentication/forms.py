from django import forms
from allauth.account.forms import SignupForm
from .models import CustomUser


class RegistrationForm(SignupForm):
    # first_name = forms.CharField(max_length=60, label="First Name", widget=forms.TextInput(attrs={'placeholder':'First_Name'}))
    # last_name = forms.CharField(max_length=60, label="Last Name", widget=forms.TextInput(attrs={'placeholder':'Last_Name'}))

    class Meta:
        model = CustomUser
        fields = ("email", "username", "first_name", "last_name", "password1", "password2")

    def clean_username(self):
        username = self.cleaned_data['username']
        user = CustomUser.objects.all().filter(username=username)
        if user.exists():
            raise forms.ValidationError('username "%s" is already in use.' % username)
        return username

    def save(self, request):
        user = super(RegistrationForm, self).save(request)
        return user
