## Programa de lançamento de moeda (cara e coroa) em Python 

import random
import re

print("Jogo de Cara ou Coroa")
print()
cara_ou_coroa = {"cara": 0, "coroa": 1}

def gerar_resultado():
    return random.choice(list(cara_ou_coroa.values()))  

def validar_entrada(escolha):
    return escolha in ["0", "1"]

vitorias = 0
derrotas = 0

while True:
    moeda = gerar_resultado()
    escolha = input("Escolha [0] para cara ou [1] para  coroa: ")

    if not validar_entrada(escolha):
        print("Erro: Digite apenas 0 ou 1")
        break
    
    escolha = "cara" if escolha == "0" else "coroa"

    if moeda == cara_ou_coroa[escolha]:
        print(f"Caiu {escolha}, você ganhou!")
        vitorias += 1
        print(f"Vitórias: {vitorias}, Derrotas: {derrotas}")
    else:
        print(f"Caiu {list(cara_ou_coroa.keys())[list(cara_ou_coroa.values()).index(moeda)]}, você perdeu!")
        derrotas += 1
        print(f"Vitórias: {vitorias}, Derrotas: {derrotas}")

    jogar_novamente = input("Deseja jogar novamente? (s/n): ")
    if jogar_novamente.lower() == "s":
        continue
    else:
        break

