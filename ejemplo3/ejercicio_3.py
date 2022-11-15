#Aplicando rutas dinamicas
from bottle import Bottle, run, template



"""
    Las rutas dinamicas contienen comodines se denominan
    rutas dinamicas y coinciden con más de una URL al mismo tiempo
    Un comodin simple consiste en un nombre encerrado entre parentesis
    angulares (ej. <name>) y acepta uno o mas caracterés hasta la 
    siguiente barra(/).
    Cada comodin pasa la parte cubierta de la URL como argumento 
    de la palabra clave a la llamada de retorno se la solicitud.
"""



app = Bottle()




@app.route('/wiki/<pagename>')   #matches /wiki/Learning_Python
def show_wiki_page(pagename):
    return template('Bienvenido a la pagina {{pagename}}',pagename=pagename)




@app.route('/<action>/<user>')
def user_api(action,user):
    return template('El usuario {{user}}, intenta realizar la acción:{{action}}',user=user, action=action)


@app.route('/object/<id:int>')
def callback(id):
    assert isinstance(id, int)
    
@app.route('/show/<name:re:[a-z]+>')
def callback(name):
    assert name.isalpha()

@app.route('/static/<path:path>')
def callback(path):
    return static_file(path, ...)

run(app,host='localhost',port=8080)