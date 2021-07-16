# Este repositório contém: 


1. 1 sistema em Pyhton que permite **converter moedas de 267 países** através de web scraping que realiza no site do Iban, utilizando as bibliotecas Requests, Beautiful Soup e Babel. :brazil: :us: :uk: :canada: :fr: :georgia: :de: :uzbekistan: :vietnam: :singapore: :australia: :austria: :ireland: :israel: :ethiopia: :south_africa: :earth_africa: :euro:




#  Este repositório tem a finalidade de:


1. Servir como meu material de apoio para relembrar conceitos, sintaxes, bibliotecas e funções úteis na linguagem, através de exemplos práticos, com códigos organizados e conteúdo visualmente fácil de encontrar.
2. mostrar um pouco dos meus conhecimentos e da minha evolução e forma de pensar Python e programação
3. contribuir com a comunidade compartilhando conhecimento prático, e também me abrir para aprendizados e contribuições



# Bibliotecas utilizadas:



1. Requests

2. BS4 - será utilizado o módulo Beautiful Soup

3. Babel - será utilizado o módulo Numbers, com a função format_currency




# Para melhor explorá-lo, como principal sugestão, siga os passos abaixo:




1. Clone o repositório para o seu ambiente de desenvolvimento
2. Abra o terminal, caminhe até a pasta clonada do projeto. 
3. Na linha de comando, digite **pip3 install requests --users** para instalar a biblioteca Requests
4. Na linha de comando, digite **pip3 install bs4** para instalar a biblioteca BS4, que contém o módulo Beautiful Soup que será utilizado neste programa
5. Na linha de comando, digite **pip3 install babel --users** para instalar a biblioteca Babel, que contém os módulos numbers e format_currency que serão utilizados neste programa para formatar as moedas.



Após a instalação de todas as bibliotecas necessárias, vamos a execução:



6. Na linha de comando, ainda dentro da pasta do projeto, digite **python3 main.py**
7. Pronto, o programa iniciará:
   - O sistema, inicialmente, tentará acessar a url do site do Iban com a biblioteca requests. 
   - Em seguida, retornará em seu terminal um índice com a lista de 267 países.
   - Escolha o país da moeda de origem e digite o número correspondente na lista
   - Escolha o país de conversão e digite o número correspondente na lista
   - Digite o valor monetário a ser convertido
   - Pronto, o programa retornará um output com o resultado da conversão.



## **Como foram organizados os conteúdos** e por que:

O sistema é composto por 2 arquivos:

1. **main.py**: aqui está localizado o código principal, onde serão executadas as funções criadas e importadas para fazer o programa funcionar.

2. **funcoes.py**: aqui estão localizadas as funções criadas que serão utilizadas no código principal para fazer o programa funcionar.
