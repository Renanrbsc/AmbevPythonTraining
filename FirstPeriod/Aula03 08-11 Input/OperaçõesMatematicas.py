print('~'*35)
newName = input('Digite seu Nome: ')
newLastname = input('Digite o sobrenome: ')
idade = int(input('Digite sua idade: '))
tamanho = input('Digite seu tamanho: ')
peso = input('Digite seu peso: ')
estado = input('Digite seu estado: ')

print('~'*35)

name = input('Digite seu Nome: ')


if name == newName:
    print('Acesso Permitido')
else: 
    print('Acesso Negado')

print('~'*35)

print(f'Seu nome completo é: {newName} {newLastname}')
print('Sua idade é: ',idade)
print('Seu tamanho é: ',tamanho)
print('Seu peso é: ',peso)
print('Seu estado é: ',estado)

print('~'*35)

if idade < 18:
    print('Não pode usar o Mercado Tech, para o que presta.')
else:
    print('Pode usar o Mercado Tech e chapar o coco')

