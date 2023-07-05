from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from webapp.models import Teacher


class TeacherRegisterForm(UserCreationForm):
    school = forms.CharField(max_length=100, label='Название школы')
    grade = forms.CharField(max_length=50, label='Название класса')

    class Meta(UserCreationForm.Meta):
        model = Teacher
        fields = ['tel_number', 'grade', 'subject', 'school']


class TeacherAuthorizationForm(AuthenticationForm):
    tel_number = forms.CharField(label='Номер телефона', max_length=30)
    username = forms.CharField(label='Имя', required=False)

    class Meta:
        model = Teacher
        fields = ['tel_number', 'password']

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        super().__init__(*args, **kwargs)

    def clean(self):
        tel_number = self.cleaned_data.get('tel_number')
        password = self.cleaned_data.get('password')
        if tel_number and password:
            self.user_cache = authenticate(request=self.request, tel_number=tel_number, password=password)
            if self.user_cache is None:
                raise forms.ValidationError('Неверный номер телефона или пароль.')

        return self.cleaned_data

    def get_user(self):
        return self.user_cache if hasattr(self, 'user_cache') else None
