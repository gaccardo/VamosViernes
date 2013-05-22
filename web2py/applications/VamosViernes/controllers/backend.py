# coding: utf8
# intente algo como
def index(): return dict(message="hello from backend.py")

def menu(): return dict()

def bares():
   result = list()
   bares  = db( (db.bar.id>0) & (db.bar.reco==1) ).select() 

   for bar in bares[0:3]:
      comments = db( (db.comments.bar==bar.id)&
                     (db.comments.uuser==db.auth_user.id)
                   ).select()
      result.append( {'bar':bar, 'comments':comments} )

   return dict(result=result)
