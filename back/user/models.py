from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group


class Hobby(models.Model):
    name = models.TextField(unique=True)

    def __str__(self):
        return self.name


class CustomUser(AbstractUser):
    # date_of_birth = models.DateField(blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True)
    pass


class Account(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.TextField(max_length=200)
    password = models.TextField(default="12345")

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккаунты'


class Survey(models.Model):
    id = models.AutoField(primary_key=True)
    form = models.ForeignKey('Form', on_delete=models.CASCADE)
    respondent = models.ForeignKey('Respondent', on_delete=models.CASCADE)
    result = models.JSONField()
    creation_time = models.TimeField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'


class Form(models.Model):
    id = models.AutoField(primary_key=True)
    questioner = models.ForeignKey('Questioner', on_delete=models.CASCADE)
    resources = models.TextField()
    body = models.JSONField()
    description = models.TextField()
    reward = models.FloatField()
    start_date = models.DateTimeField()
    expiration_date = models.DateTimeField()
    creation_date = models.DateField()
    last_updated = models.DateField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'


class Respondent(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
    avatar_url = models.TextField()
    first_name = models.TextField()
    second_name = models.TextField()
    patronymic = models.TextField()
    gender = models.TextField()
    birthday = models.DateField()
    hobbies = models.ManyToManyField(Hobby)
    EDUCATION_LEVEL_CHOICES = [
        ('B', 'Bachelor'),
        ('M', 'Master'),
        ('P', 'PhD'),
    ]
    education_level = models.CharField(max_length=1, choices=EDUCATION_LEVEL_CHOICES)
    about_me = models.TextField()
    balance = models.FloatField()
    creation_time = models.DateField()
    last_updated = models.DateTimeField()

    def __str__(self):
        return f"{self.first_name} {self.second_name}"

    class Meta:
        verbose_name = 'Ответчик'
        verbose_name_plural = 'Ответчики'


class Questioner(models.Model):
    id = models.AutoField(primary_key=True,)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, null=True)
    image_url = models.TextField()
    name = models.TextField()
    description = models.TextField()
    address = models.TextField()
    telephone = models.TextField(max_length=200)
    site = models.TextField()
    balance = models.FloatField()

    def __str__(self):
        return self.id

    class Meta:
        verbose_name = 'Опросник'
        verbose_name_plural = 'Опросники'
