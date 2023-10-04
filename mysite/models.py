from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200) #標題
    slug=models.CharField(max_length=200) #網址
    body=models.TextField() #內容
    pub_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=('-pub_date', ) #-反向排序
    def __str__(self) -> str:
        return self.title