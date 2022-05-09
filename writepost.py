
import time
import os
import requests
import sqlite3
import content
import cover

conn = sqlite3.connect('db/6277a9de2d110.db')
c = conn.cursor()
img = cover.cover()
imglist =cover.isset()

print(imglist)
#print(img)


# data = content.info(1)
#
# c.execute("INSERT INTO 'typecho_contents' (cid,title,slug,created,modified,text,'order',authorId,template,'type',status,password,commentsNum,allowComment,allowPing,allowFeed,parent,likes) \
#       VALUES (" + data['cid'] + ",'" + data['title'] + "', " + data['cid'] + ", " + data['time'] + ", " + data[
#     'time'] + ",'" + data['content'] + "',0,1,null,'post','publish',null,1,1,1,1,0," + data['likenum'] + " )")
#
# c.execute("INSERT INTO 'typecho_relationships' (cid,mid) \
#       VALUES (" + data['cid'] + ",1)")

##写入content
for index in range(0,211):
    data = content.info(index)
    #print(data['music'])
    musicbind = data['music'].split('/')[-1]
    if musicbind == '':
        print('empty')
    else:
        musicbind = str('/Background/Music/' + musicbind)
    #print(musicbind)
    #print(musicbind)
    try:
        imgbind = img[data['cid']]['imgname']
        if str(imgbind) in str(imglist):
            print('have')
            imgbind =str('/Background/ContentImage/'+imgbind)
        else:
            imgbind=''
    except:
        imgbind = ''

    c.execute("INSERT INTO 'typecho_contents' (cid,title,slug,created,modified,text,'order',authorId,template,'type',status,password,commentsNum,allowComment,allowPing,allowFeed,parent,views,likes) \
          VALUES ("+data['cid']+",'"+data['title']+"', "+data['cid']+", "+data['time']+", "+data['time']+",'"+data['content']+"',0,1,null,'post','publish',null,1,1,1,1,0,'"+data['looknum']+"',"+data['likenum']+" )")


    c.execute("INSERT INTO 'typecho_relationships' (cid,mid) \
          VALUES ("+data['cid']+",1)")

    c.execute("INSERT INTO 'typecho_fields' (cid,'name','type',str_value,int_value,float_value) \
          VALUES ("+data['cid']+",'coverList','str','" + imgbind + "',0,0.0)")
    c.execute("INSERT INTO 'typecho_fields' (cid,'name','type',str_value,int_value,float_value) \
          VALUES (" + data['cid'] + ",'bgMusicList','str','" + musicbind + "',0,0.0)")

#     print(index)
#

conn.commit()
conn.close()
