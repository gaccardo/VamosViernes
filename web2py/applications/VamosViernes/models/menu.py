# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('web',SPAN(2),'py'),XML('&trade;&nbsp;'),
                  _class="brand",_href="http://www.web2py.com/")
response.title = request.application.replace('_',' ').title()
response.subtitle = T('customize me!')

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

#response.menu = [
#    (T('Home'), False, URL('default', 'index'), [])
#]

DEVELOPMENT_MENU = True

#########################################################################
## provide shortcuts for development. remove in production
#########################################################################

response.menu = [
                 ( T('HOME'),  T('Bienvenidos'), URL('Rosario', 'index'), [] ),
                 ( T('BARES'), T('Bares'),       URL('Rosario', 'bares'), 
                     [
                       ( T('Buscador'),         URL('Rosario', 'buscador')   ),
                       ( T('Aleatorio'),        URL('Rosario', 'aleatorio')  ),
                       ( T('Decir a un amigo'), URL('Rosario', 'deciramigo') )
                     ] ),
                 ( T('FOTOS'), T('Fotos de Usuarios'), URL('Rosario', 'fotos'), [] ),
                 ( T('LOGIN'), T('Ingreso para usuarios'), URL('default', 'user/login'), [] ),                 
                ]
