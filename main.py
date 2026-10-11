print("=== VALIDADOR DE CADASTRO ===")
print("\n 1- Validar Email \n 2- Validar CPF \n 3- Sair")

r = int(input("Ação: "))

while True:

    if r == 1:
        email = input("Digite o seu Email: ").lower()
        if email.count("@") != 1:
            print("❌ Erro: O email precisa ter somente um @.")
        elif " " in email:
            print("❌ Erro: o email não pode conter espaços ")
        else:
            usuario, dominio = email.split("@")

            if usuario == " " or dominio == " ":
                print("❌ Erro: Falta o usuário ou domínio.")

            elif "." not in dominio:
                print("❌ Erro: o domínio precisa conter um ponto.")

            elif ".." in usuario or dominio:
                print("❌ Erro: O Email não pode ter dois pontos seguidos.")

            elif dominio.startswith(".") or dominio.endswith("."):
                print("❌ Erro: o domínio não pode começar e nem terminar com um ponto.")

            elif usuario.startswith(".") or usuario.endswith("."):
                print("❌ Erro: O usuário não pode começar nem terminar com um ponto.")

            else:
                print("✅ Formato aprovado nas verificações básicas.")


    elif r == 2:
        cpf = input("Digite o seu CPF: ")
        cpf = cpf.replace(".", "").replace("-", "")

        if len(cpf) == 11 and cpf.isdigit():
            print("✅ Formato inicial válido!")

            if cpf == cpf[0] * 11:
                print("✅ Formato Inválido!")

            else:
                soma = 0
                posicao = 0
                peso = 10

                while posicao < 9:
                    soma = soma + int(cpf[posicao]) * peso
                    posicao = posicao + 1
                    peso = peso -1

                print("Soma: ", soma)

                resto = soma % 11

                if resto < 2:
                    primeiro_digito = 0
                else:
                    primeiro_digito = 11 - resto

                print("Primeiro digito verificador: ", primeiro_digito)

                if primeiro_digito != int(cpf[9]):
                    print("❌ CPF inválido: primeiro dígito incorreto.")

                else:
                    print("✅ Primeiro dígito correto!")

                    soma = 0
                    posicao = 0
                    peso = 11

                    while posicao < 10:
                        soma = soma + int(cpf[posicao]) * peso
                        posicao = posicao + 1
                        peso = peso - 1

                    print("Segunda soma: ", soma)

                    resto = soma % 11

                    if resto < 2:
                        segundo_digito = 0
                    else:
                        segundo_digito == 11 - resto

                    if segundo_digito == int(cpf[10]):
                        print("✅ CPF Válido nos cálculos dos digitos verificadores!")
                    else:
                        print("❌ CPF inválido: segundo dígito incorreto.")

        else:
            print("❌ Erro: o CPF precisa ter 11 dígitos.")

    else:
        print("Saindo do sistema...")
        break




            

            