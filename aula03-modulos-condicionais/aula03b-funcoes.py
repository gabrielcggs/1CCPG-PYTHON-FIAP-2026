# FUNÇÃO SEM RETORNO SEM PARAM.
def print_lyrics():
    print("I ain't gonna live forever")
    print("I just want to live while I'm alive")

print_lyrics()

# FUNÇÃO SEM RETORNO COM PARAM.
def boas_vindas(nome):
        print(f"Olá, {nome}!! Seja bem-vindo")

nome_digitado = input("Digite seu nome: ")
boas_vindas(nome_digitado)

# FUNÇÃO COM RETORNO COM PARAM.
def soma(num_a, num_b):
    soma = num_a + num_b
    return soma

print(soma(10,5))
print(type(nome_digitado))