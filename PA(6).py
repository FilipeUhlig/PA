"""
Programa: Progressão aritmética
Descrição: Este programa calcula o n-ésimo termo e a soma dos termos de uma PA.
Autor: Filipe
Data: 04/06/2023
Versão: 0.0.1
"""
#Atribuição de variáveis

#Entrada de dados
n = float(input("Qual a quantidade de termos? "))
a1 = float(input("Qual o primeiro termo? "))
r = float(input("Qual a razão da progressão? "))

#Processamento de dados
an = ((a1 + (n-1))*r)
sn = (((a1 + an)/2)*n)

#Saida de dados
print(f"O n-ésimo termo é {an}.")
print(f"A soma dos n-ésimos termos é {sn}.")
