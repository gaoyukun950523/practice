from django.shortcuts import render
from app01 import models
# Create your views here.


def data(req):
    type_data = models.Types.objects.all()
    level_data = models.Level.objects.all()
    return render(req, "data.html",
                  {"type_data": type_data, "level_data": level_data})
def datas(req,types_id=0,level_id=0):
    comment={"types_id":types_id,"level_id":level_id}
    type_data=models.Types.objects.all()
    level_data=models.Level.objects.all()
    video_data=models.Video.objects.filter(**comment)
    return render(req,"data.html",
                  {"type_data":type_data,"level_data":level_data,"video_data":video_data,"types_id":types_id})
