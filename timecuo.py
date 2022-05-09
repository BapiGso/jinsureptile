import time
def timein(s):
    #s="2016-05-05 20:28:54"
    #转换成时间数组
    timeArray = time.strptime(s, "%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timestamp = time.mktime(timeArray)
    timeout = str(timestamp)[:-2]
    return timeout

