
import requests  # Modulo responsavel por entrar no site e pegar seus dados.
from bs4 import BeautifulSoup  # Manipula o HTML dentro do Python

url = r'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)  # Pegando os dados da url
html = BeautifulSoup(response.text, 'html.parser')  # Analisa o html da url e retorna ela

print('\n\n\t\t\033[;1mAs principais perguntas sobre python'
      '\n\t\t\t\tna stackoverflow\033[m')
input('\nPressione enter para mostrar.\n\n')


for pergunta in html.select('.s-post-summary.js-post-summary'):  # Para cada elemento de uma pergunta em HTML
    print('--' * 40)
    voto = pergunta.select_one('.s-post-summary--stats-item-number')  # Pegando votos da pergunta com o nome da classe
    titulo_pergunta = pergunta.select_one('.s-link')  # Pegando titulo da pergunta
    data_da_pergunta = pergunta.select_one('.relativetime')  # Pegando a data da pergunta

    print(f"""[{data_da_pergunta.text}]
Votos: {voto.text}
Pergunta
    {titulo_pergunta.text}""")
