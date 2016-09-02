#! /usr/bin/env python
#coding=utf-8

#! /usr/bin/env python
#coding=utf-8
#这里需要引入三个模块
import time, os, sched, urllib2
    
# 第一个参数确定任务的时间，返回从某个特定的时间到现在经历的秒数 
# 第二个参数以某种人为的方式衡量时间 
schedule = sched.scheduler(time.time, time.sleep) 
    
def perform_command(): 
    try:
        s = urllib2.urlopen("https://www.baidu.com").read()
        print s
    except urllib2.HTTPError,e:
       print e.code
       
        
def timming_exe(): 
    print time.time()
    #enter用来安排某事件的发生时间，从现在起第n秒开始启动 
    schedule.enter(60, 0, perform_command, ())
    # 持续运行，直到计划时间队列变成空为止 
    schedule.run()
    print time.time()
  

def print_ts(message):
    print "[%s] %s"%(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()), message)
    
def run(interval):
    print_ts("-"*100)
    while True:  
        try:  
            # sleep for the remaining seconds of interval  
            print_ts("Starting.")  
            perform_command()
            time.sleep(1)
            print_ts("end.")

        except Exception, e:  
            print e  


if __name__=="__main__":  
    interval = 60
    run(interval) 
    
# print("show time after 10 seconds:") 
# timming_exe()