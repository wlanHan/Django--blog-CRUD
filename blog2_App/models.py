from django.db import models

# Create your models here.


class BlogModel(models.Model):
    # her modelin gizli bir ID si vardır 
    # model.py yapılan her değişiklikten sonra py manage.py makemigrations daha sonra migrate yapılmalı
    author = models.CharField(("Yazar"), max_length=50)
    post = models.TextField(("Post İçerik"))
    createdAt = models.DateTimeField(("Tarih"), auto_now=True)
    
    
    # bu admin panelde başlığı koyuyor
    def __str__(self) -> str:
        return self.post