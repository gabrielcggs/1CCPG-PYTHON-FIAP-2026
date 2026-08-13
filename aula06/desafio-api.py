endpoints = ["/login", "/produtos", "/pedidos"]
status = [
[200, 200, 401, 200, 500],
[200, 200, 200, 200, 200],
[201, 500, 502, 201, 500]
]
'''
print(endpoints[0])
print(status[0])
'''
# FUNÇÃO QUE VERIFICA SE UM STATUS CODE HTTP É SUCESSO
# 200-299 = SUCESSO
def sucesso(codigo):
    return codigo >= 200 and codigo < 300

# print(sucesso(status[0][0]))

# FUNÇÃO QUE VAI DETECTAR 2 ERROS SEGUIDOS NOS CÓDIGOS HTTP DE UM ENDPOINT
# [200, 200, 401, 200, 500] --> /login >> False
# [201, 500, 502, 201, 500] --> /pedidos >> True

def erros_seguidos(codigos_http):
    for i in range(len(codigos_http) - 1):
        codigo_atual = codigos_http[i]
        prox_codigo = codigos_http[i + 1]

        if not sucesso(codigo_atual) and not sucesso(prox_codigo):
            return True
    return False

#print(erros_seguidos(status[2]))

# [200, 200, 401, 200, 500] --> /login
# [201, 500, 502, 201, 500] --> /pedidos
def analisar_endpoint(codigos_http):
    qtd_sucesso = 0

    for codigo in codigos_http:
        if sucesso(codigo):
            qtd_sucesso += 1

    qtd_requisicoes = len(codigos_http)
    qtd_erros = qtd_requisicoes - qtd_sucesso

    percentual_sucesso = (qtd_sucesso / qtd_requisicoes) * 100

    tem_erros_seguidos = erros_seguidos(codigos_http)

    if tem_erros_seguidos:
        classificacao = "CRÍTICO"
    elif percentual_sucesso >= 80:
        classificacao = "ESTÁVEL"
    else:
        classificacao = "INSTÁVEL"

    return (qtd_sucesso, qtd_erros, percentual_sucesso, classificacao)

#print(analisar_endpoint(status[2]))

# PERCORRENDO TODA A MATRIZ
maior_qtd_de_erros = -1
endpoint_maior_qtd_de_erros = ""

for i in range(len(endpoints)):
    nome_endpoint = endpoints[i]
    codigos_endpoint = status[i]

    sucessos, erros, percentual, classificacao = analisar_endpoint(codigos_endpoint)

    print(f"Endpoint: {nome_endpoint}")
    print(f"Codigos HTTP: {codigos_endpoint}")
    print(f"Sucessos: {sucessos}")
    print(f"Erros: {erros}")
    print(f"% de sucesso: {percentual:.1f}%")
    print(f"Classificacao: {classificacao}")
    print("-" * 30)
    print()

    if erros > maior_qtd_de_erros:
        maior_qtd_de_erros = erros
        endpoint_maior_qtd_de_erros = nome_endpoint
    elif erros == maior_qtd_de_erros:
        endpoint_maior_qtd_de_erros += nome_endpoint

print(f"Endpoint(s) com mais erros: {endpoint_maior_qtd_de_erros}")