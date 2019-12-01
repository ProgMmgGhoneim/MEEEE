from django.db import models
from django.conf import settings


# Create your models here.
class category(models.Model):
    category = models.CharField(max_length=200)
    def __str__(self):
        return self.category
class post (models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL , default ='mmg' ,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True , auto_now=False)
    content = models.TextField()
    summary = models.TextField(null =True , blank =True)
    image = models.ImageField(null=True , blank=True)
    num_viwes = models.PositiveIntegerField(blank=True , default =0)
    category = models.ManyToManyField(category)

    class Meta:
        ordering = ['-timestamp']

    def __str__(self):
        return self.title






class comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,on_delete=models.CASCADE)
    post = models.ForeignKey(post , on_delete=models.CASCADE)
    txt = models.TextField(null=False)
    timestamp = models.DateTimeField(auto_now_add=True , auto_now=False)

    def __str__(self):
        return self.txt

    class Meta:
        ordering = ['-timestamp']
        
