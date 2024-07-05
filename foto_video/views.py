import pathlib
import re

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins

from rest_framework.viewsets import GenericViewSet

from foto_video.models import Video, Foto
from foto_video.module import update_request_data_by_file_param
from foto_video.pagination import CustomPagination
from foto_video.serializer import VideoSerializer, FotoSerializer


class VideoViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'date': ['gte', 'lte', 'exact', 'gt', 'lt'],
    }

    def create(self, request, *args, **kwargs):
        update_request_data_by_file_param(request)
        return mixins.CreateModelMixin.create(self, request,
                                                    *args,
                                                    **kwargs)

class FotoViewSet(mixins.CreateModelMixin,
                   mixins.ListModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.DestroyModelMixin,
                   GenericViewSet):
    queryset = Foto.objects.all()
    serializer_class = FotoSerializer
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_fields = {
        'date': ['gte', 'lte', 'exact', 'gt', 'lt'],
    }

    def create(self, request, *args, **kwargs):
        update_request_data_by_file_param(request)
        return mixins.CreateModelMixin.create(self, request,
                                                    *args,
                                                    **kwargs)
