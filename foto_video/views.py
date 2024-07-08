from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import mixins
from rest_framework.decorators import action
from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet

from foto_video.models import Video, Foto
from foto_video.controller.module import update_request_data_by_file_param, VideoCamera, \
    gen
from foto_video.pagination import CustomPagination
from foto_video.serializer import VideoSerializer, FotoSerializer

from django.views.decorators import gzip
from django.http import StreamingHttpResponse

from foto_video.controller.web_cam.video import video


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

    @action(detail=False, methods=['get'])
    def web_cam(self, request, pk=None):
        return render(request, 'home.html')

    @action(detail=False, methods=['get'])
    def display(self, request):
        return video(request)


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


@gzip.gzip_page
def detectme(request):
    try:
        cam = VideoCamera()
        return StreamingHttpResponse(
            gen(cam),
            content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass
