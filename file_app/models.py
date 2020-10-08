from django.db import models
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
import os

class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, *args, **kwargs):
        if self.exists(name):
            self.delete(name)
            # os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name

class File(models.Model):
    file = models.FileField(upload_to='files', storage=OverwriteStorage())