from django.db import models
from django.conf import settings

# Create your models here.
User = settings.AUTH_USER_MODEL

class search_model(models.Model):
    user = models.ForeignKey(User , null=True ,blank=True, on_delete=models.CASCADE)
    query = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.query
