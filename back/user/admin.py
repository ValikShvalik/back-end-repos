from django.contrib import admin
from .models import Respondent, Form, Survey, Account, Questioner
# Register your models here.

admin.site.register(Respondent)
admin.site.register(Survey)
admin.site.register(Account)
admin.site.register(Questioner)
admin.site.register(Form)
