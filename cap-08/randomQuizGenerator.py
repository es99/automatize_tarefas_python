# randomQuizGenerator.py - Cria provas com perguntas e respostas em
# ordem aleatória, juntamente com os gabaritos contendo as respostas.

import random, os
from capitais import capitais
from datetime import date

data_atual = date.today()
data_txt = '{}/{}/{}'.format(data_atual.day, data_atual.month, data_atual.year)
linha = "_" * 60

numero_de_provas = input("Quantas provas deseja criar? ")

for quizNum in range(int(numero_de_provas)):

    numero = quizNum + 1
    header = f"""
    Nome: {linha}
    Data: {data_txt}
    Período: {linha}
    """

    estados = list(capitais.keys())
    random.shuffle(estados)

    os.makedirs(f'{numero}')

    gabarito = open(f'./{numero}/gabarito-{numero}.txt', 'w')

    with open(f'./{numero}/prova-{numero}.txt', 'w') as prova:
        prova.write(header)
        prova.write(' ' * 20 + 'Prova %s - Estados e capitais' % (numero))
        prova.write("\n\n")

        for questionNum in range(27):
            respostaCorreta = capitais[estados[questionNum]]
            respostasErradas = list(capitais.values())
            del respostasErradas[respostasErradas.index(respostaCorreta)]
            respostasErradas = random.sample(respostasErradas, 3)
            opcoes = respostasErradas + [respostaCorreta]
            random.shuffle(opcoes)

            prova.write('%s. Qual a capital do estado %s?\n' % (questionNum + 1, estados[questionNum]))
            for i in range(len(opcoes)):
                prova.write('\t%s. %s\n' % ('ABCD'[i], opcoes[i]))  
            prova.write('\n')
            gabarito.write('%s. %s\n' % (questionNum + 1, 'ABCD'[opcoes.index(respostaCorreta)]))
    gabarito.close()