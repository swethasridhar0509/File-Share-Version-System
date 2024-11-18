from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file_id = models.AutoField(primary_key=True)
    file_name = models.CharField(max_length=100, unique=True)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    s3_key = models.CharField(max_length=150)
    current_version = models.IntegerField()
    uploaded_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'Files'
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.file_name} - v{self.current_version}"



class FileVersion(models.Model):
    version_number = models.AutoField(primary_key=True)
    file = models.ForeignKey(File, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=100)
    file_size = models.IntegerField()
    file_type = models.CharField(max_length=50)
    s3_key = models.CharField(max_length=150)
    is_active = models.BooleanField(default=False)
    uploaded_at = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'FileVersion'
        ordering = ['-uploaded_at']
    
    def __str__(self):
        return f"{self.file_name} - v{self.version_number}"
