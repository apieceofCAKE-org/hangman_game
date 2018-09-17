# -*- coding: utf-8 -*-

# Trabalho Prático: Programar o jogo da forca
# Prazo: 7 de jul 23:59

# Luis Marti Orosa
# Programe o jogo da forca (https://pt.wikipedia.org/wiki/Jogo_da_forca)
# a partir do arquivo 'jogodaforca.py' completando as funções
# não implementadas do mesmo.

# Importante:
# * Edite o cabeçalho do arquivo para incluir seu nome e matrícula.
# * Entregue o resultado via google classroom antes da data limite.
# * O código está também disponível em:
# https://github.com/rio-group/Prog1-trabalho

# Os arquivos que você adicionar ou criar poderão ser visualizados
# e editados pelo seu professor

# ******************************************************************

# Trabalho Prático I: Implementar o jogo da forca
# Completar a seguinte informação:
# Nome: Caíque Guimarães Evaristo
# Matrícula: 118083018
# jogoforca.py

# ******************************************************************

import random
from unicodedata import normalize

LISTA_PALAVRAS = ('Mequetrefe', 'Salamaleque', 'Piripaque', 'Serelepe',
                  'Siricutico', 'Bugiganga', 'Borogodó', 'Quinquilharia',
                  'Beleléu', 'Balacobaco', 'Faniquito', 'Quiproquó', 'Pebolim',
                  'Ziquizira', 'Zunzunzum', 'Ziguezague')


# Número máximo de tentativas.
MAX_TENTATIVAS = 6


def obter_palavra():
    '''
    Retorna uma palavra aleatória da lista de palavras LISTA_PALAVRAS.
    '''

    ps_acento = random.choice(LISTA_PALAVRAS)

    # As letras serão sempre maíusculas e sem acentos.
    ps_acento = ps_acento.upper()
    palavra_secreta = (normalize('NFKD', ps_acento)
                       .encode('ASCII', 'ignore').decode('ASCII'))

    return palavra_secreta


def palavra_adivinhada(palavra_secreta, letras_usuario):
    '''
    Retorna True se os caracteres presentes na lista letras_usuario são
    suficentes para adivinhar a palavra palavra_secreta.
    Retorna False em outro caso.

    Parâmetros:
    * palavra_secreta: palavra a ser adivinhada.
    * letras_usuario: lista das letras que o usuário entrou até agora.
    '''

    ps = palavra_secreta[:]
    lu = letras_usuario[:]
    conjunto_lu = set(lu)
    conjunto_ps = set(ps)

    # Verifica se o conjunto com as letras da palavra secreta é subconjunto
    # do conjunto das letras do usuário.
    if conjunto_ps.issubset(conjunto_lu):
        return True
    else:
        return False


def tentativas_erradas(palavra_secreta, letras_usuario):
    '''
    Retorna a quantidade de letras em letras_usuario que não aparecem em
    palavra_secreta.

    Parâmetros:
    * palavra_secreta: palavra a ser adivinhada.
    * letras_usuario: lista das letras que o usuário entrou até agora.
    '''

    # Tomando o cuidado de não modificar os parâmetros por referência.
    ps2 = palavra_secreta[:]
    lu2 = letras_usuario[:]
    conjunto_lu2 = set(lu2)
    conjunto_ps2 = set(ps2)

    # Contador:
    k = 0

    for x in conjunto_lu2:
        if x not in conjunto_ps2:
            k += 1

    return k


def mostra_adivinhadas(palavra_secreta, letras_usuario):
    '''
    Mostra que letras de palavra_secreta tem sido adivinhadas até agora e
    todas as letras entradas pelo usuário.

    Por exemplo, a saída para a palavra secreta "batatinha" e as entradas do
    usuário b, c e t deve ser do tipo:

    Palavra secreta: B _ T _ T _ _ _ _
    Letras tentadas até agora: B, C, T

    Parâmetros:
    * palavra_secreta: palavra a ser adivinhada.
    * letras_usuario: lista das letras que o usuário entrou até agora.
    '''

    palavra_incompleta = []
    for y in palavra_secreta:
        if y in letras_usuario:
            palavra_incompleta.append(y)
        else:
            palavra_incompleta.append('_')

    print('Palavra secreta: ')
    print('')

    # Formatação das listas para a impressão de duas maneiras diferentes.
    print(' '.join(str(x) for x in palavra_incompleta))
    print('')
    print('Letras tentadas até agora: ')
    print('')
    print(*letras_usuario, sep=', ')
    print('')


