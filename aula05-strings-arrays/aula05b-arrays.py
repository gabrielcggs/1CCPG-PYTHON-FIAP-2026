lista_frutas = ["Banana","Maçã", "Morango"]

# lista_frutas[0] = "Banana"
# lista_frutas[1] = "Maçã"
# lista_frutas[2] = "Morango"
print(lista_frutas[1:3])

lista_frutas.append("Pera")
print(lista_frutas)

qtd_frutas = len(lista_frutas)
print("Qtde de frutas: ", qtd_frutas)

# FOR INDEXADO para PERCORRER
for i in range(qtd_frutas):
    print(lista_frutas[i])

print()

# FOR EACH em Python
for fruta in lista_frutas:
    print(fruta)

numeros = [0, 5, 11, 4]
for numero in numeros:
    print(numero)