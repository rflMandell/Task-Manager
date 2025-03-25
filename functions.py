from dic import *

def forca_opcao(msg,opcoes):
    possibilidades = '\n'.join(opcoes)
    opcao = input(f"{msg}\n{possibilidades}\n->")
    while opcao not in opcoes:
        print('Opção invalida')
        opcao = input(f"{msg}\n{possibilidades}\n->")
    return opcao

def acoes(opcao):
    if opcao == "1":
        print()
    elif opcao == "2":
        print()
    elif  opcao == "3":
        print()
    else:
        print()