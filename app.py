from flask import Flask,jsonify,request,send_file
import comandos

app = Flask(__name__)

@app.route("/get", methods=["GET"])
def get():
    elements = comandos.verContenido("/files/")
    return jsonify(data = elements)
    
@app.route("/post", methods=["POST"])
def post():
    autor = request.json['autor']
    frase = request.json['frase']
    comandos.crearArchivo(autor,frase)
    return jsonify(message = True)

@app.route("/image", methods=["GET"])
def image():
    return send_file("./image.jpg", mimetype='image/gif')


