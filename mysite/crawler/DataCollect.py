'''
Created on 2018年4月4日

@author: SBC
'''
import os
import time
from . import models

class DataCollect(object):
    '''
    classdocs
    '''
    low_salary = 0
    high_salary = 0
    num_count = 0
    def __init__(self):
        '''
        Constructor
        '''
    def saveData(self,lis,file_name,name):
#         t = int(time.time())
#         if not os.path.exists(os.path.dirname(file_name)) :
#             os.mkdir(os.path.dirname(file_name))
#         document = open(file_name,'a')
        lens = len(lis)-1
#         try:
        while lens>0 :
            lens-= 1
            info = lis[lens]
            if info.get('position') is None or info.get('company') is None or info.get('low_salary') is None or info.get('high_salary') is None or info.get('gzdd') is None:
                print('这是空的')
                continue
#             dic = {'comp':info.get('company'),'low':info.get('low'),'high':info.get('high')
#                    ,'pos':info.get('position'),'addr':info.get('gzdd'),'site':'智联招聘','status':0,'name':name}
            models.Info.objects.create(comp=info.get('company'),low=info.get('low_salary'),high=info.get('high_salary')
                   ,pos=info.get('position'),addr=info.get('gzdd'),site='智联招聘',status=0,name=name)
            l = int(info.get('low_salary'))
            h = int(info.get('high_salary'))
            self.low_salary =self.low_salary + l
            self.high_salary += h
            self.num_count +=1
#         except:
#             print('文件写入错误')
#         finally:
#             print('文件写入完毕')  
        pass
    
    def writeResult(self,keyword):
            if self.num_count == 0:
                print('一条数据都没有')
                avg_low_salary = 0
                avg_high_salary = 0
            else:
                avg_low_salary = int(self.low_salary/self.num_count)
                avg_high_salary = int(self.high_salary/self.num_count)
            models.TotalInfo.objects.create(name=keyword,avg_low=avg_low_salary,avg_high=avg_high_salary,site='智联招聘',count=self.num_count)
            self.low_salary = 0
            self.high_salary = 0
            self.num_count = 0