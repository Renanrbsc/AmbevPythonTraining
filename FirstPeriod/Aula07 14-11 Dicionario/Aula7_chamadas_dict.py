# Exercicio 1 - Dicionarios
# Escreva programa que leia os dados de cerveja
# Cerveja: Marca,Tipo, IBU, ABV, EBC, Volume
# Crie um dicionario para armazenar os dados
# Imprima os dados do dicionario (nao dicionario inteiro)

# Primeira forma - Simples

marca = input(f'Digite o marca da cerveja:\n')
tipo = input(f'Digite o tipo da cerveja:\n')
ibu = input(f'Digite o ibu da cerveja:\n')
abv = input(f'Digite o abv da cerveja:\n')
ebc = input(f'Digite o ebc da cerveja:\n')
volume = input(f'Digite o volume da cerveja:\n')

inf_cerveja = {'Marca':marca, 'tipo':tipo, 'ibu':ibu, 'abv':abv, 'ebc':ebc, 'volume':volume}

print(f"{inf_cerveja['Marca']}|{inf_cerveja['tipo']}|{inf_cerveja['ibu']}|{inf_cerveja['abv']}|{inf_cerveja['ebc']}|{inf_cerveja['volume']}")

# Segunda forma - usando o proprio recurso de dicionario

cerveja = {}
cerveja ['marca'] = (input('Digite a marca: '))
cerveja ['tipo'] = (input('Digite a marca: '))
cerveja ['ibu'] = int(input('Digite a marca: '))
cerveja ['abv'] = float(input('Digite a marca: '))
cerveja ['ebc'] = float(input('Digite a marca: '))
cerveja ['volume'] = float(input('Digite a marca: '))

print(f"{cerveja['marca']}|{cerveja['tipo']}|{cerveja['ibu']}|{cerveja['abv']}|{cerveja['ebc']}|{cerveja['volume']}")

