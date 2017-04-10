import mechanize
from bs4 import BeautifulSoup
import urllib2 
import cookielib
import playsound
from gtts import gTTS

cj = cookielib.CookieJar()
br = mechanize.Browser()
br.set_cookiejar(cj)

#Url do glpi

br.open("http://glpiti/index.php")

#Fazendo o login

br.select_form(nr=0)
br.form['login_name'] = 'usuario'
br.form['login_password'] = 'senha'
br.submit()
br.open("http://pagina de todos os chamados")

#Transformo toda a pagina em string

string = str(br.response().read())

#Contador de quantas vezes o icone que representa um novo chamado 
#aparece na pagina

nroChamadosNovos = string.count("/pics/new.png")

#Tratamento para verificar se existe um novo chamdo
#filtrando pela string /pics/new.png que é o icone de um novo chamdo

if "/pics/new.png" in string:
	text='existe um novo chamado.'
	text1='total de chamados novos'+str(nroChamadosNovos)
	tts = gTTS(text, lang='pt-br')
	tts.save("good.mp3")
	playsound.playsound('good.mp3')
	tts = gTTS(text1, lang='pt-br')
	tts.save("good2.mp3")
	playsound.playsound('good2.mp3')
