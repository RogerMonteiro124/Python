from fake_useragent import UserAgent
import requests

#Gerando um user agente fake
def geraUserAgente():
	ua=UserAgent()
	ua.update
	user=ua.random
	return str(user)
def urlAlvo():
	url=raw_input('Endereco do site alvo:\n>_http://')
	return str(url)
def conectaSite(user,url):
	headers = {'User-Agent': user}
	response = requests.get(url, headers=headers)
	print(response.content)
def main():
	url='http://'+urlAlvo()
	user=geraUserAgente()
	conectaSite(user,url)
main()
