import json
import re
import shutil

import requests
from bs4 import BeautifulSoup as bs

import os
import tran
import timecuo
import wget


#todo按文件名称排序
filelist = []
imglist = []
jsontmp={}
g = os.walk(r"D:/PyCharm 2022.1/homework/isujin/coverhtml")
h = os.walk(r"D:/PyCharm 2022.1/homework/isujin/coverbig")

for path,dir_list,file_list in h:
    for file_name in file_list:
        #print(os.path.join(path+'/'+file_name) )
        imglist.append(os.path.join(path+'/'+file_name) )

for path,dir_list,file_list in g:
    for file_name in file_list:
        #print(os.path.join(path+'/'+file_name) )
        filelist.append(os.path.join(path+'/'+file_name) )


def isset():
    return imglist

def cover():
    for index in range(0,10):
        f = open(filelist[index],'r',encoding='utf-8')
        html1 = f.read()
        html = bs(html1, 'html.parser')



        url = html.find_all('div',{"class":"post"})
        for index2 in range(0, 15):
            cid= url[index2].find('a').attrs['href']
            img=url[index2].find('img').attrs['src']


            #处理
            cid= cid.split('/')[-1]
            imgname = img.split('/')[-1]
            imgurl = img.split('//')
            imgurl = 'https://'+imgurl[1]+'//'+imgurl[3]
            #print(imgurl)
            # print(cid)
            # print(img)
            # print(imgurl)
            jsontmp[cid] = cid
            jsontmp2={}
            jsontmp2['imgname']=imgname
            jsontmp2['imgurl'] = img
            jsontmp[cid]=jsontmp2
            # try:
            #     url1 = str(img)
            #     filename = wget.download(url1)
            # except:''
            # print(img)






    json1 = json.dumps(jsontmp)
    jsonload= json.loads(json1)

    #print(jsonload)
    return (jsonload)

