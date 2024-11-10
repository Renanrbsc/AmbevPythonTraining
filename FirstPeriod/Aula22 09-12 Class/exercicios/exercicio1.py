# Aula 21 - 09-12-2019
# Como Tratar e Trabalhar Erros!!!

# Com base no seguinte dado bruto:

dadobruto = '1;Arnaldo;23;m;alexcabeludo2@hotmail.com;014908648117'

# 1) Faça uma classe cliente que receba como parametro o dado bruto.
# 2) A classe deve iniciar (__init__) guardando o dado bruto nume variável chamada self.dado_bruto
# 3) As variáveis  código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# devem iniciar com o valor None
# 4) Crie um metodo que pegue o valor bruto e adicione nas variáveis:
# código cliente (inteiro), nome, idade (inteiro), sexo, email, telefone
# convertendo os valores de string para inteiros quando necessários. 
# (Faça da forma que vocês conseguirem! O importante é o resultado e não como chegaram nele!)

class Cliente:

    def __init__ (self,dadobruto):

        # Variaveis globais da classe
        self.dado_bruto = dadobruto

        # Variaveis exclusivas da classe
        self.lista = []
        self.lista_linha = []
        self.codigo_cliente = None
        self.nome_cliente = None
        self.idade_cliente = None
        self.sexo_cliente = None
        self.email_cliente = None
        self.telefone_cliente = None
        
    def separa_dados(self): # metodo

        self.dado_bruto.strip() # Quebrando a string 
        self.lista_linha = self.dado_bruto.split(';') # lancando os dados separados em nova lista

        print(self.lista_linha) # imprimindo nova lista

        # lancando dados em variaveis exclusivas da classe
        self.codigo_cliente = self.lista_linha[0]
        self.nome_cliente = self.lista_linha[1]
        self.idade_cliente = self.lista_linha[2]
        self.sexo_cliente = self.lista_linha[3]
        self.email_cliente = self.lista_linha[4]
        self.telefone_cliente = self.lista_linha[5]

        print(f'''\nCodigo: {self.codigo_cliente} 
Nome: {self.nome_cliente} 
Idade: {self.idade_cliente} 
Sexo: {self.sexo_cliente} 
Email: {self.email_cliente} 
Telefone: {self.telefone_cliente}\n''')



cliente = Cliente(dadobruto)

cliente.separa_dados()




    


