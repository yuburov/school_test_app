from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from main import settings
from .models import Student

@receiver(post_save, sender=Student)
def send_student_notification(sender, instance, created, **kwargs):
    if created:
        # Отправка уведомления по электронной почте
        subject = 'Новый ученик зарегистрирован'
        message = f'Привет, {instance.full_name}! Вы успешно зарегистрированы.'
        recipient_list = [instance.mail]
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)