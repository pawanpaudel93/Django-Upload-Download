from rest_framework import serializers
from .models import File


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ('file',)

class FileViewSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    class Meta:
        model = File
        fields = ('file',)
    
    def get_file(self, obj):
        return obj.file.name.replace("files/", '')
