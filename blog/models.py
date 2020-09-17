from django.db import models

class Blog_Category(models.Model):
    name = models.CharField(max_length=100, verbose_name = "Kategori Adı")
    url = models.CharField(max_length=100, verbose_name = "Kategori URL")
    def __str__(self):
        return self.name




class Blog(models.Model):
    title = models.CharField(max_length=200,verbose_name="Başlık")
    content = models.TextField(verbose_name="İçerik")
    quote = models.TextField(blank = True, null = True, verbose_name = "Alıntı")
    category = models.ForeignKey(Blog_Category, on_delete=models.CASCADE,verbose_name="Kategori")
    date = models.DateTimeField(auto_now_add=True,verbose_name="Oluşturulma Tarihi")
    published = models.BooleanField(verbose_name="Görünürlük")
    image_1 = models.FileField(blank = True, null = True, verbose_name="Makaleye içerik ekleyin",default="buyap.jpeg")
    image_2 = models.FileField(blank = True, null = True, verbose_name="Makaleye içerik ekleyin",default="buyap.jpeg")
    image_3 = models.FileField(blank = True, null = True, verbose_name="Makaleye içerik ekleyin",default="buyap.jpeg")
    image_4 = models.FileField(blank = True, null = True, verbose_name="Makaleye içerik ekleyin",default="buyap.jpeg")
    def __str__(self):
        return self.title