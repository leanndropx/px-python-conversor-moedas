import requests
from bs4 import BeautifulSoup


def cria_lista_iban(url):
  
  try:
    requisicao=requests.get(url)
    if requisicao.status_code==200:
      print(f'Acessamos o site {url}')
      print('Escola pelo número da lista o país que deseja consultar o código de moeda')

  except:
    print(f'O site {url} não está acessando')



  #PASSO 3 - salvou o texto da requisição em uma variável
  html_texto = requisicao.text


  #PASSO 4 - criou a variavel soup com o texto html
  soup=BeautifulSoup(html_texto, 'html.parser')


  #PASSO 5 - encontrou todas as tags 'tr', colocou em uma lista e deletou a Head da tabela
  paises=soup.find_all('tr')
  del paises[0]


  #PASSO 6 - criou um dicionario e uma lista pra usar no loop de filtro das informações de pais e codigo da moeda
  dicionario={}
  lista=[]

  #PASSO 7 - executou o loop, filtrou Pais e Codigo e adicionou no dicionario e na lista
  for c in paises:
    for k,v in enumerate(c):
      
      if k==1:
        dicionario['pais']=v.get_text()
        
      if k==5:
        dicionario['codigo']=v.get_text()
        
    lista.append(dicionario.copy())
  return lista

def usuario_escolhe(lista):
  
  lista_para_return=[]
  print()
  try:
    escolha = int(input('Informe pelo número o país de origem: '))
    
    while escolha<0:
      escolha = int(input('Escolha um número entre 0 e 267 para escolher o país de origem: '))

    if escolha>=0 and escolha<=len(lista):
      print(f'  [ x ] - {lista[escolha]["pais"]}')
      origem=lista[escolha]["codigo"]

    if escolha>len(lista):
      print('Não existe, escolha uma opção na lista')
      return lista_para_return

    else:
      try:
        escolha_conversao=int(input('quer negociar com qual país?: '))
        
        while escolha_conversao<0:
          escolha_conversao=int(input('Escolha um número entre 0 e 267 para o país com o qual você quer negociar: '))


        if escolha_conversao>=0 and escolha_conversao<=len(lista):
          print(f'  [ x ] - {lista[escolha_conversao]["pais"]}')
          destino=lista[escolha_conversao]["codigo"]

          quantos=float(input(f'e quantos {lista[escolha]["codigo"]} você quer converter para {lista[escolha_conversao]["codigo"]}: '))
          
          lista_para_return=[origem,destino,quantos]
          return lista_para_return
          

        if escolha_conversao>len(lista):
          print('Não existe, escolha uma opção na lista')
          return lista_para_return

      except:
        print('Isto não é um número')
        return lista_para_return
  except:
    print('Isto não é um número')
    return lista_para_return
 
def personaliza_url(lista_para_return):
  if len(lista_para_return)==0:
    print('Tente novamente')
  else:
    origem=lista_para_return[0]
    destino=lista_para_return[1]
    quantos=lista_para_return[2]

    url=f'https://transferwise.com/gb/currency-converter/{origem}-to-{destino}-rate?amount={quantos}'
    return url

