#--- Exercicio 4  - Input, Estrutura de decisão e operações matemáticas
#--- Crie um programa que realize a autenticação de usuário
#--- Crie duas variáveis para conter o usuário e senha padrão do sistema
#--- Leia o usuário e senha informados pelo usuário via função input()
#--- Valide se usuário e senha estão corretos
#--- Caso o usuário e senha estejam corretos informe com mensagem de boas vindas
#--- Caso o usuário e senha estejam incorretos informe com mensagem de falha de login

userNew = input('Digite seu novo Usuario: ')
senhaNew = input('Digite sua nova senha: ')

user = input('Digite seu novo Usuario novamente: ')
senha = input('Digite sua nova senha novamente: ')

if userNew == user and senhaNew == senha:
    print(f'Bem vindo {user}')
else:
    print('Falha no login')

    