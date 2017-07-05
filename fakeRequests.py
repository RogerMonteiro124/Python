#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Developed by Roger Monteiro
#Github: https://github.com/RogerMonteiro124
import os
import urllib
from urllib import FancyURLopener
from random import *

def getUrl():
	os.system("setterm -foreground green")
	url=raw_input('Endereco do site alvo:\n>_http://')
	return str(url)
def getOrigem():
	os.system("setterm -foreground green")
	prx=raw_input('Endereco da Origem:\n>_')
	return str(prx)
def conectaSite(url,prx,user):
	Origem = {"http" : "http://"+prx}
	urllib.URLopener.version = user
	os.system("setterm -foreground red")
	resposta = urllib.urlopen(url,proxies=Origem).read()
	return str(resposta)
def Banner():
	os.system("clear")
	os.system("setterm -foreground red")
	print '''
·▄▄▄ ▄▄▄· ▄ •▄ ▄▄▄ .    ▄▄▄  ▄▄▄ ..▄▄▄  ▄• ▄▌▄▄▄ ..▄▄ · ▄▄▄▄▄.▄▄ · 
▐▄▄·▐█ ▀█ █▌▄▌▪▀▄.▀·    ▀▄ █·▀▄.▀·▐▀•▀█ █▪██▌▀▄.▀·▐█ ▀. •██  ▐█ ▀. 
██▪ ▄█▀▀█ ▐▀▀▄·▐▀▀▪▄    ▐▀▀▄ ▐▀▀▪▄█▌·.█▌█▌▐█▌▐▀▀▪▄▄▀▀▀█▄ ▐█.▪▄▀▀▀█▄
██▌.▐█ ▪▐▌▐█.█▌▐█▄▄▌    ▐█•█▌▐█▄▄▌▐█▪▄█·▐█▄█▌▐█▄▄▌▐█▄▪▐█ ▐█▌·▐█▄▪▐█
▀▀▀  ▀  ▀ ·▀  ▀ ▀▀▀     .▀  ▀ ▀▀▀ ·▀▀█.  ▀▀▀  ▀▀▀  ▀▀▀▀  ▀▀▀  ▀▀▀▀ 
	'''
	Help()
def Help():
	os.system("setterm -foreground white")
	print '''
Uso: python fakeRequestes.py
Endereço da WEB é a pagina que deseja acessar 
com um UserAgent falso.
	'''
def main():
	Banner()
	opt=input('''[1] - Usar um UserAgent especifico\n
[2] - Usar um UserAgent randominco\n>_''')
	dic = {
		1:'Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)',
		2:'Mozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)',
		3:'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)',
		4:'Opera/9.80 (X11; Linux i686; U; ru) Presto/2.8.131 Version/11.11',
		5:'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.2 (KHTML, like Gecko) Chrome/22.0.1216.0 Safari/537.2',
		6:'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_4) AppleWebKit/537.13 (KHTML, like Gecko) Chrome/24.0.1290.1 Safari/537.13',
		7:'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11',
		8:'Mozilla/5.0 (Windows NT 6.2; Win64; x64; rv:16.0.1) Gecko/20121011 Firefox/16.0.1',
		9:'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1',
		10:'Mozilla/5.0 (iPad; CPU OS 6_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/6.0 Mobile/10A5355d Safari/8536.25'
		}
	if opt ==1:
		for x in dic:
			print '[',x,'] ',dic[x]+'\n'
		userOpt=input('Opcao\n>_')
		user=dic[userOpt]	
		url='http://'+getUrl()
		prx=getOrigem()
		print conectaSite(url,prx,user)
	elif opt ==2:
		user=dic[randint(1,11)]
		url='http://'+getUrl()
		prx=getOrigem()
		print conectaSite(url,prx,user)
	else:
		print "Opção invalida"
		main()
main()
