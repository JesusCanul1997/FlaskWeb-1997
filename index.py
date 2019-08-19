from flask import Flask
from flask import render_template #funcionalidad template

#render_template me ayuda a obtener las paginas de la carpeta templates
app = Flask(__name__)

@app.route('/')
def home():
    #desplega el contenido de la pagina web home.html
    return render_template('home.html')

@app.route('/diseños')
def diseños():
    #desplega el contenido de la pagina web diseños.html
    return render_template('diseños.html')

@app.route('/acerca')
def acerca():
    #desplega el contenido de la pagina web about.html
    return render_template('about.html')

@app.route('/contacto')
def contacto():
    #desplega el contenido de la pagina web contacto.html
    return render_template('contacto.html')

if __name__=='__main__':
    #se encarga de ejecutar el servidor
    app.run(debug=True)