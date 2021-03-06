from django.db import models
from PIL import Image

from django.contrib.auth.models import User

class Department(models.Model):
    department_name = models.CharField(max_length=200)

    def __str__(self):
        return self.department_name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    department = models.ForeignKey(Department, null=True, blank=True, on_delete=models.CASCADE)
    is_frontdesk = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super().save()

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)