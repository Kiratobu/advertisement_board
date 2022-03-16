from django.db import models



# Create your models here.


class Advertisement(models.Model):
    title = models.CharField(max_length=1000,verbose_name='заголовок')
    description = models.CharField(max_length=1000,default='', verbose_name='описание')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    price = models.FloatField(verbose_name='цена',default=0)
    views_count = models.IntegerField(verbose_name='количество просмотров', default=0)
    status = models.ForeignKey('AdvertisementStatus',default=None,null=True,related_name='advertisements',on_delete=models.CASCADE,
                                verbose_name='статус')
    author = models.ForeignKey('Author',default=None,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:

        db_table = 'advertisements'
        ordering = ['title']


class Author(models.Model):
    name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    biography = models.TextField()
    instagram = models.CharField(max_length=50,default=None,null=True)
    twitter = models.CharField(max_length=50,default=None,null=True)
    facebook=models.CharField(max_length=50,default=None,null=True)
    birth_date = models.DateField(null=True,blank=True)


    def __str__(self):
        return f'{self.first_name},{self.last_name}'


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

