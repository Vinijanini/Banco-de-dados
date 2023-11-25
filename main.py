import time
lista1 = []
lista2 = []
lista3 = []
cont2 = "s"
cont = "s"
n1 = "s"
def lin():
    print('=-' * 10)
while True:
    lin()
    print(f"[1] - {lista1}")
    print(f"[2] - {lista2}")
    print(f"[3] - {lista3}")
    print('[4] - apagar dados')
    print('[5] - limpar pasta')
    print('[6] - sair')
    lin()
    n1 = str(input('Qual pasta deseja inserir dados:'))
    while n1 == "4" and len(lista1 + lista2 + lista3) <= 0:
        print("Impossivel, todas as pastas estão limpas")
        break
    while n1 == "5" and len(lista1 + lista2 + lista3) <= 0:
        print("Impossivel, todas as pastas estão limpas")
        break
    if n1 == "6":
        print('Um banco_de_dados.txt foi criado para salvar as informações')
        time.sleep(1.3)
        print('Programa finalizado!')
        break
    while n1 not in '123456':
        print('Erro!')
        n1 = str(input("Qual pasta deseja inserir dados:"))
    while n1 == "1":
        print('Entrando na pasta 1...')
        time.sleep(1.3)
        while cont == 's':
            n2 = input('Informação a armazenar>>>>>>')
            lista1.append(n2)
            cont = (str(input('Continuar[s/n]:'))).lower()
            while cont not in 'sn':
                print('Erro!')
                cont = (str(input('Continuar[s/n]:'))).lower()
            if cont != "s":
                break
        break
    while n1 == "2":
        print('Entrando na pasta 2...')
        time.sleep(1.3)
        while cont == 's':
            n2 = input('Informação a armazenar>>>>>>')
            lista2.append(n2)
            cont = (str(input('Continuar[s/n]:'))).lower()
            while cont not in 'sn':
                print('Erro!')
                cont = (str(input('Continuar[s/n]:'))).lower()
            if cont != "s":
                break
        break
    while n1 == "3":
        print('Entrando na pasta 3...')
        time.sleep(1.3)
        while cont == 's':
            n2 = input('Informação a armazenar>>>>>>')
            lista3.append(n2)
            cont = (str(input('Continuar[s/n]:'))).lower()
            while cont not in 'sn':
                print('Erro!')
                cont = (str(input('Continuar[s/n]:'))).lower()
            if cont != "s":
                break
        break
    while n1 == "4" and len(lista1+lista2+lista3) >= 1:
        apag = str(input('De qual pasta você deseja apagar um dado?:'))
        while apag == "1" and len(lista1) == 0:
            print('Essa pasta está vazia!')
            apag = str(input('De qual pasta você deseja apagar um dado?:'))
        while apag == "2" and len(lista2) == 0:
            print('Essa pasta está vazia!')
            apag = str(input('De qual pasta você deseja apagar um dado?:'))
        while apag == "3" and len(lista3) == 0:
            print('Essa pasta está vazia!')
            apag = str(input('De qual pasta você deseja apagar um dado?:'))
        while apag not in ["1", "2", "3"]:
            print(f'Erro! "{apag}" não corresponde a uma pasta!')
            apag = str(input('De qual pasta você deseja apagar um dado?:'))
        while apag == "1":
            itemapag = int(input(f'Qual item apagar de 1/{len(lista1)}:'))
            while itemapag not in range(1, len(lista1)+1):
                print('Opção inválida!')
                itemapag = int(input(f'Qual item apagar de 1/{len(lista1)}:'))
            while len(lista1) < itemapag:
                print('Essa pasta não tem esse número de dados')
                itemapag = int(input('Qual item apagar:'))
            del lista1[itemapag-1]
            print(f'Lista 1 agora {lista1}')
            if len(lista1) == 0:
                break
            cont2 = str(input('Continuar[s/n]:')).lower()
            while cont2 not in "sn":
                print('Erro!')
                cont2 = str(input('Continuar[s/n]:')).lower()
            if cont2 == "n":
                break
        while apag == "2":
            itemapag = int(input(f'Qual item apagar de 1/{len(lista2)}:'))
            while itemapag not in range(1, len(lista2) + 1):
                print('Opção inválida!')
                itemapag = int(input(f'Qual item apagar de 1/{len(lista2)}:'))
            while len(lista2) < itemapag:
                print('Essa pasta não tem esse número de dados')
                itemapag = int(input('Qual item apagar:'))
            del lista2[itemapag-1]
            if len(lista2) == 0:
                break
            print(f'Lista 2 agora {lista2}')
            cont2 = str(input('Continuar[s/n]:')).lower()
            while cont2 not in "sn":
                print('Erro!')
                cont2 = str(input('Continuar[s/n]:')).lower()
            if cont2 == "n":
                break
        while apag == "3":
            itemapag = int(input(f'Qual item apagar de 1/{len(lista3)}:'))
            while itemapag not in range(1, len(lista3) + 1):
                print('Opção inválida!')
                itemapag = int(input(f'Qual item apagar de 1/{len(lista3)}:'))
            while len(lista3) < itemapag:
                print('Essa pasta não tem esse número de dados')
                itemapag = int(input('Qual item apagar:'))
            del lista3[itemapag-1]
            if len(lista3) == 0:
                break
            print(f'Lista 3 agora {lista3}')
            cont2 = str(input('Continuar[s/n]:')).lower()
            while cont2 not in "sn":
                print('Erro!')
                cont2 = str(input('Continuar[s/n]:')).lower()
            if cont2 == "n":
                break
        if cont2 == "n":
            break
    while n1 == "5" and len(lista1+lista2+lista3) >= 1:
        limp = str(input('Qual pasta deseja limpar:'))
        while limp not in "123":
            print(f'Erro! "{limp} não é uma pasta"')
        if limp == "1":
            lista1.clear()
        if limp == "2":
            lista2.clear()
        if limp == "3":
            lista3.clear
        break
    cont = "s"
with open("banco_de_dados.txt", "w") as aqr:
    aqr.write(f"[Pasta 1] = {lista1}\n")
    aqr.write(f"[Pasta 2] = {lista2}\n")
    aqr.write(f"[Pasta 3] = {lista3}\n")