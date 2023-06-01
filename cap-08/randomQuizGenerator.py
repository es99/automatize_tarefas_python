# randomQuizGenerator.py - Cria provas com perguntas e respostas em
# ordem aleatória, juntamente com os gabaritos contendo as respostas.

import random, os
from capitais import capitais
from datetime import date

data_atual = date.today()
data_txt = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
linha = "_" * 60

for quizNum in range(2):

    numero = quizNum + 1
    header = f"""
    Nome: {linha}
    Data: {data_txt}
    Período: {linha}
    """

    estados = list(capitais.keys())
    random.shuffle(estados)

    os.makedirs(f'{numero}')
    with open(f'./{numero}/prova-{numero}.txt', 'w') as prova:
        prova.write(header)
        prova.write(' ' * 20 + 'Prova %s - Estados e capitais' % (numero))
        prova.write("\n\n")

    with open(f'./{numero}/gabarito-{numero}.txt', 'w') as gabarito:
        pass