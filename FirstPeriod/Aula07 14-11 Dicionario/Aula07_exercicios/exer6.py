#--- Exercicio 1  - Variávies e impressão com interpolacão de string
#--- Crie 5 variávies para armazenar os dados de um funcionário
#--- Funcionario: Nome, Sobrenome, Cpf, Rg, Salário
#--- Os dados devem ser impressos utilizando a funcao format()
#--- Deve ser usado apenas uma vez a função print(), porem os dados devem ser apresentados um em cada linha
#--- O salario deve ser de tipo flutuante e na impressão deve apesentar apenas duas casas após a vírgula

Nome = input('Digite o nome:')
Sobrenome = input('Digite o Sobrenome:')
Cpf = input('Digite o cpf:')
Rg = input('Digite o rg:')
Salário = float(input('Digite o Salario:'))

print(f'Funcionario: {Nome}{Sobrenome}\nCPF:{Cpf}\nRG:{Rg}\nSalario: R${Salário:.2f}')

