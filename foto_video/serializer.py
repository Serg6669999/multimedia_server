from rest_framework import serializers

from foto_video.models import Video, Foto


class VideoSerializer(serializers.ModelSerializer):
    file = serializers.FileField(allow_empty_file=True)

    class Meta:
        model = Video
        fields = '__all__'


class FotoSerializer(serializers.ModelSerializer):
    file = serializers.FileField(allow_empty_file=True)

    class Meta:
        model = Foto
        fields = '__all__'
