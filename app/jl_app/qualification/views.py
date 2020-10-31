from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
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


class QualificationInit(APIView):
    """Инициализаця квалификации"""

    permission_classes = [IsAuthenticated]
    http_method_names = ['get']

    def get(self, request):
        serializer = QualificationInitSerializer(
            data={'user': request.user.id}
        )

        if serializer.is_valid():
            serializer.save()

            return Response(status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
