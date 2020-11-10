import os
import subprocess


def verContenido(ruta):
    ls = str(subprocess.check_output("ls -l " + ruta, shell = True))
    ls = ls.split('\\')
    aux = []
    l = []
    for elemento in ls[1:len(ls)-1]:
        aux = elemento.split(' ')
        aux = [x for x in aux if x]
        aux.pop(1)
        l.append({
            'permisos': aux[0],
            'usuario': aux[1],
            'grupo': aux[2],
            'peso': aux[3],
            'fecha': aux[4] + " "+ aux[5] + " " + aux[6],
            'nombre': aux[7]})
    return l



def verContenidoArchivo():
    ls = str(subprocess.check_output("ls -l /files/", shell = True))
    ls = ls.split('\\')
    aux = []
    l = []
    for elemento in ls[1:len(ls)-1]:
        aux = elemento.split(' ')
        aux = [x for x in aux if x]
        aux.pop(1)
        nombre = aux[7]
        cat = subprocess.run(['cat', "/files/{}".format(nombre)],stdout = subprocess.PIPE,stderr=subprocess.PIPE, universal_newlines=True)
        l.append({
            "nombre":nombre,
            "contenido":cat.stdout
        })
    return l

def crearArchivo(nombre, contenido):
    os.system("touch /files/{}".format(nombre))
    os.system("echo '{}'>> {}".format(contenido,nombre))

def crearCarpeta(nombre):
    os.system("mkdir " + nombre)

def borrarArchivo(nombre):
    os.system("sudo rm -f "+ nombre)

def borrarCarpeta(nombre):
    os.system("sudo rm -rf " + nombre)

def moverArchivo(nombre,destino):
    os.system("sudo mv "+ nombre + " " + destino)

def copiarArchivo(nombre,destino):
    os.system("sudo cp -r " + nombre + " " + destino)

def editarPermisos(nombre, permisos):
    os.system("sudo chmod " + permisos + " " + nombre)

def editarDueno(nombre_usuario, nombre_archivo):
    os.system("sudo chown -R " + nombre_usuario + " " + nombre_archivo)
