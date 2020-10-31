from django.db import models
from django.contrib.auth.models import User


def passport_directory_path(instance, filename):
    f_path = 'uploads/passport/user_{id}/{f_name}'.format(
        id=instance.passport.user.id,
        f_name=filename
    )

    return f_path


def qualification_directory_path(instance, filename):
    f_path = 'uploads/qualification/user_{id}/{f_name}'.format(
        id=instance.user.id,
        f_name=filename
    )

    return f_path


class Passport(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="passport",
        verbose_name="Пользователь"
    )

    first_name = models.CharField(
        max_length=25,
        null=False,
        verbose_name="Имя"
    )

    last_name = models.CharField(
        max_length=25,
        null=False,
        verbose_name="Фамилия"
    )

    middle_name = models.CharField(
        max_length=25,
        null=False,
        verbose_name="Отчество"
    )

    serial_number = models.IntegerField(
        null=False,
        unique=True,
        verbose_name="Серийный номер"
    )

    date_birth = models.DateField(
        null=False,
        verbose_name="Дата рождения"
    )

    place_birth = models.CharField(
        max_length=125,
        verbose_name="Место рождения"
    )

    date_issue = models.DateField(
        null=False,
        verbose_name="Дата выдачи"
    )

    issued_by = models.CharField(
        max_length=75,
        null=False,
        verbose_name="Кем выдан"
    )

    registration_address = models.CharField(
        max_length=75,
        null=False,
        verbose_name="Адрес регистрации"
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Паспорт'
        verbose_name_plural = 'Паспорта'
        ordering = ['first_name']


class PassportImage(models.Model):
    passport = models.ForeignKey(
        Passport,
        on_delete=models.CASCADE,
        related_name='passport_image'
    )

    images = models.ImageField(
        upload_to=passport_directory_path,
        verbose_name="Фотография"
    )

    def __str__(self):
        return self.passport.user.username

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class Qualification(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="qualification",
        verbose_name="Пользователь"
    )

    status = models.BooleanField(
        default=False,
        verbose_name="Статус подтверждения квалификации"
    )

    confirm_rules = models.BooleanField(
        default=False,
        verbose_name="Подтверждение присоединения к правилам"
    )

    document = models.FileField(
        upload_to=qualification_directory_path,
        null=True,
        verbose_name="Документ о квалификации"
    )

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Квалификация'
        verbose_name_plural = 'Квалификации'
