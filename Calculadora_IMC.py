import time
print("Bem vindo a calculadora de IMC.")
print("Qual a sua altura?")
altura = float(input())

print("Qual o seu peso?")
peso = float(input())

print("Calculando.....")
print("===============")
time.sleep(1)
print("Seu IMC é: {:.2f}".format(peso / altura**2))
