'''
Created on 2018年4月4日

@author: SBC
'''
import re
import os
from urllib import parse
from mysite.crawler.SpiderMan import SpiderMan

if __name__ == '__main__':
    keyworkd = '项目经理'
    keyw = parse.quote(keyworkd)
    # 
    #统计总的信息
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx?jl=%E9%87%8D%E5%BA%86&kw='+keyw+'&sm=0&p=1'
    sp = SpiderMan(url)
#     filename1 = os.path.dirname(os.path.realpath(__file__))+"\\"+keyworkd+"\\"+keyworkd+'所有智联招聘数据'+'.txt'
#     resname1 = '所有'+keyworkd
#     sp.startSpider(filename1,resname1)
     
