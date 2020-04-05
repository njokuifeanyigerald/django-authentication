from django import forms
from django.contrib.auth import authenticate,get_user_model


User = get_user_model()

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('this user does not exist')
            if not user.check_password(password):
                raise  forms.ValidationError('incorrect password')
            if not user.is_active:
                raise  forms.ValidationError('this user is not active')
        return super(LoginForm, self).clean(*args, **kwargs)

class RegisterForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(label="email address")
    password = forms.CharField(widget=forms.PasswordInput, label="password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="confirm password")

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'password2'
        ]

    def clean_register(self, *args, **kwargs):
        username = self.cleaned_data.get('username')
        email = self.cleaned_data.get('email')
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError('passwords must match')

        email_qs = User.objects.filter(email=email)
        username_qs = User.objects.filter(username=username)

        if email_qs.exists():
            raise forms.ValidationError('email has already been used')
        return email       
        if username_qs.exists():
                raise forms.ValidationError('username has already been used ') 