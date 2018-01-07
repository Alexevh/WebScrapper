import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import ssl, re

class voyager():
    """
    Este es el spider en si mismo, tiene metodos para recorrer desde una URL a las demas y metodos
    para buscar cosas especificas como direcciones de correo y guardarlas en un fichero

    """

    def __init__(self):
        self.contador = 0

    def obtenerMails(self, url, lista=[]):
        """
        Dada una URL voy a devolver una lista de correos que encontre
        :param url:
        :return:
        """

        #Cuando hagamos la recorrida esta expresion regular va a buscar los correos
        emailRegex = re.compile(r'''([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+(\.[a-zA-Z]{2,4}))''')

        #Esto es para enga;ar a los anti robots
        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        #Obtengo la pagina en bytes
        web_byte = urlopen(req).read()

        #Convierto los bytes a UTF-8
        webpage = web_byte.decode('utf-8')

        #Obtuve la pagina, ahora busco por la regEx
        email = re.findall(emailRegex, webpage)

        #lista = []
        cantidad = 0

        for mail in email:
            #No queremos correos repetidos
            if mail[0] not in lista:
                lista.append(mail[0])
                cantidad = cantidad+1
                print("encontre "+mail[0]+" voy "+str(cantidad)+" correos encontrados")

        return lista

    def buscarCorreosDesdeURL(self, url, niveles):
        """
        Vamos a recorrer desde una URL todas las que tengan conexion con ella (con links) hasta un nivel
        :param url:
        :param niveles:
        :return:
        """

        req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})

        #Inicalizo la lista de correos
        lista = []

        web_byte = urlopen(req).read()

        webpage = web_byte.decode('utf-8')


        #Obtengo todos los links de la pagina
        links = re.findall(b'href="(http://.*?)"', web_byte)

        #La primera pagina no es nivel
        lista = lista + self.obtenerMails(url)

        print("La lista lleva "+str(len(lista))+" elementos")
        self.contador = self.contador+1

        print("El contador esta en el nivel "+str(self.contador))

        for link in links:
            if (self.contador < niveles):
                self.contador = self.contador + 1
                print("el contador ahora esta en el nivel " + str(self.contador))
                lista = self.obtenerMails(link.decode(), lista)
                #self.buscarCorreosDesdeURL(link.decode(), niveles)

                print("La lista lleva " + str(len(lista)) + " elementos")


        return lista

