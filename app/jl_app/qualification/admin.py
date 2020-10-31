from django.contrib import admin
from .models import Qualification, Passport, PassportImage


# Register your models here.

class PassportImageAdmin(admin.TabularInline):
    model = PassportImage


@admin.register(Qualification)
class QualificationAdmin(admin.ModelAdmin):
    class Meta:
        fields = '__all__'


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    inlines = [
        PassportImageAdmin,
    ]

    class Meta:
        fields = '__all__'
