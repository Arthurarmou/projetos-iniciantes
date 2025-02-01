def lernumero():
    while True:
        escolha = input("insira o número da opções, 1 para adicionar contato 2 para remover e 3 para editar. Qualquer número maior ou menor fecha o programa:")
        try:
            numero = int(escolha)
            return numero
        except:
            print("você não inseriu um número inteiro")
            continue
def adicionar():
    while True:
        item = input("insira o contato que deseja adicionar:")
        while item == "":
            print("o item não pode ser vazio")
            item = input("insira o item novamente")
        lista.append(item)
        print("sua nova lista de contato é essa:",lista)
        continuar = input("você deseja continuar?:")
        if continuar == "sim":
            continue
        else:
            print("fechando...")
            break
def remover():
    while True:
        print(f"sua lista é:{lista}")
        if not lista:
            print(f"não tem lista de contato {lista},dito isso voltando para o menu...")
            break
        item = input("insira o contato que você deseja remover ou digite tudo para remover tudo:").strip()
        if item == "tudo" or item == "Tudo":
            lista.clear()
            print(f"voltando para o menu pois a lista de contato é vazia {lista}...")
            break
        while item not in lista:
            print(f"o contato:{item} não está na lista")
            item = input("insira o contato novamente")
        if item in lista:
            lista.remove(item)
            print(f"o contato removido foi:{item}")
            print(f"sua lista de contato é:{lista}")
            continuar = input("deseja continuar, se sim digite sim se não quiser digite não:")
            if continuar == "sim":
                continue
            else:
                print("fechando...")
                break
def editar():
    while True:
        print(f"sua lista é:{lista}")
        if not lista:
            print("voltando para o menu,pois não tem lista")
            break
        contato = input(f"insira o contato que você quer editar:")

        while contato not in lista:
            print("este contato não tem na lista")
            contato = input("insira o contato que você quer editar novamente:")
        if contato in lista:
            contatoedit = input("insira o nome do contato para substituir esse:")
            while contatoedit == contato:
                print("está errado!")
                contatoedit = input("insira um nome diferente para o contato:")
            index = lista.index(contato)
            lista[index] = contatoedit
            print(f"sua lista é:{lista}")
            continuar = input("você deseja continuar? digite sim para continuar:")

            if continuar == "sim":
                continue
            else:
                print("fechando...")
                break

lista = []
while True:
    menu = lernumero()

    if menu == 1:
        adicionar()
    elif menu == 2:
        remover()
    elif menu == 3:
        editar()
    else:
        print("fechando...")
        break