pessoa = '\t maykon' ' ' 'granemann \n'

print('''aaaaaaaaaa
    aaaaaa
aaaaaaa''') # imprime varias linhas com um comando

print(len(pessoa)) # len - conta quantos caracters tem a variavel

print(pessoa.count('a')) # count - conta e busca quantos dados do parametro contem em determinada variavel

print(pessoa.lower()) # lower - Coloca tudo em minusculo

print(pessoa.upper()) # upper - Coloca tudo em maiusculo

print(pessoa.split(' ')) # split - separa a variavel em varios dados, transforma em um array, tira o caracter do parametro e o separa.

print(pessoa.strip().split('a')) 

print(pessoa.strip()) # strip - remove espaços no inicio e final de dados

print(pessoa.strip()) # strip - remove Espaços, Tabulação, Quebra linha no inicio e final de dados

print(pessoa.capitalize()) # capitalize - Coloca a primeira letra do conteudo em maiuscula

pessoa1 = [" ","Carinhoso","Atencioso","Querido"]
print(pessoa1)
print((' nem ').join(pessoa1)) # Array tem a ',' como delimitador, adiciona nem depois de cada dado

frase = 'Teti torrado'
print('a'.join(frase)) # String não tem delimitador, adiciona 'a' depois de cada caracter

print(pessoa1[:1]) # seleciona e imprime do primeiro elemento ate o parametro
print(pessoa1[1:]) # seleciona e imprime do ultimo elemento ate o parametro
print(pessoa1[1:3]) # seleciona os dados de posicao 1 ate posicao 3 e imprime
print(frase[5:]) # seleciona do ultimo ate o 5 caracter
print(frase[5:10]) # seleciona do 5 ao 10 caracter
print(frase[:4]) # seleciona do primeiro ao 4 caracter
print(pessoa1.count("Carinhoso")) # verifica quantos do conteudo na variavel
print(pessoa1.count(" carinhoso".strip().capitalize())) # verifica o conteudo formatando o mesmo para verificaçao
