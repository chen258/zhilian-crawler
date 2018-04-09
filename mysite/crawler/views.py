from django.shortcuts import render
from django.http import HttpResponse
import re
import os
from urllib import parse
import json
import random
from . import SpiderMan
from . import models
import threading
# Create your views here.
def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
    return render(request,'crawler.html')

def crawl(request):
    keyworkd = request.GET.get('keyword')
    info = models.Info.objects.filter(name=keyworkd)
    len = info.__len__()
    if len > 0:
        print('正在搞事情，别搞啦')
        return render(request,'crawlershow.html',{'keyword':keyworkd}) 
    print('开始去搞事情')
    t = threading.Thread(target=thRun,args=(keyworkd,))
    try:
        t.start()
    except:
        print('线程执行出错了')
    print('开启线程搞事情')
    return render(request,'crawlershow.html',{'keyword':keyworkd})

def thRun(keyworkd): 
    keyw = parse.quote(keyworkd)
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%87%8D%E5%BA%86&kw='+keyw+'&sm=0&p=1'
    sp = SpiderMan.SpiderMan(url)
    filename1 = os.path.dirname(os.path.realpath(__file__))+"\\"+keyworkd+"\\"+keyworkd+'所有智联招聘数据'+'.txt'
    resname1 = '所有'+keyworkd
    sp.startSpider(filename1,resname1,keyworkd)
    
def getcrawl(request):
    key = request.GET.get('keyword');
    try:
        totalinfo = models.TotalInfo.objects.filter(name=key).values_list()
    except:
        print('数据库查询冲突，开始休眠')
    len = totalinfo.__len__()
    sta = 0
    data = {}
    if len > 0:
        # ok 已经搞定了
        sta = 1
        data['total_data']= {'site':'智联招聘','avg_low':totalinfo[0][2],'avg_high':totalinfo[0][3],'count':totalinfo[0][5]
                             ,'name':totalinfo[0][1]}
    data['status'] = sta
    data['data'] = []
    
    info = models.Info.objects.filter(name=key).values_list()
    for i in info:
        data['data'].append({'comp':i[2],'low':i[3],'high':i[4],'pos':i[5],'addr':i[6]})
    str = json.dumps(data)
    return HttpResponse(str)