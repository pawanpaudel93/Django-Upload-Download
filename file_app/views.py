from django.core.exceptions import ObjectDoesNotExist
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status

from .serializers import FileSerializer, FileViewSerializer
from .models import File


class FileView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        file_serializer = FileSerializer(data=request.data)
        if file_serializer.is_valid():
            file_name = file_serializer.validated_data['file']
            try:
                file_obj = File.objects.get(file='files/' + '_'.join(str(file_name).split()))
            except ObjectDoesNotExist:
                file_obj = None
            if file_obj:
                file_obj.delete()
            file_serializer.save()
            return Response({'status': '1', 'message': 'File uploaded successfully', 'file_details': file_serializer.data},
                            status=status.HTTP_201_CREATED)
        else:
            return Response({'status': '0', 'message': 'File not uploaded', 'file_details': file_serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)


class FileGetView(APIView):
    def get(self, request, *args, **kwargs):
        name = 'files/' + '_'.join(self.request.query_params.get('name').split())
        print(name)
        try:
            file = File.objects.get(file=name)
            serializer = FileViewSerializer(file, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except ObjectDoesNotExist:
            return Response({"error": "File Not Found"}, status=status.HTTP_404_NOT_FOUND)


class FileGetAllView(APIView):
    def get(self, request, *args, **kwargs):
        files = File.objects.all()
        serializer = FileViewSerializer(files, many=True)
        return Response({"files": serializer.data}, status=status.HTTP_200_OK)