import random


def imprime_abertura():
    print("*********************************")
    print("***Bem-vindo ao Jogo da Forca!***")
    print("*********************************")


def cria_palavra_secreta(nome_arquivo = "palavras.txt"):
    arquivo = open(nome_arquivo, "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()

    # vai gerar um numero randomico correspondente ao numero de palavras, o numero corresponde ao indice
    numero = random.randrange(0, len(palavras))
    # a variavel recebe a palavra correspondente ao indice sorteado
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta


    print(letras_acertadas)


def inicializa_letras_acertadas(palavra):
    # expressão dentro da lista para contar as letras da palavra secreta
    return ["_" for letras in palavra]


def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    posicao = 0
    return chute


def marca_chute_correto(chute,letras_acertadas,palavra_secreta):
    posicao = 0
    for letra in palavra_secreta:
        if (chute == letra):
            letras_acertadas[posicao] = letra
        posicao = posicao + 1


def imprime_mensagem_ganhador():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def imprime_mensagem_perdedor(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_letras_faltando(letras_acertadas):
    letras_faltando = str(letras_acertadas.count("_"))
    return print(f"Ainda faltam acertar {letras_faltando} letras")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

def jogar():

    imprime_abertura()

    palavra_secreta = cria_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    imprime_letras_faltando(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    #enquanto não enforcou e não acertou
    while(not enforcou and not acertou ):

        chute = pede_chute()

        #verificar se a letra escolhida consta na palavra secreta
        if(chute in palavra_secreta):
            marca_chute_correto(chute,letras_acertadas,palavra_secreta)
        else:
            erros = erros + 1
            desenha_forca(erros)

        #quando enforcou atinge o numero de tentativas definia ele muda para True
        enforcou = erros == 7
        #quando não tiver mais "_" na variavel letras_acertada o acertou muda para True
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    #laço para acabar o jogo
    if(acertou):
        imprime_mensagem_ganhador()
    else:
        imprime_mensagem_perdedor(palavra_secreta)

    

if(__name__ == "__main__"):
    jogar()