#ex1
while True:
    print("Olá, mundo")
    jogar = input("Deseja exibir a mensagem novamente? (sim/não) ")
    if jogar.lower() == "não":
        print("Fim")
        break
print("=======================================================================================================")
#ex2
for x in range (0,110, 10):
    print(x)

print("=======================================================================================================")
#ex3
n = int(input("Digite um número inteiro positivo: "))

while n <= 0:
    print("Valor inválido! Digite um número inteiro POSITIVO.")
    n = int(input("Digite um número inteiro positivo: "))

soma = 0

for i in range(1, n + 1):
    soma += i

print(f"A soma de 1 até {n} é: {soma}")