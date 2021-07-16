
import requests
from bs4 import BeautifulSoup
from babel.numbers import format_currency
from funcoes import cria_lista_iban
from funcoes import usuario_escolhe
from funcoes import personaliza_url

print('Bem-vindo ao navegador de moedas')
print()

# - variável recebe função que retorna uma lista com países e códigos de moeda.
lista_com_paises=cria_lista_iban("https://www.iban.com/currency-codes")

#loop na lista com numeração na lista criada
for index,c in enumerate(lista_com_paises):
  print(f'{index} - {lista_com_paises[index]["pais"]}')

#variável recebe função que retorna lista com 3 valores: código da moeda de origem, código da moeda de conversão e valor escolhido para conversão.
lista_com_escolhidos=usuario_escolhe(lista_com_paises)


#função personaliza a url da transferwize com códigos das moedas e quantidade escolhida pelo usuário
url_personalizada=personaliza_url(lista_com_escolhidos)


#tenta fazer o request, e conseguir, recebe os valores e faz a conversão.
try:
    requisicao=requests.get(url_personalizada)
    if requisicao.status_code==200:
      print('Conseguimos acessar:')
      print(f'{url_personalizada}')
      print()

      #recebe a string do valor unitário da moeda escolhida
      html_texto=requisicao.text
      soup=BeautifulSoup(html_texto, 'html.parser')
      tag_resultado=soup.find('span',class_='text-success').get_text()
      
      
      #transforma a string em numero, faz os calculos e conversões
      valor_unitario_destino=float(tag_resultado)
      valor_conversao=lista_com_escolhidos[2]
      resultado=valor_unitario_destino*valor_conversao
      
      valor_conversao_formatado=format_currency(valor_conversao, lista_com_escolhidos[0])
      
      resultado_formatado=format_currency(resultado,lista_com_escolhidos[1])

    
      print(f'{valor_conversao_formatado} é igual a {resultado_formatado}')
    
        
    else:
      print()
      print(f'Conseguimos nos comunicar com o servidor mas o site não conseguiu completar a requisição. Response status: {requisicao.status_code}')

except:
  print('Não foi possível concluir sua requisição')



