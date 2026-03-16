 #Verificador de senha:
print("Página de cadastro")
nome = input("Nome: ")
email = input("Email: ")

if "@" in email:
     print("Email válido: ")
else:
     print("Email inválido ")



senha = str(input("Senha: "))
confirmação = str(input("Confirme sua senha: "))
if confirmação == senha:
     print("Senha válida")
else:
      print("Senha inválida")


if len(senha) >= 12:
     print("Senha forte")
elif len(senha) >= 10:
     print("Senha média")
elif len(senha) >= 8:
     print("Senha válida")
     print("Senha fraca")
else:
     print("Sua senha deve ter pelo menos 8 caractéres")
     print("Digite uma nova senha")
     senha = (input(":"))