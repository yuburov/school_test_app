from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Teacher(AbstractUser):
    tel_number = models.CharField(max_length=20, unique=True, verbose_name='Номер телефона')
    subject = models.CharField(max_length=50, verbose_name="Название предмета")
    username = models.CharField(max_length=55, unique=False, null=True, blank=True)
    USERNAME_FIELD = 'tel_number'

    def __str__(self):
        return self.tel_number


class School(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название школы")

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название класса")
    teacher = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="grade", primary_key=True,
                                   on_delete=models.CASCADE, verbose_name='Учитель')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="grades", verbose_name='Школа')

    def __str__(self):
        return self.name


class Student(models.Model):
    GENDER_CHOICES = [
        ('male', 'Мужской'),
        ('female', 'Женский'),
    ]
    full_name = models.CharField(max_length=100, verbose_name="ФИО")
    mail = models.EmailField()
    birth_date = models.DateField(verbose_name="Дата рождения", help_text='Формат даты: ГГГГ-ММ-ДД')
    grade = models.ForeignKey(Grade, related_name="students", on_delete=models.CASCADE, verbose_name="Класс")
    address = models.CharField(max_length=100, verbose_name="Адрес")
    sex = models.CharField(max_length=10, choices=GENDER_CHOICES, default=GENDER_CHOICES[0][0], verbose_name="Пол")
    photo = models.ImageField(upload_to="photos", null=True, blank=True, verbose_name="Фото")

    def __str__(self):
        return self.full_name
