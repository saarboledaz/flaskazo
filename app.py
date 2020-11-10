from flask import Flask,jsonify,request,send_file
import comandos
from flask_cors import CORS

comandos.createFolders()

app = Flask(__name__)

CORS(app, resources=r'/*')
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route("/api/get", methods=["GET"])
def get():
    elements = comandos.verContenidoArchivo()
    return jsonify(data = elements)
    
@app.route("/api/post", methods=["POST"])
def post():
    print(request.json)
    autor = request.json['autor']
    frase = request.json['frase']
    comandos.crearArchivo(autor,frase)
    return jsonify(message = True)

@app.route("/image", methods=["GET"])
def image():
    return send_file("/files/assets/image.jpg", mimetype='image/gif')


