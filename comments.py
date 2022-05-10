import json
import re
import sqlite3
import uuid

import requests
from bs4 import BeautifulSoup as bs

import os
import tran
import timecuo
import random
from strgen import StringGenerator

conn = sqlite3.connect('db/6277a9de2d110.db')
c = conn.cursor()
filelist = []

g = os.walk(r"D:/PyCharm 2022.1/homework/isujin/html")

for path, dir_list, file_list in g:
    for file_name in file_list:
        # print(os.path.join(path+'/'+file_name) )
        filelist.append(os.path.join(path + '/' + file_name))

coid =2
# for遍历所有html
for index in range(0, 211):
    f = open(filelist[index], 'r', encoding='utf-8')
    html1 = f.read()
    html = bs(html1, 'html.parser')

    cid = str(filelist[index])[-9:-5]

    comment = html.find_all('div', {"class": "comment-body"})
    # print(len(comment))

    # for遍历所有评论
    for index2 in comment:
        comm_a = comment[comment.index(index2)].find_all('a')
        comm_p = comment[comment.index(index2)].p
        #comm_usrname = re.search('fn\">(([\s\S])*?)<\/cite>',str(comment[comment.index(index2)]))
        comm_usrname = comment[comment.index(index2)].find('cite', {"class": "fn"})
        if str(comm_usrname).endswith('</a></cite>'):
            comm_usrnameout = str(comm_usrname).split('>')[-3][:-3]
        else:
            #print('err')
            try:
                comm_usrnameout = str(re.search(r'fn\">(([\s\S])*?)<\/cite', str(comment[comment.index(index2)])))
                comm_usrnameout =comm_usrnameout.split('>')[-2][:-7]
            except:
                comm_usrnameout =''

        comm_usrurl = comm_a[0].attrs['href']
        comm_usrurl = 'http' + comm_usrurl.split('http')[-1]
        #print(comm_a)
        print(comm_usrnameout)
        print(comm_usrurl)
        #print(cid)
        try:
            comm_time = str(re.search(r'\d{4}\/\d{1,2}\/\d{1,2}', str(comment[comment.index(index2)])))[-12:-2]
            comm_timeout = comm_time[0][-4:]+'-'+comm_time[1]+'-'+comm_time[2][:2]
            comm_timeout = timecuo.timein(re.sub('/', '-', comm_time) + ' 09:05:20')
            # print(comment.index(index2))

            #print(comm_time)
            # print(comment.index(index2))
        except:
            print('some err')

        jsontmp = {}
        jsontmp['cid']=cid
        jsontmp['time']=comm_time
        jsontmp['commusr']=comm_usrnameout
        #jsontmp['mail']=str(random.randint(1,9999999))+'@mihoyo.ltd'
        mailtmp = str(random.randint(1,99999999))
        mailtmp = mailtmp+'@mihoyo.ltd'
        coid =coid+1

        try:
            c.execute("INSERT INTO 'typecho_comments' ('coid','cid','created',author,authorId,ownerId,mail,url,ip,agent,text,'type',status,parent) \
                  VALUES ("+str(coid)+","+str(cid)+","+str(comm_timeout)+",'"+str(comm_usrnameout)+"',0,1,'"+str(mailtmp)+"','','1.1.1.1','mihoyo','"+str(comm_p)+"','comment','approved',0)")

            conn.commit()
        except:
            print('some err')
conn.close()