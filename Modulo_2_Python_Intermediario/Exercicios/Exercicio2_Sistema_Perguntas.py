# Exercicio - Sistema de perguntas e resposta

perguntas = [
    {
        'Pergunta': 'Quanto é 2+2?',
        'Opções': ['1', '3', '4', '5'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10/2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5',
    },
]


def questoes():
    contador_acerto = 0
    for pergunta in perguntas:
        print('Pergunta: ',pergunta['Pergunta'])
    
        opcoes = pergunta['Opções']

        for x, y in enumerate(opcoes):
            print(f'{x})', y)
    
        confirma = input('Digite uma alternativa: ')

        confirma_int = None

        if confirma.isdigit():
            confirma_int = int(confirma)

        if opcoes[confirma_int] == pergunta['Resposta']:
            contador_acerto += 1
            print('Voce acertou')
        else:
            print('Você errou')

    print(contador_acerto)
                        
questoes()




