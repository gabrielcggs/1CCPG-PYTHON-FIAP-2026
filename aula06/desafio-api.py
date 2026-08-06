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

print(sucesso(status[0][0]))