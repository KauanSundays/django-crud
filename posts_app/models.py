from django.db import models

# Create your models here.
class Posts(models.mMdel):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')
    create_at =models.DateTimeField(auto_now_add=True)#adiciona automaticamente