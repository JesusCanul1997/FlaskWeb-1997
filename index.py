from flask import Flask, render_template
#importacion de flask y la funcionalidad template

#render_template me ayuda a obtener las paginas de la carpeta templates
app = Flask(__name__)

@app.route('/')
def home():
    #desplega el contenido de la pagina web home.html
    return render_template('home.html')

@app.route('/acerca')
def acerca():
    #desplega el contenido de la pagina web about.html
    return render_template('about.html')

if __name__ =='__main__':
    #se encarga de ejecutar el servidor
    app.run(debug=True)