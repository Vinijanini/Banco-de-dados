import sqlite3
import time

banco = sqlite3.connect('banco_dados.db') #cria banco de dados#
cursor = banco.cursor() #conecta o cursor#

cursor.execute("CREATE TABLE IF NOT EXISTS dados_1 (dados text)")
cursor.execute("CREATE TABLE IF NOT EXISTS dados_2 (dados text)")
cursor.execute("CREATE TABLE IF NOT EXISTS dados_3 (dados text)")

#Define as listas#
lista1 = []
lista2 = []
lista3 = []

#Insere os dados das tabelas nas listas
cursor.execute('SELECT * FROM dados_1')
for c in cursor.fetchall():
    for c2 in c:
        lista1.append(c2)
cursor.execute('SELECT * FROM dados_2')
for c in cursor.fetchall():
    for c2 in c:
        lista2.append(c2)
cursor.execute('SELECT * FROM dados_3')
for c in cursor.fetchall():
    for c2 in c:
        lista3.append(c2)

#Variáveis globais#
cont = "s"

#Funções#
def lin():
    print('=-' * 10)

#Programa principal#
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

    #Tratamento de erro#
    while n1 == "4" and len(lista1 + lista2 + lista3) <= 0:
        print("Impossivel, todas as pastas estão limpas")
        break
    while n1 == "5" and len(lista1 + lista2 + lista3) <= 0:
        print("Impossivel, todas as pastas estão limpas")
        break
    while n1 not in ('1','2','3','4','5','6'):
        print('Erro!')
        n1 = str(input("Qual pasta deseja inserir dados:"))

    #Adicionar dado na pasta1#
    while n1 == "1":
        print('Entrando na pasta 1...')
        time.sleep(1.3)
        while cont == 's':
            n2 = input('Informação a armazenar>>>>>>')
            lista1.append(n2)

            cursor.execute("INSERT INTO dados_1 VALUES('" +n2+ "')")
            banco.commit()

            cont = (str(input('Continuar[s/n]:'))).lower()

            #Tratamento de erro#
            while cont not in ('s', 'n'):
                print('Erro!')
                cont = (str(input('Continuar[s/n]:'))).lower()
            if cont != "s":
                break
        break

    #Adiciona dado na pasta2#
    while n1 == "2":
        print('Entrando na pasta 2...')
        time.sleep(1.3)
        while cont == 's':
            n2 = input('Informação a armazenar>>>>>>')
            lista2.append(n2)
            cursor.execute("INSERT INTO dados_2 VALUES('" + n2 + "')")
            banco.commit()
            cont = (str(input('Continuar[s/n]:'))).lower()
            while cont not in ('s','n'):
                print('Erro!')
                cont = (str(input('Continuar[s/n]:'))).lower()
            if cont != "s":
                break
        break

    # Adiciona dado na pasta3#
    while n1 == "3":
        print('Entrando na pasta 3...')
        time.sleep(1.3)
        while cont == 's':
            n2 = input('Informação a armazenar>>>>>>')
            lista3.append(n2)

            cursor.execute("INSERT INTO dados_3 VALUES('" + n2 + "')")
            banco.commit()

            cont = (str(input('Continuar[s/n]:'))).lower()
            while cont not in 'sn':
                print('Erro!')
                cont = (str(input('Continuar[s/n]:'))).lower()
            if cont != "s":
                break
        break

    #Apagar dado#
    while n1 == "4" and len(lista1+lista2+lista3) >= 1:

        apag = '0'
        while apag not in ("1", "2", "3"):
            apag = str(input('De qual pasta você deseja apagar um dado?:'))
            if apag not in ('1', '2', '3'):
                print(f'"{apag}" Não é uma pasta!')

        while apag == "2" and len(lista2) == 0 or apag == "1" and len(lista1) == 0 or apag == "3" and len(lista3) == 0:
            print('Essa pasta está vazia!')
            apag = str(input('De qual pasta você deseja apagar um dado?:'))


        if apag == "1":
            while True:
                itemapag = int(input(f'Qual item apagar de 1/{len(lista1)}:'))
                while itemapag not in range(1, len(lista1)+1):
                    print('Opção inválida!')
                    itemapag = int(input(f'Qual item apagar de 1/{len(lista1)}:'))
                while len(lista1) < itemapag:
                    print('Essa pasta não tem esse número de dados')
                    itemapag = int(input('Qual item apagar:'))

                dado_apagar = lista1[itemapag - 1]
                cursor.execute("DELETE from dados_1 WHERE dados = '" + dado_apagar + "'")
                banco.commit()
                del lista1[itemapag - 1]

                print(f'Lista 1 agora {lista1}')
                if len(lista1) == 0:
                    break

                cont = str(input('Continuar[s/n]:')).lower()
                while cont not in ("s","n"):
                    print('Erro!')
                    cont = str(input('Continuar[s/n]:')).lower()
                if cont == "n":
                    break

        if apag == "2":
            while True:
                itemapag = int(input(f'Qual item apagar de 1/{len(lista2)}:'))
                while itemapag not in range(1, len(lista2) + 1):
                    print('Opção inválida!')
                    itemapag = int(input(f'Qual item apagar de 1/{len(lista2)}:'))
                while len(lista2) < itemapag:
                    print('Essa pasta não tem esse número de dados')
                    itemapag = int(input('Qual item apagar:'))

                dado_apagar = lista2[itemapag - 1]
                cursor.execute("DELETE from dados_2 WHERE dados = '" + dado_apagar + "'")
                banco.commit()
                del lista2[itemapag - 1]

                if len(lista2) == 0:
                    break
                print(f'Lista 2 agora {lista2}')
                cont = str(input('Continuar[s/n]:')).lower()
                while cont not in ('s','n'):
                    print('Erro!')
                    cont = str(input('Continuar[s/n]:')).lower()
                if cont == "n":
                    break

        if apag == "3":
            while True:
                itemapag = int(input(f'Qual item apagar de 1/{len(lista3)}:'))
                while itemapag not in range(1, len(lista3) + 1):
                    print('Opção inválida!')
                    itemapag = int(input(f'Qual item apagar de 1/{len(lista3)}:'))
                while len(lista3) < itemapag:
                    print('Essa pasta não tem esse número de dados')
                    itemapag = int(input('Qual item apagar:'))

                dado_apagar = lista3[itemapag - 1]
                cursor.execute("DELETE from dados_3 WHERE dados = '" + dado_apagar + "'")
                banco.commit()
                del lista3[itemapag - 1]

                if len(lista3) == 0:
                    break
                print(f'Lista 3 agora {lista3}')
                cont = str(input('Continuar[s/n]:')).lower()
                while cont not in ('s','n'):
                    print('Erro!')
                    cont = str(input('Continuar[s/n]:')).lower()
                if cont == "n":
                    break
        if cont == "n":
            break

    #Limpar pasta#
    if n1 == "5" and len(lista1+lista2+lista3) >= 1:
        while True:
            print('Digite "V" para voltar')
            limp = str(input('Qual pasta deseja limpar:'))
            if limp in 'Vv':
                break
            while limp not in ("1","2","3"):
                print(f'Erro! "{limp}" não é uma pasta"')
                print('Cancelando')
                break
            if limp == "1":
                cursor.execute('DELETE FROM dados_1')
                banco.commit()
                lista1.clear()
            if limp == "2":
                cursor.execute('DELETE FROM dados_2')
                banco.commit()
                lista2.clear()
            if limp == "3":
                cursor.execute('DELETE FROM dados_3')
                banco.commit()
                lista3.clear()
            break

    cont = "s"

    #Sair do programa#
    if n1 == "6":
        print('Um banco_de_dados.txt foi criado para salvar as informações')
        time.sleep(1.3)
        print('Programa finalizado!')
        break
with open("banco_de_dados.txt", "w") as aqr:
    aqr.write(f"[Pasta 1] = {lista1}\n")
    aqr.write(f"[Pasta 2] = {lista2}\n")
    aqr.write(f"[Pasta 3] = {lista3}\n")