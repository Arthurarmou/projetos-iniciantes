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
numeroadv = randint(1,10)
ultimonum = 0
chances = 5
tentativas = 0
print("insira o número inteiro para adivinhação em baixo (número entre 0 e 10):")
while True:
    if chances == 0:
        print("acabou o jogo, suas chances chegaram a 0")
        continuar = input("você deseja continuar?. Se sim digite sim:").lower().strip()
        if continuar == "sim" or continuar =="si" or continuar =="s":
            chances += 5
            tentativas = 1
            numeroadv = randint(1, 10)
            continue
        else:
            print("fechando...")
            break
    escolha = lernumero()
    if escolha > 10 or escolha < 1:
        print(f"está incorreto insira um número entre 0 e 10 e não: {escolha}")
        continue
    if escolha == ultimonum: #para verificar se o último número é igual 
        print("o número inserido está incorreto tem que ser diferente do último!")
        continue

    ultimonum = escolha

    if escolha > numeroadv:
        print(f"o número é menor que {escolha}")
        chances -= 1
        tentativas += 1
        if chances != 0:
            print(f"você ainda tem {chances} chances")
        continue
    elif escolha < numeroadv:
        print(f"o número é maior que {escolha}")
        chances -= 1
        tentativas +=1
        if chances != 0:
            print(f"você ainda tem {chances} chances")
        continue
    else:
        tentativas += 1
        print(f"o número está correto!: {escolha}, você acertou em {tentativas} tentativas!")
        chances = 5
        tentativas = 0
        numeroadv = randint(1, 10)
    continuar = input("insira se deseja continuar:").lower().strip()
    if not continuar == "sim" or continuar =="si" or continuar =="s":
        print("fechando o programa...")
        break
