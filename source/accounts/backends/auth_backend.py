from django.contrib.auth.backends import ModelBackend
from webapp.models import Teacher


class PhoneNumberBackend(ModelBackend):
    def authenticate(self, request, tel_number=None, password=None, **kwargs):
        try:
            user = Teacher.objects.get(tel_number=tel_number)
            if user.check_password(password):
                return user
        except Teacher.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Teacher.objects.get(pk=user_id)
        except Teacher.DoesNotExist:
            return None
