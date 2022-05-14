import random #para importar a biblioteca do random

def jogar():

    print("*********************************")
    print("Bem-vindo ao jogo de Adivinhação!")
    print("*********************************")

    #Variáveis
    numero_secreto = random.randrange(1,101) #função random gera um numero aleatório de 0.0 a 1.0 por isso o randrange
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina o nível: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    for rodada in range(1,total_de_tentativas + 1):
    #while(rodada <= tal_de_tentativas): #tudo no while repete até a condição ser satisfeita
        #forma de printar 1
        #print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        #forma de printar 2
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ") #entrada de dados
        print ("Você digitou", chute_str)
        chute = int(chute_str) #conversão de string para int

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue #pula para a próxima interação

        acertou = chute == numero_secreto #abreviação das condições if
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if (acertou):
            print (f"Você acertou e fez {pontos} pontos! Parabéns!")
            break #sai do bloco do laço abruptamente
        else:
            if(maior):
                print("Você errou! O seu chute foi maior que o número secreto")
            elif(menor):
                print("Você errou! O seu chute foi menor que o número secreto.")
            if(rodada == total_de_tentativas):
                print(f"O número secreto era {numero_secreto}. Você fez {pontos} pontos")
            pontos_perdidos = abs(numero_secreto - chute) #subtrai o valor do chute dos pontos
            pontos = pontos - pontos_perdidos
        #rodada = rodada + 1 #sempre que a rodada acaba adiciona mais 1 no valor da variável

    print("Fim do jogo!")

if(__name__ == "__main__"): #esse laço serve para executar a função jogar ao escrever o nome do arquivo no terminal
    jogar()