def entra_tentativa():
    '''
    Permite ao usuário entrar uma letra. Deve garantir que a entrada não seja
    um caracter inválido (números, varias letras, signos de pontuação, etc.)
    '''

    # Garantindo um bom funcionamento com try/except.
    while True:
        try:
            while True:
                letra = str(input('Entre com uma letra: '))

                # Lidando com erros de entrada.
                # letra deve ser uma string de um caractere que seja letra.
                if not letra.isalpha() or len(letra) != 1:
                    print('')
                    print('O caractere é inválido. Tente novamente...')
                    continue
                else:
                    break
            break
        except TypeError or ValueError:
            print('Entrada inválida. Tente novamente...')
    print('*' * 35)
    print('')

    # As letras serão sempre maíusculas.
    letra = letra.upper()
    return letra


def jogo_da_forca():
    '''
    Função principal do jogo.
    '''

    print('')
    print('Bem vindo ao jogo da forca. Versão feita pelo Caíque com carinho!')
    print('')
    print('*' * 35)
    print('')

    while True:
        palavra_secreta = obter_palavra()

        letras_usuario = []

        while not palavra_adivinhada(palavra_secreta, letras_usuario) and \
            tentativas_erradas(palavra_secreta, letras_usuario) < \
                MAX_TENTATIVAS:

                    mostra_adivinhadas(palavra_secreta, letras_usuario)

                    restantes = MAX_TENTATIVAS - \
                        tentativas_erradas(palavra_secreta, letras_usuario)

                    print('Tentativas restantes: ', restantes)
                    letra = entra_tentativa()
                    if letra in letras_usuario:
                        print('Letra já inserida previamente! Continuando...')
                        print('')
                    else:
                        letras_usuario.append(letra)

        mostra_adivinhadas(palavra_secreta, letras_usuario)

        if palavra_adivinhada(palavra_secreta, letras_usuario):
            print('Parabéns, você adivinhou a palavra!')
        else:
            print('¯\\_(ツ)_/¯ você perdeu.')

        print('')

        # Garantindo um bom funcionamento com try/except.
        while True:
            try:
                cont = input('Entre C se deseja continuar jogando: ')
                break
            except TypeError or ValueError:
                print('Entrada inválida!')
                print('')
        if not (cont == 'C' or cont == 'c'):
            break

    print('')
    print('Game over. Até a próxima!')


boneco = '''
                     ▗▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
                     ▐█                        ▘
                     ▐█                       ▜▌
                     ▐█                       █▛
                     ▐█                       ▟▙
                     ▐█                     ▄▄█▙▄▄
                     ▐█                  ▗▟▛▀    ▀█▙
                     ▐█                 ▗█▀        ▜█
                     ▐█                 ▟▛         █▙
                     ▐█                 █▌   X   X  ▜█
                     ▐█                 █▙          █▌
                     ▐█                 ▝█▖        ▐█
                     ▐█                  ▀█▄      ▄█▘
                     ▐█                   ▝▀█▄▄▄▟▛▀
                     ▐█                       █▙
                     ▐█              ▗▄       ▟▌
                     ▐█              ▀██▄▖    ▜▛    ▗▟█▛▘
                     ▐█                ▀██▄▖  █▙  ▗▟█▛▘
                     ▐█                  ▝██▙▖▟▌▗▟█▛▘
                     ▐█                    ▝▜████▛▘
                     ▐█                      ▝█▛▘
                     ▐█                       ▜▙
                     ▐█                       █▌
                     ▐█                       ▜▛
                     ▐█                       █▙
                     ▐█                       ▟▌
                     ▐█                       █▛
                     ▐█                       ▟▙
                     ▐█                       ▜▌
                     ▐█                       █▛
                     ▐█                       ▟▙
                     ▐█                      ▟██
                     ▐█                     ▄█▘█▌
                     ▐█                    ▗█▘ ▝█▖
                     ▐█                   ▗█▀   ▜▙
                     ▐█                  ▗█▛    ▝█▖
                     ▐█                 ▗█▛      ▜█ ▗▟▖
                     ▐█            ▀██▙▄█▛        █▙█▀
                     ▐█              ▝▀▀▀         ▝▛▘
                     ▐█
                     ▐█
                     ▐█
  ▗▄▄▄▙▄▄▄▙▄▄▄▙▄▄▄▙▄▙██▟▟▄▙▙▟▟▄▙▙▟▄▙▟▄▄▄▄▄

   '''

print(boneco)

# Chamada da função principal para executar o jogo.
jogo_da_forca()
