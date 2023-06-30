from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.core.mail import send_mail
from main import settings
from .models import Student
from .forms import StudentForm, SimpleSearchForm


class StudentListView(ListView):
    model = Student
    template_name = 'student/list.html'
    context_object_name = 'students'

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['form'] = self.form
        if self.search_value:
            context['query'] = urlencode({'search': self.search_value})
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.search_value:
            query = Q(full_name__icontains=self.search_value)
            queryset = queryset.filter(query)
            return queryset
        else:
            return queryset

    def get_search_form(self):
        return SimpleSearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search']
        return None


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/create.html'
    success_url = '/'

    def form_valid(self, form):
        response = super().form_valid(form)
        send_notification_email(self.object)
        return response


class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/detail.html'
    context_object_name = 'student'


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/update.html'
    success_url = '/'


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/delete.html'
    success_url = '/'


def send_notification_email(student):
    subject = 'Добро пожаловать!'
    message = f'Здравствуйте, {student.full_name}! Вы успешно зарегистрированы в нашей школе.'
    from_email = settings.EMAIL_HOST_USER
    to_email = student.mail
    send_mail(subject, message, from_email, [to_email])
