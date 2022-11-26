# -*- coding: utf-8 -*-
"""Desafio.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lWfme5l3_cjOYUuOFZdYQRKRJ4JkpSLf
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

business = pd.read_csv('/content/Desafio/udemy-business.csv')
design = pd.read_csv('/content/Desafio/udemy-design.csv')
music = pd.read_csv('/content/Desafio/udemy-music.csv')
web = pd.read_csv('/content/Desafio/udemy-web.csv')

geral = pd.concat([business, design, music, web])

"""### Perguntas a serem respondidas a partir dos dados.

1. Quantos cursos estão disponíveis na plataforma?
"""

total = geral['course_id'].unique()
tamanho_total = len(total)

print(f'Nossa plataforma disponibiliza total de {tamanho_total} cursos')

"""2. Quais e quantos são os cursos que abordam o assunto: JavaScript?"""

geral['course_title'] = geral['course_title'].str.lower() 
js = geral[geral['course_title'].str.contains('javascript', na= False)]

tamanho = len(js)

cursos_js = js[['course_title']]

print(f'''Temos um total de {tamanho} de JavasScript. 

Segue nossa lista:
{cursos_js}.''')

"""3. Qual é o preço médio (coluna price) dos cursos oferecidos na plataforma?"""

preço_médio = np.round(geral[['price']].mean(), 2)
preço_business = np.round(business[['price']].mean(), 2)
preço_design = np.round(design[['price']].mean(), 2)
preço_music = np.round(music[['price']].mean(), 2)
preço_web = np.round(web[['price']].mean(), 2)

print(f'''Os cursos tem um preço médio de {preço_médio} com as seguintes médias de preço em R$:

Business: {preço_business}
Design: {preço_design}
Música: {preço_music}
Web: {preço_web}

''')

"""4. Quais são os cinco cursos com maior número de inscritos (coluna num_subscribers)?"""

inscritos_ordem = geral.sort_values(by='num_subscribers', ascending=False).reset_index()
inscritos_ordem.head()
curso_1 = inscritos_ordem['course_title'][0]
curso_2 = inscritos_ordem['course_title'][1]
curso_3 = inscritos_ordem['course_title'][2]
curso_4 = inscritos_ordem['course_title'][3]
curso_5 = inscritos_ordem['course_title'][4]
maior_1 = inscritos_ordem['num_subscribers'][0]
maior_2 = inscritos_ordem['num_subscribers'][1]
maior_3 = inscritos_ordem['num_subscribers'][2]
maior_4 = inscritos_ordem['num_subscribers'][3]
maior_5 = inscritos_ordem['num_subscribers'][4]

cursos = [curso_5, curso_4, curso_3, curso_2, curso_1]
inscritos = [maior_5, maior_4, maior_3, maior_2, maior_1]


plt.plot(inscritos, cursos, 'ro', linestyle = '-', color = 'red')
plt.show()

"""5. Dos cinco cursos mais populares em termos de inscritos, mostre o rate médio, máximo e mínimo de cada um deles."""

rate_max = inscritos_ordem['Rating'].max()
rate_min = inscritos_ordem['Rating'].min()
rate_medio = np.round(inscritos_ordem['Rating'].mean(), 3)

rate = ['Avaliação (média)', 'Avaliação (min)', 'Avaliação (max)']
valores_rate = [rate_medio, rate_min, rate_max]



plt.plot(valores_rate, rate, 'ro')
plt.show()

"""6. Apresente os dez cursos mais visualizados na plataforma."""

views = geral.sort_values(by='num_reviews', ascending=False).reset_index().head(10)

curso1 = views['course_title'][0]
curso2 = views['course_title'][1]
curso3 = views['course_title'][2]
curso4 = views['course_title'][3]
curso5 = views['course_title'][4]
curso6 = views['course_title'][5]
curso7 = views['course_title'][6]
curso8 = views['course_title'][7]
curso9 = views['course_title'][8]
curso10 =views['course_title'][9]

vis1 = views['num_reviews'][0]
vis2 = views['num_reviews'][1]
vis3 = views['num_reviews'][2]
vis4 = views['num_reviews'][3]
vis5 = views['num_reviews'][4]
vis6 = views['num_reviews'][5]
vis7 = views['num_reviews'][6]
vis8 = views['num_reviews'][7]
vis9 = views['num_reviews'][8]
vis10 = views['num_reviews'][9]

cursos = [curso1, curso2, curso3, curso4, curso5, curso6, curso7, curso8, curso9, curso10]
view = [vis1, vis2, vis3, vis4, vis5, vis6, vis7, vis8, vis9, vis10]

plt.plot(view, cursos, 'ro', linestyle = '-', color = 'red')
plt.show()

"""7. A partir dos dez cursos mais vistos, mostre:


1.   qual tem o maior número de inscritos;
2.   qual tem o maior rate (avaliação do curso).



"""

subs = views.sort_values(by='num_subscribers', ascending=False).reset_index()
mais_subs = subs['course_title'][0]
subs = views['num_subscribers'].max()
print(f'''1. O curso com mais inscrições dentre os mais avaliados 
é "{mais_subs}",
ele tem {subs} inscritos\n''')

rate = views.sort_values(by='Rating', ascending=False).reset_index()
rate_maior = rate['course_title'][0]
rate = views['Rating'].max()
print(f'''2. O curso com melhor avaliação dentre os mais avaliados 
é "{rate_maior}", ele tem {rate} de pontos''')

"""8. Dos cursos listados na base de dados, qual tem maior duração em horas?"""

duracao = geral.sort_values(by='content_duration', ascending=False).reset_index()
maior_duracao = duracao['course_title'][0]
quanto_tempo = duracao['content_duration'][0]

print(f'O curso de maior duração é "{maior_duracao}" com uma duração de {quanto_tempo} horas')

"""9. Dos cursos listados na base de dados, qual tem o maior número de aulas (lectures)?"""

aulas = geral.sort_values(by='num_lectures', ascending=False).reset_index()

mais_aulas = aulas['course_title'][0]
quantas_aulas = aulas['num_lectures'][0]

print(f'''O curso com mais aulas é "{mais_aulas}" 
com {quantas_aulas} aulas''')

"""10.Apresente o número (contagem) de cursos agrupados por nível (coluna level)."""

grupo = geral.groupby(by='level').count().reset_index()
grupo

#analisando a tabela pela coluna "course_id"
print(f'''Existe 4 níveis de cursos:
- Iniciante, com 1271 cursos;
- Intermediário, com 422 cursos;
- Avançado, com 58 cursos;
- Livre, com 1925 cursos;
Sendo 3681 cursos no total''')

"""11.Quais são os cursos mais recentes contidos na base de dados?"""

publicado = geral.sort_values(by='published_timestamp', ascending=False).reset_index()
publicado.head()

"""12.Apresente o número (contagem) de cursos agrupados por nível (coluna level) e por assunto (coluna subject)."""

contagem = geral.groupby(by=['level', 'subject']).count().reset_index()
contagem

"""13. Disponibilize suas análises em um repositório do Github e compartilhe o link abaixo.

https://github.com/luizhvn1/desafio-diversidadetech-dados

14.Crie uma conta no Kaggle e crie um Notebook com as análises feitas neste projeto. A ideia aqui, é que você comece a criar um portfólio de análise de dados na plataforma :)

https://www.kaggle.com/luizenrique/desafio-diversidadetech-dados
"""