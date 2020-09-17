from django.db import models

# Create your models here.

class Credits_Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Kategori Adı")



class Credits(models.Model):
    title = models.CharField(max_length=200,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    category = models.ForeignKey(Credits_Category, on_delete=models.CASCADE,verbose_name="Kategori")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    published = models.BooleanField(verbose_name="Görünürlük")
    def __str__(self):
        return self.title