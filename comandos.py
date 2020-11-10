import os
import subprocess

def verContenidoArchivo():
    ls = str(subprocess.check_output("ls -l /files/authors/", shell = True))
    ls = ls.split('\\')
    aux = []
    l = []
    for elemento in ls[1:len(ls)-1]:
        aux = elemento.split(' ')
        aux = [x for x in aux if x]
        aux.pop(1)
        nombre = aux[7]
        cat = subprocess.run(['cat', "/files/authors/{}".format(nombre)],stdout = subprocess.PIPE,stderr=subprocess.PIPE, universal_newlines=True)
        l.append({
            "nombre":nombre,
            "contenido":cat.stdout
        })
    return l

def crearArchivo(nombre, contenido):
    os.system("touch /files/authors/{}".format(nombre))
    os.system("echo '{}' >> /files/authors/{}".format(contenido,nombre))

