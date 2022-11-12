from bottle import route, run


#route: vincula un fragmento del codigo a una URL.
# 
@route('/hello')
def hello():
    """
    route(): vincula un fragmento del codigo a una URL.
    En este caso vinculamos la ruta '/hello'
    Estas son rutas estaticas.
    """
    return "Hello World!"

@route('/')
def hola():
    """
    route(): vincula un fragmento del codigo a una URL.
    En este caso vinculamos la ruta '/' a la funcion hola
    Estas son rutas estaticas.
    """
    return '<h1> Hola Mundo </h1>'



"""
run() inicia un servidor de desarrollo incorporado.
Se ejecuta en el puerto 8080 de localhost y sirve peticiones
hasta que se pulsa ctrl+C
"""
run(host= 'localhost', port=8080, debug=True)
