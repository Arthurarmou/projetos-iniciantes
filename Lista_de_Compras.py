def lernumero():
    while True:
        escolha = input("insira 1 para adicionar e 2 para remover ou um outro número para sair do programa: ")
        try:
            numero = int(escolha)
            return numero
        except ValueError:
            print("insira um número não símbolos ou letras!!")
            continue
def adicionar():
    while True:
        item = input("insira o item que deseja adicionar:")
        while item == "":
            print("o item não pode ser vazio")
            item = input("insira o item que deseja adicionar")
        lista.append(item)
        print(f"sua lista é: {lista}")
        continuar = input("insira se deseja continuar (sim), se quiser voltar para o menu digite não: ").lower().strip()
        if continuar == "não":
            print("fechando...")
            break
def remover():
    while True:
        if not lista:
            print("não tem item na lista")
            break
        item = input("insira o item que deseja remover ou se quiser remover tudo digite tudo:")
        if item == "tudo":
            lista.clear()
            print(f"sua lista agora está vazia:{lista}, voltando para o menu")
            break
        while item not in lista:
            print("o item não está na lista")
            item = input("insira o item que deseja remover ou se quiser remover tudo digite tudo:")
        if item in lista:
            lista.remove(item)
            print(f"o item: {item} foi removido")
            print("sua nova lista é:",lista)
            continuar = input("deseja continuar removendo?:")
            if continuar == "sim":
                continue

lista = []
while True:
    menu = lernumero()
    if menu == 1:
        adicionar()
    if menu == 2:
        remover()
    if menu >= 3 or menu <=0:
        print("fechando o programa")
        break
