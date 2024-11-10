# Aula 28 - 17-12-2019
# Lista com for e metodos

# Dica: Para este formulário será necessário usar um metodo para string novo.
# Vocês já conhecem o .strip() que remove os caracteres especiais \n do final 
# da string. o .splint('') que quebra a string em uma lista conforme o caracteres
# que tem dentro das aspas.
# O metodo novo para este exercico é o .replace('{velho}','{novo}') - O velho
# é um caracter que queira substituir e o novo é o caracter que deseja incluir.
# Exemplo pelo shell do pyton: 
# >>> 'agua verde mar'.replace('a','A') 
# 'AguA verde mAr'
# >>> 'agua verde mar'.replace('a','')
# 'gu verde mr'

# Como vemos, no primeiro exemplo o caracter "a" foi substituido pelo "A"
# e no segundo exemplo o "a" foi removido da string.

# https://forms.gle/PLuAZXpmpBvE1vkX7

# Fazer usando funções

# 1 - abrir o arquivo pesquisa.csv e fazer o tratamento padrão dos dados
# (criar lista com dicionarios)
# 2 - Separar aqueles que gostam de cerveja e salvar no cerveja.txt 
# 3 - Separar aqueles que gostam de refigerantes e salvar no refrigerante.txt
# 4 - Separar em arquivos .txt os homens das mulheres

def abrir_arquivo():
    arquivo = open('TrabalhosPython\Aula28 17-12\exercicios\Pesquisa de Gostos.csv','r')
    lista = []
    for i in arquivo:
        i.strip()
        j = i.split(',')
        dicionario = {'data':j[0],'genero':j[1],'escolaridade':j[2],'possui_veiculo':j[3],
                      'veiculo':j[4],'idade':j[5],'comida':j[6],'gosta_cerveja':j[7],
                      'marca_cerveja':j[8],'quat_mercadotech':j[9],'valor_mercadotech':j[10],
                      'gosta_refri':j[11],'marca_refri':j[12],'quat_refri':j[13],
                      'valor_refri':j[14],'opcao':j[15]}
        lista.append(dicionario)
    arquivo.close()
    return lista

def cerveja(lista):
    nao = []
    sim = []
    for i in lista:
        for j in i['gosta_cerveja']:
            if j == 'S':          
                sim.append(i)
                break
            elif j == 'T' or j == 'N':
                nao.append(i)
                break
    salvar('nao gosta cerv',nao)
    salvar('gosta cerv',sim)

def refrigerante(lista):
    nao = []
    sim = []
    for i in lista:
        for j in i['gosta_refri']:
            if j == 'S':          
                sim.append(i)
                break
            elif j == 'T' or j == 'N':
                nao.append(i)
                break
    salvar('nao gosta refri',nao)
    salvar('gosta refri',sim)

def genero(lista):
    femi = []
    masc = []
    for i in lista:
        for j in i['genero']:
            if j == 'M':          
                masc.append(i)
                break
            elif j == 'F':
                femi.append(i)
                break
    salvar('femi',femi)
    salvar('masc',masc)

def salvar(nome,lista):
    arquivo = open(f'TrabalhosPython\Aula28 17-12\exercicios\{nome}.txt','w')
    for i in lista:
        lista_dados = []
        for j in i:
            lista_dados.append(str(i[j]))
        arquivo.write(';'.join(lista_dados))
    arquivo.close()

lista = abrir_arquivo()
cerveja(lista)
refrigerante(lista)
genero(lista)

