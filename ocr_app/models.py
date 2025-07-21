

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class OCRResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads/')
    extracted_text = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return f"{self.user.username} - {self.uploaded_at}"