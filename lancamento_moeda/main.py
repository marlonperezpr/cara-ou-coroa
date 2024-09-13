## Programa de lançamento de moeda (cara e coroa) em Python 

import random
import re

print("Jogo de Cara ou Coroa")
print()
cara_ou_coroa = [0, 1]
resultado = random.choice(cara_ou_coroa)

while True:
    if resultado == 0:
        resultado = "cara"
    elif resultado == 1:
        resultado = "coroa"

    escolha = input("Escolha [0] para cara ou [1] para  coroa: ")
    if re.match("^[01]$", escolha):
        if escolha == "0":
            escolha = "cara"
        elif escolha == "1":
            escolha = "coroa"
    else:
        print("Erro: Digite apenas 0 ou 1")
        break

    if resultado == escolha:
        print(f"Caiu {resultado}, você ganhou!")
        break
    else:
        print(f"Caiu {resultado}, você perdeu!")
        

