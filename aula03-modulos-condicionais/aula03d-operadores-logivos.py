# LÓGICA E (and)

verifica_email = True
verifica_senha = False

login = verifica_email and verifica_senha
print(login)

if login:
    print("Entrar no programa")

# LÓGICA OU (or)
logica_ou = False or False or True
print(logica_ou)

# NEGAÇÃO (not)
negacao = not False
print(negacao)

if not login:
    print("loga certo aí")