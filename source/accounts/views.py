from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from accounts.forms import TeacherRegisterForm, TeacherAuthorizationForm
from webapp.models import Grade, School


class SignUpUserView(CreateView):
    form_class = TeacherRegisterForm
    template_name = 'account/user_sign_up.html'
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        # Получение значений из полей ввода
        school_name = form.cleaned_data['school']
        grade_name = form.cleaned_data['grade']

        # Создание учителя
        teacher = form.save()
        # Получение или создание школы
        school, _ = School.objects.get_or_create(name=school_name)
        # Создание класса
        Grade.objects.create(name=grade_name, teacher=teacher, school=school)

        return super().form_valid(form)


class UserLoginView(LoginView):
    template_name = 'account/login.html'
    authentication_form = TeacherAuthorizationForm
    redirect_authenticated_user = True

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class UserLogoutView(LogoutView):
    next_page = 'webapp:index'
