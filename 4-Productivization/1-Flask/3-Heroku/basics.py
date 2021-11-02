# -*- coding: utf-8 -*-
from flask import Flask, render_template # render_template después de enseñar "hello"

app = Flask(__name__)

@app.route('/') # / significa que estamos en ese nivel de la URL cuando la llamemos
def home():
    #return "<h1>hello</h1>"  # esta línea primero, luego con la de abajo
    return render_template('home.html')

if __name__ == '__main__':  # estamos en este script, ejecutando este script directamente, no llamando desde fuera
    app.run(debug=True) # debug True, si hago cambios, se cambian directamente sin volver a ejecutar nada
