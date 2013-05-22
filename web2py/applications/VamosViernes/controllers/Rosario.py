# coding: utf8

def index(): 
   return dict()

def bares():
   response.flash = "VamosViernes Rosario"
   result         = list()
   bares          = db(db.bar.id).select() 

   for bar in bares:
      comments = db( (db.comments.bar==bar.id)&(db.comments.uuser==db.auth_user.id) ).select()
      result.append( {'bar':bar, 'comments':comments} )

   return dict(bares=result)
