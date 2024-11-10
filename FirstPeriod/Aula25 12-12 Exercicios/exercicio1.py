# Aula 21 - 12-12-2019


# Cliente.....

# Crie uma classe cliente.
# Use os seguintes atributos: codigo cliente(int), nome, idade(int), telefone, email, endereço
# Use o seguinte atributo de estado: crédito em R$, saldo R$, 
#                                    cliente_devedor(True/False)
# O atributo cliente_devedor deve ser True toda vez que o saldo negativo for menor 
# ou igual ao crédito. 
# Para o atributo cliente_devedor voltar a ser False o cliente deve pagar sua divida
# ficando com o saldo igual a 0 ou positivo.

# Como metodo use:
class Cliente:
    def __init__(self):

        self.lista_dados = []
        self.divida = 0
        self.credito  = 50
        self.saldo = 0 
        self.cliente_devedor = False       

    def adicionar_cadastro(self):
        dados = []  
        indice = ['Codigo: ','Nome:','Idade: ',
                  'Telefone: ','Email: ','Endereco: ']
        for i in indice:
            a = input(i)
            dados.append(a)
        dicionario = {'codigo':dados[0],'nome':dados[1],'idade':dados[2],
                      'telefone':dados[3],'email':dados[4],'endereco':dados[5],
                      'limite':self.credito,'divida':self.divida,'saldo':self.saldo,
                      'devedor':self.cliente_devedor}
        self.lista_dados.append(dicionario)
        print(f'Cadastro adicionado: {dicionario}')

    def atualizar (self):
        
        '''
        Este metodo serve para atualizar o cadastro do cliente. 
        Os dados que podem ser atualizados são: 
        nome, idade(int), telefone, email, endereço
        '''
        pass

    def limite_credito(self):
        i = self.__srt__()

        if i['divida'] > i['limite']:
            i['devedor'] = True

        if i['devedor'] == True:
            print(f"Cliente Devedor - {i['devedor']}")
            altera_cred = int(input('Digite quanto de limite deseja diminuir : '))
            print(f"Limite atual: {i['limite']}")
            if i['limite'] - altera_cred <= 0:
                print(f"Limite reduzido: {i['limite']}")
                i['limite'] = 0
                print(f"Limite atual: {i['limite']}")
            else:
                print(f"Limite reduzido: {altera_cred}")
                i['limite'] -= altera_cred
                print(f"Limite atual: {i['limite']}")
        else:
            print(f"Cliente Devedor - {i['devedor']}")
            print('Digite um valor maior ou menor de limite.')
            altera_cred = int(input('Digite o novo limite: '))
            i['limite'] = altera_cred
            print('Novo limite alterado com sucesso!')

    def adicionar_saldo(self):
        i = self.__srt__()
        valor = float(input('Digite o valor a ser depositado: R$'))
        i['saldo'] += valor
        print(f"Saldo atual: R${i['saldo']}")

    def dinheiro(self):
        i = self.__srt__()
        print('1- Usar credito\n2- Usar saldo/credito\n')
        op = int(input('Digite a opcao: '))
        if op == 1:
            valor = float(input("Digite o valor: R$"))
            if i['divida'] + valor <= i['limite']:
                i['divida'] += valor
                i['devedor'] = True
            else:
                print('\nLimite de cartao atingido!\nOperacao cancelada!\n')
        elif op == 2:
            valor = float(input("Digite o valor: R$"))
            if valor <= i['saldo'] + i['limite'] - i['divida']:
                i['saldo'] = i['saldo'] - valor
                if i['saldo'] < 0:
                    i['divida'] = i['divida'] + (i['saldo'] - (i['saldo']*2))
                    i['saldo'] = 0
                    i['devedor'] = True
                    print(f"\nSaldo excedido!\nLimite utilizado {valor - i['saldo']}")
                else:
                    print(f"Saldo atualizado: {i['saldo']}")
                    i['devedor'] = False
            else:
                print('Saldo e limite excedido!\nOperacao cancelada!\n')
        
        print(f'''\nSaldo atual do cartao: {i['saldo']}
Divida do cartao: {i['divida']}
Limite do cartao: {i['limite']}''')

    def pagar_divida(self):
        i = self.__srt__()

        if i['divida'] > 0:
            print(f"Sua divida é: {i['divida']}")
            valor = int(input('Digite quanto deseja pagar: '))
            if valor <= i['divida'] and valor >= 0: 
                i['divida'] -= valor
                print(f"Sua divida atual é: {i['divida']}")
                if i['divida'] == 0:
                    i['divida'] = 0
                    i['devedor'] = False
            else:
                print('Valor invalido!')
        else:
            print('Nao há dividas!')
            i['devedor'] = False

    def __eq__(self):
        while True:                
            cod = input("Digite o codigo do cliente: ")
            if not self.lista_dados:
                print('\nNão há clientes cadastrados!\n')
                print('Cadastrar cliente!')
                cliente.adicionar_cadastro()
                for i in self.lista_dados:
                    if cod == i['codigo']:  
                        return i
                print('Codigo invalido!')
            else:
                for i in self.lista_dados:
                    if cod == i['codigo']:  
                        return i
                print('Codigo invalido!')


    def __srt__(self):
        i = self.__eq__()
        print(f'''\nCodigo: {i['codigo']}
Nome:{i['nome']}
Idade: {i['idade']}
Telefone: {i['telefone']}
Email: {i['email']}
Endereco: {i['endereco']}
Saldo: {i['saldo']}
Limite Credito: {i['limite']}
Dividas: {i['divida']}\n''')
        return i



if __name__ == "__main__":

    '''
    Use este if para fazer os testes com a classe.
    Este if pergunta se este arquivo está sendo executado diretamente.
    Caso positivo o código será executado.
    '''
    pass

cliente = Cliente()


def menu():
    print('**********************************')
    print('*1 Cadastrar Usuarios            *')
    print('*2 Limite de cartao credito      *')
    print('*3 Adicionar Saldo               *')
    print('*4 Usar credito e Debito         *')
    print('*5 Pagamento de Divida           *')
    print('**********************************')
    print('Digite a opcao: ')

while True:
    menu()
    op = int(input())
    if op == 1:
        print('Cadastrar usuario:')
        cliente.adicionar_cadastro()
    elif op == 2:
        print('Definir limite de cartao')
        cliente.limite_credito()
    elif op == 3:
        print('Adicionar Saldo')
        cliente.adicionar_saldo()
    elif op == 4:
        cliente.dinheiro()
    elif op == 5:
        print('Pagar dividas')
        cliente.pagar_divida()



