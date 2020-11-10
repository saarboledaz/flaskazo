from flask import Flask,jsonify,request,send_file
import comandos
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/get", methods=["GET"])
def get():
    elements = comandos.verContenidoArchivo()
    return jsonify(data = elements)
    
@app.route("/post", methods=["POST"])
def post():
    autor = request.json['autor']
    frase = request.json['frase']
    comandos.crearArchivo(autor,frase)
    return jsonify(message = True)

@app.route("/image", methods=["GET"])
def image():
    return send_file("/files/image.jpg", mimetype='image/gif')


