#!/usr/bin/env python
# coding: utf-8

# 1  -----------------------

idade_dias = int(input("Digite sua idade em dias: "))

anos = idade_dias/365
meses = idade_dias/30
dias = idade_dias

print(f'A sua idade em anos é: {anos:.0f}; em meses:{meses:.0f}; e em dias: {dias}')


# 2  -----------------------

a = int(input("Digite o Valor de a: "))
b = int(input("Digite o Valor de b: "))
c = int(input("Digite o Valor de c: "))

p = (a+b+c)/2

if a > (b+c):
    print(f'Não é um triangulo: {a}, {b}, {c}')
else:
    s = (p*(p-a)*(p-b)*(p-c))**0.5
    print(f'A área do triângulo é {s}')




# 3  -----------------------

lista = []
for x in range(1, 4):
    n = input(f"Digite o {x}° número: ")
    lista.append(int(n))
print(f'O menor número digitado foi: {min(lista)}')




# 4  -----------------------

def primo(x):
    if x==0 or x==1:
        return False
    for num in range(2,x+1):
        if x%num==0 and x!=num:
            return False
    return True

for x in range(101):
    if primo(x):
        print(x, 'é primo')
    else:
        print(x,'não é primo')



# 5  -----------------------
def inverter(frase):
    return frase[::-1]

inverter('Está frase será invertida')

