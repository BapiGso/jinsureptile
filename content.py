import json
import re

import requests
from bs4 import BeautifulSoup as bs

import os
import tran
import timecuo


#todo按文件名称排序
filelist = []

g = os.walk(r"D:/PyCharm 2022.1/homework/isujin/html")

for path,dir_list,file_list in g:
    for file_name in file_list:
        #print(os.path.join(path+'/'+file_name) )
        filelist.append(os.path.join(path+'/'+file_name) )

def info(htmlname):
    f = open(filelist[htmlname],'r',encoding='utf-8')
    html1 = f.read()
    html = bs(html1, 'html.parser')

    #时间、标题、内容
    cid =str(filelist[htmlname])[-9:-5]

    time = html.find_all("span")[2].string
    timetmp = time.split(' ')
    mon= tran.mon(timetmp[0][:-1])
    day = timetmp[1][:-1]
    year = timetmp[2]
    timecache= str(year)+'-'+str(mon)+'-'+str(day)+' 00:09:05'
    timefinal = timecuo.timein(timecache)

    title = html.h1.string
    content = html.find('div',{"class":"content"}).get_text()
    content = re.sub('http(([\s\S])*?)mp3','',content)#去掉MP3
    content = '<!--markdown-->'+content#加上MD标识
    #print(content)




    #阅读数、喜欢、背景音乐
    looknum = html.find_all("span")[3].string
    looknum = looknum[3:]
    likenum = html.find_all("span")[8].string
    music = html.find_all('source')[0].attrs['src'] if html.find_all('source') else ''

    #评论
    comment = html.find('li',{"class":"comment even thread-even depth-1 parent"})
    #comment_child = comment.find_all('ol',{"class":"children"})
    #print(comment)
    #print(len(comment.find_all('p')))
    #print(len(comment.find_all('p')))

    #封面处理

    jsontmp={}
    jsontmp['cid']=cid
    jsontmp['time']=timefinal
    jsontmp['title']=str(title)
    jsontmp['content']=str(content)
    jsontmp['looknum']=str(looknum)
    jsontmp['likenum']=str(likenum)
    jsontmp['music']=str(music)


    json1 = json.dumps(jsontmp)
    jsonload= json.loads(json1)
    #print(jsonload['content'])
    return jsonload


