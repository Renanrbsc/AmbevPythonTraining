# Aula 6 - 13-11-19
# reforço sobre if else
#If Else Elif

# If simples, valida apenas uma condição
id = 1
if id == 1:
    print('id é True')
print('')
print('')

# if else Valida como true or false, apenas as que atingirem as condiçoes
idade = 25
if (idade < 18): # a condiçao em parenteses é validada como false 
    print('Dimenor') 
elif (idade == 18): # a condiçao em parenteses é validada como false
    print('Vai pro quartel')
else:
    print('Dimaior') # não atingiu nenhuma condiçao, valida else como true
print('')
print('')

# if else em Boolean
ativo = True

if ativo:
    print('Logar')
else:
    print('Não pode')
print('Variavel ativo:')
print(type(ativo),f': {ativo}')
print('')
print('')

# valor em variave booleana
at = int(input('Digite 1 ou 0\n'))
validador = (at == 1 ) # retorna valor booleano
print(validador) # imprime valor booleano

if at == 1: # caso seja True
    print(type(validador),f': {validador}') # imprime o tipo da variavel e seu valor
else: # caso seja False
    print(type(validador),f': {validador}')
print('')
print('')


# teste de boolean em uma variavel inteira
a = 18

validador = (a == 18)
print(validador)
validador = (a != 18)
print(validador)
validador = (a > 18)
print(validador)
validador = (a < 18)
print(validador)
validador = (a >= 18)
print(validador)
validador = (a <= 18)
print(validador)
print('')
print('')

# operador not faz o valor contrario
validador = not True 
validador = not False 

sorteado= 'Marcela'
validador1 = (sorteado == 'Mateus' and sorteado == 'Marcela') # valida se todas entrarem nas condiçoes
validador2 = (sorteado == 'Mateus' or sorteado == 'Marcela') # valida uma das duas condiçoes
print(f'{sorteado} validador and:{validador1}\n{sorteado} validador or:{validador2}\n')

