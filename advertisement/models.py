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
    # author = models.ForeignKey('Author',default=None,null=True,on_delete=models.CASCADE)
    # region = models.ManyToManyField('Region',default=None,null=True,related_name='region',on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:

        db_table = 'advertisements'
        ordering = ['title']


# class Author(models.Model):
#     name = models.CharField(max_length=1000)
#     register_at = models.DateTimeField(auto_now_add=True)


class AdvertisementStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Region(models.Model):
#     region_name = models.CharField(max_length=100)