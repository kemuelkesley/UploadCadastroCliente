print("=====================Cadastro de clientes versão 1.0===================")
print()
nome = str(input("Informe seu nome :"))
idade = int(input("Informe sua idade :"))
nascimento = int(input("Informe seu ano de nascimento :"))
digi_cpf = input("Informe seu CPF sem espaços :")

print("confira as informações.")
print()
print("nome :",nome)
print("idade :",idade)
print("nascimento:",nascimento)
print("cpf :",digi_cpf)


cpf = "{}.{}.{}-{}".format(digi_cpf[:3], digi_cpf[3:6], digi_cpf[6:9], digi_cpf[9:])
print(cpf)

