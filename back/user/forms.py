from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from .models import Account, Respondent, Questioner, Form, Survey, Hobby
from django import forms


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password')  # Добавьте дополнительные поля, если необходимо


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomUser


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


class RespondentForm(forms.ModelForm):
    class Meta:
        model = Respondent
        fields = '__all__'


class QuestionerForm(forms.ModelForm):
    class Meta:
        model = Questioner
        fields = '__all__'


class FormForm(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'


class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = '__all__'


class HobbyForm(forms.ModelForm):
    class Meta:
        model = Hobby
        fields = '__all__'
