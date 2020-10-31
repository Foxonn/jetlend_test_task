from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import (CreateAPIView,
                                     UpdateAPIView,
                                     RetrieveUpdateAPIView)

from django.shortcuts import get_object_or_404
from .models import Qualification, Passport, PassportImage

from .serializers import (QualificationStatusSerializer,
                          QualificationCreatePassportSerializer,
                          QualificationIsConfirmRulesSerializer,
                          QualificationInitSerializer,
                          QualificationUploadDocumentQualificationSerializer,
                          QualificationPassportImageSerializer)


class QualificationInit(CreateAPIView):
    """Инициализаця квалификации"""

    permission_classes = [IsAuthenticated]
    serializer_class = QualificationInitSerializer


class QualificationStatusView(RetrieveUpdateAPIView):
    """Получить или изменить статус подтверждения квалификации"""

    permission_classes = [IsAuthenticated]
    serializer_class = QualificationStatusSerializer
    queryset = Qualification.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)

        return obj


class AddPassportView(CreateAPIView):
    """Добавление паспорта"""

    permission_classes = [IsAuthenticated]
    serializer_class = QualificationCreatePassportSerializer
    queryset = Passport.objects.all()


class AddImagePassportView(CreateAPIView):
    """Добавление фотографии паспорта"""

    permission_classes = [IsAuthenticated]
    serializer_class = QualificationPassportImageSerializer
    queryset = PassportImage.objects.all()


class ConfirmRulesView(RetrieveUpdateAPIView):
    """Подтверждение присоединения к правилам"""

    permission_classes = [IsAuthenticated]
    serializer_class = QualificationIsConfirmRulesSerializer
    queryset = Qualification.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)

        return obj


class AddQualificationDocsView(UpdateAPIView):
    """Добавление документа квалификации"""

    permission_classes = [IsAuthenticated]
    serializer_class = QualificationUploadDocumentQualificationSerializer
    queryset = Qualification.objects.all()

    def get_object(self):
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, user=self.request.user)

        return obj
