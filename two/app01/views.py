from django.shortcuts import render,HttpResponse,redirect
from app01 import models
# Create your views here.

def login(req):
    return render(req,"inits.html")


def test(req):
    datas=req.POST.get("datas")
    pargh={"title":"啥子","content":datas}
    models.Article.objects.create(**pargh)
    return HttpResponse(datas)
def check(req):
    datas=models.Article.objects.get(id=2)
    print(datas.title)
    return render(req,"test.html",{"datas":datas.content})
