from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200) #標題
    slug=models.CharField(max_length=200) #網址
    body=models.TextField() #內容
    category=models.TextField(null=True) #分類
    pub_date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=('-pub_date', ) #-反向排序
        
    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    pub_date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.text    
    
class Product(models.Model):
    SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=20)
    price = models.PositiveIntegerField()
    size = models.CharField(max_length=1, choices=SIZES)
    result = models.BooleanField()
    