from django.contrib import admin

from webapp.models import Teacher, School, Grade, Student

admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Grade)


