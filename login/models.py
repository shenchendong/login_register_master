from django.db import models

# Create your models here.


class User(models.Model):

    gender = (
        ('male', '男'),
        ('female', '女'),
    )

    name = models.CharField(max_length=256,unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default='男')
    # auto_now_add添加时修改时间， auto_add添加、修改时都修改时间
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-create_time']
        verbose_name = '用户'
        verbose_name_plural = '用户'
