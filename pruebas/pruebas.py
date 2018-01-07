from Spider import voyager as v



sonda = v.voyager()
url = 'https://www.xataka.com/servicios/gmail-27-trucos-y-algun-extra-para-exprimir-al-maximo-tus-correos'

#Probamos obtener los mails de una pagina
lista = sonda.obtenerMails(url)
print("La lista tiene estos elementos  : "+str(len(lista)))
#for correo in lista:
    #print(correo)


#Probamos recursividad
lista2 = sonda.buscarCorreosDesdeURL(url, 50)
for correo in lista2:
    print(correo)


#print("La lista tiene :"+str(len(lista2)))+" elementos"