from functions import *
from dic import *


# na function forca_opcao, colocar para que a funcao depois de pedir o input, considere o value da chave
mensagem = forca_opcao("Bem vindo ao seu task manager, o que desejar fazer:", opcoes_menu)

acoes(mensagem)