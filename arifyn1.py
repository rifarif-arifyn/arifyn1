#!/usr/bin/python2
#coding=utf-8


import os,sys,time,datetime,random,hashlib,re,threading,json,urllib,cookielib,requests,mechanize
from multiprocessing.pool import ThreadPool
from requests.exceptions import ConnectionError
from mechanize import Browser


reload(sys)
sys.setdefaultencoding('utf8')
br = mechanize.Browser()
br.set_handle_robots(False)
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(),max_time=1)
br.addheaders = [('User-Agent', 'Opera/9.80 (Android; Opera Mini/32.0.2254/85. U; id) Presto/2.12.423 Version/12.16')]


def keluar():
	print "\033[1;96m[!] \x1b[1;91mExit"
	os.sys.exit()


def acak(b):
    w = 'ahtdzjc'
    d = ''
    for i in x:
        d += '!'+w[random.randint(0,len(w)-1)]+i
    return cetak(d)


def cetak(b):
    w = 'ahtdzjc'
    for i in w:
        j = w.index(i)
        x= x.replace('!%s'%i,'\033[%s;1m'%str(31+j))
    x += '\033[0m'
    x = x.replace('!0','\033[0m')
    sys.stdout.write(x+'\n')


def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(00000.1)


##### LOGO #####
logo = """\033[1;34m█████████
\033[1;34m█▄█████▄█      \033[1;35m●▬▬▬▬▬▬▬▬▬๑۩۩๑▬▬▬▬▬▬▬▬●
\033[1;34m█\033[1;92m▼▼▼▼▼ \033[1;92m- _ --_--\033[1;34m╔╦╗┌─┐┬─┐┬┌─   ╔═╗╔╗
\033[1;34m█ \033[1;92m \033[1;92m_-_-- -_ --__\033[1;93m ║║├─┤├┬┘├┴┐───╠╣ ╠╩╗
\033[1;34m█\033[1;92m▲▲▲▲▲\033[1;92m--  - _ --\033[1;35m═╩╝┴ ┴┴└─┴ ┴   ╚  ╚═╝ \033[1;34mRIFARIF'ARIFYN 
\033[1;34m█████████      \033[1;92m«----------✧----------»
\033[1;34m ██ ██
\033[1;96m╔═══════════════════════════════════════════════╗
\033[1;96m║\033[1;96m* \033[1;93mAuthor  \033[1;93m : \033[1;93mBrother•|RIFARIF'ARIFYN\033[1;96m           ║
\033[1;96m║\033[1;96m* \033[1;93mGitHub  \033[1;93m : \033[1;93m\033[4mhttps://Github.com/rifarif-arifyn\033[0m \033[1;96m║
\033[1;96m║\033[1;96m* \033[1;93mWhatsApp \033[1;93m: \033[1;93m0856-1391-5016\033[1;96m                    ║
\033[1;96m╚═══════════════════════════════════════════════╝"""

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\033[1;96m[●] \x1b[1;93mSedang masuk \x1b[1;97m"+o),;sys.stdout.flush();time.sleep(1)


back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

os.system("clear")
print "\033[1;96m ====================================================="
print  """\033[1;34m [☆] \x1b[1;93mASSALAMUALAIKUM\x1b[1;96m  \033[1;34m   [☆] \x1b[1;93mWHATSAPP : +6285813915016\x1b[1;96m  
\033[1;34m [☆] \x1b[1;93mSELAMAT DATAMG\x1b[1;34m      [☆] \x1b[1;93mFACEBOOK : RIFARIF'ARIFYN \x1b[1;96m  
\033[1;34m [☆] \x1b[1;93mTOOLS ARIFARIFYN\x1b[1;34m    [☆] \x1b[1;93mYOUTUBE  : RIFARIF'ARIFYN \x1b[1;96m"""
print " \x1b[1;96m====================================================="

CorrectUsername = "RIFARIF'ARIFYN"
CorrectPassword = "ARWA0212"
