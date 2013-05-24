# coding: utf8

import datetime
import time

def index(): return dict(message="hello from backend.py")

def menu(): return dict()

def menufooter(): return dict()

def bares():
   result = list()
   bares  = db( (db.bar.id>0) & (db.bar.reco==1) ).select() 

   for bar in bares[0:3]:
      comments = db( (db.comments.bar==bar.id)&
                     (db.comments.uuser==db.auth_user.id)
                   ).select()
      result.append( {'bar':bar, 'comments':comments} )

   return dict(result=result)

def counter():
   options   = dict(month=5, day=21)
   today     = datetime.date.today()
   friday    = today + datetime.timedelta( (4-today.weekday()) % 7 ) 
   now       = datetime.datetime.now()
   end_time  = datetime.datetime(year=friday.year, 
                                month=friday.month,
                                day=friday.day,
                                hour=0,
                                minute=0,
                                second=0)
   init_time =  datetime.datetime(year=today.year, 
                         month=today.month,
                         day=today.day,
                         hour=now.hour,
                         minute=now.minute,
                         second=now.second)
   diff      = end_time-init_time
   parts     = diff.__str__().split(' ')
   hora      = parts[2].split(':')[0]

   if hora>9:
      diff = "%s 0%s" % (parts[0], parts[2])
   else:
      diff = "%s %s" % (parts[0], parts[2])

   diff = diff.split('\n')[0]

   return dict(daysdiff=diff)
