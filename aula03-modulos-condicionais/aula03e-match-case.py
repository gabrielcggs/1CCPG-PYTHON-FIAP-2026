# escolha do usuário
# 0 --> sair do programa
# 1 --> entrar no programa
# ----> erro!

escolha_usuario = 1545

match escolha_usuario:
    case 0:
        print("Sair do programa")
    case 1:
        print("Entar no programa")
    case _:
        print("Erro!!")