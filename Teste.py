print("Ola mundo")
print("Este é um teste de código em Python.")
while True:
    print("Digite 'sair' para encerrar o programa.")
    user_input = input("Digite algo: ")
    if user_input.lower() == "sair":
        print("Encerrando o programa...")
        break
    else:
        print(f"Você digitou: {user_input}")
