from random import randint
def lernumero():
    while True:
        escolha = input("insira o número: ")
        try:
            numero = int(escolha)
            return numero
        except:
            print("você não inseriu um número inteiro:")
            continue
numeroadv = randint(1,10) #botando as randons para os números
ultimonum = 0
chances = 5
tentativas = 0
print("insira o número inteiro para adivinhação em baixo (número entre 1 e 10):")
while True:
    if chances == 0: #se as chances acabarem o jogo acaba também
        print("acabou o jogo, suas chances chegaram a 0")
        continuar = input("você deseja continuar?. Se sim digite sim:").lower().strip() #opção para continuar a jogar
        if continuar == "sim" or continuar == "si" or continuar == "s":
            chances = 5 #resetando as coisas para um novo jogo
            tentativas = 0 #resetando as coisas para um novo jogo
            numeroadv = randint(1, 10) #rodando os números de novo para não ser o mesmo antigo
        else:
            print("fechando o programa...")
            break

    escolha = lernumero() #escolha atribuida à uma func para validar apenas números

    if escolha > 10 or escolha < 1: #se a escolha for maior do que o randint pede para validar de novo
        print(f"está incorreto insira um número entre 1 e 10 e não: {escolha}")
        continue
    if escolha == ultimonum: #para verificar se o último número é igual 
        print("o número inserido está incorreto tem que ser diferente do último número inserido!")
        continue

    ultimonum = escolha #atribuida a escolha para ir sempre resetando conforme a pessoa vai digitando. O if está em cima dele pois sempre daria verdadeiro se botasse abaixo

    if escolha > numeroadv: #para ajudar a pessoa que está adivinhando o número
        print(f"o número é menor que {escolha}")
        chances -= 1
        tentativas += 1
        if chances != 0: #mostrar quantas chances a pessoa tem
            print(f"você ainda tem {chances} chances!")
        continue
    elif escolha < numeroadv: #para ajudar a pessoa que está adivinhando o número
        print(f"o número é maior que {escolha}")
        chances -= 1
        tentativas +=1
        if chances != 0: #mostrar quantas chances a pessoa tem
            print(f"você ainda tem {chances} chances")
        continue
    else:
        tentativas += 1 #adicionando uma tentativa,pois tentativa é 0, ou seja não tem como a pessoa acertar a resposta em 0 tentativas
        if tentativas == 1: #única coisa que muda do else de baixo é o print, coloca tentativas no singular. Pois não tem como a pessoa acertar em 1 tentativaS
            print(f"o número está correto!: {escolha}, você acertou em {tentativas} tentativa!")
        else:
            print(f"o número está correto!: {escolha}, você acertou em {tentativas} tentativas!")
    continuar = input("insira se deseja continuar:").lower().strip() #input para ver se a pessoa quer continuar
    if continuar == "sim" or continuar =="si" or continuar =="s": #se sim continua o programa para um novo jogo
        chances = 5  # resetando as coisas para um novo jogo
        tentativas = 0  # resetando as coisas para um novo jogo
        numeroadv = randint(1, 10)  # rodando os números de novo para não ser o mesmo
    else: #se não fecha o programa
        print("fechando programa...")
        break
