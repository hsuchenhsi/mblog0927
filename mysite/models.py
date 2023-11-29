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
    
    
from django.db import models

class NewTable(models.Model):
    bigint_f = models.BigIntegerField()
    bool_f   = models.BooleanField()
    date_f   = models.DateField(auto_now=True)
    char_f   = models.CharField(max_length=20, unique=True)
    datetime_f=models.DateTimeField(auto_now_add=True)
    decimal_f= models.DecimalField(max_digits=10, decimal_places=2)
    float_f  = models.FloatField(null=True)
    int_f    = models.IntegerField(default=2010)
    text_f   = models.TextField()
