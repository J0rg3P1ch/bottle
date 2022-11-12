#Ejemplo utilizando POO
from bottle import Bottle, run, template



app = Bottle()
"""
Se crea instancia de Bottle que se crea la primera vez
que se llama a route()
"""


@app.route('/')
@app.route('/hola/<name>')
def greet(name='Extraño'):
    """
    REQUEST ROUTING
    Este ejemplo demuestra dos cosas:
    -Se pueden vincular más de una ruta a una sola
    devolución de la llamada.
    -Se pueden añadir mas comodines a las URL
    y acceder a ellas mediante argumentos de 
    palabras clave.
    """
    return template('Hola {{name}}, ¿cómo estas?', name=name)




run(app,host='localhost',port=8080)