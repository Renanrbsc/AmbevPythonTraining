#2 -
# Mercado Tech
# Solicitar Nome o funcionario 
# Solicitar idade
# Informar se o funcionario pode adquirir produto Alcoolico

#3 -
# Cadastro Produto Mercado Tech
#Solicitar nome do produto
# Solicitar a categoria do produto (Alcoolico e não alcoolicos)
# Exiir o produto cadastrado

#2 Mercado Tech

print('~'*70)
nome = input('Digite o Funcionario:\n')
idade = int(input('Digite a idade do Funcionario:\n'))
print('~'*70)
if idade < 18:
    print(f'Funcionario {nome}, Não pode consumir Bebida Alcoolica')
else:
    print(f'Funcionario {nome}, Pode consumir Bebida Alcoolica')
print('~'*70)



#3 Cadastro Produto Mercado Tech

prod = input('Digite o novo produto:\n')
categ = input('Digite a categoria do produto: (Alcoolico ou Não alcoolico)\n')
print('~'*70)
print(f'Novo Produto: {prod}\nCategoria: {categ}')
print('~'*70)




