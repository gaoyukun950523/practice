from django.db import models

# Create your models here.
class Types(models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name
class Level(models.Model):
    name=models.CharField(max_length=32)
    def __str__(self):
        return self.name
class Video(models.Model):
    title=models.CharField(verbose_name="标题",max_length=32)
    summary=models.CharField(verbose_name="简介",max_length=32)
    img=models.ImageField(verbose_name="图片",upload_to="static/img")
    href=models.CharField(verbose_name="视频地址",max_length=256)
    create_date=models.DateTimeField(auto_now_add=True)
    types=models.ForeignKey("Types",on_delete=models.CASCADE)
    level=models.ForeignKey("Level",on_delete=models.CASCADE)

    def __str__(self):
        return self.title

