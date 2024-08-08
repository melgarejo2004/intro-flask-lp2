from flask import Flask, render_template

app = Flask(__name__)

@app.route('/inicio')
def inicio():
    return "hola mundo desde el backend"
# endpopint o ruta
@app.route('/contacto')
def contacto():
    return "<h3>Introduciendo HTML desde el servidor</h3>"

@app.route('/contacto2')
def contacto2():
       return render_template('contacto.html') 

if __name__=='__main__':
    app.run(debug=True)