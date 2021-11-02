from flask import Flask, render_template

app = Flask(__name__)

@app.route('/') # significa que estamos en este nivel de la URL cuando la llamemos
def home():
    #return "<h1>hello</h1>"
    return render_template('home.html')

if __name__ == '__main__': # estamos en este script, ejecutando directamente, no desde fuera
    app.run(debug=True) # debug True, si hago cambios, se cambian directamente sin volver a ejecutar