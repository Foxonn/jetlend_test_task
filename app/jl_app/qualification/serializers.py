from .models import Passport, Qualification, PassportImage
from rest_framework import serializers


class CurrentUserPassportDefault:
    requires_context = True

    def __call__(self, serializer_field):
        passport = Passport.objects.get(
            user=serializer_field.context['request'].user
        )

        return passport

    def __repr__(self):
        return '%s()' % self.__class__.__name__


class QualificationInitSerializer(serializers.ModelSerializer):
    """Инициализаця квалификации"""

    class Meta:
        model = Qualification
        fields = ['user']


class QualificationStatusSerializer(serializers.ModelSerializer):
    """Статус подтверждения квалификации"""

    class Meta:
        model = Qualification
        fields = ['status']


class QualificationIsConfirmRulesSerializer(serializers.ModelSerializer):
    """Подтверждение присоединения к правилам"""

    class Meta:
        model = Qualification
        fields = ['confirm_rules']


class QualificationCreatePassportSerializer(serializers.ModelSerializer):
    """Загрузка паспортных данных"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Passport
        fields = '__all__'


class QualificationPassportImageSerializer(serializers.ModelSerializer):
    """Загрузка фотографии паспорта"""

    passport = serializers.HiddenField(default=CurrentUserPassportDefault())

    class Meta:
        model = PassportImage
        fields = '__all__'


class QualificationUploadDocumentQualificationSerializer(serializers.ModelSerializer):
    """Документ квалификации"""

    class Meta:
        model = Qualification
        fields = ['document']
