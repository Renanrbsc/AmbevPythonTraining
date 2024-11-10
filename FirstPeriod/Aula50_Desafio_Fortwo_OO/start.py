  # - tecnica
# piloto
# oficial1
# oficial2
  # - Cabine
# Chefe de serviço
# comissaria1
# comissario2
  # - Passageiros
# policial
# presidiario

lista_terminal = [
	'Piloto', 'Oficial1', 'Oficial2',
	'Chefe de serviço', 'Comissario1', 'Comissario2',
	'Policial', 'Presidente'
]


class Start:

	def __int__(self):
		self.fortwo = {'Motorista': '', 'Passageiro': ''}
		self.lista_aviao = []

	def viagem(self, motorista, passageiro):
		self.fortwo['Motorista'] = motorista
		self.fortwo['Passageiro'] = passageiro
		print("Iniciando Viagem...")
		print(f"Motorista: {self.fortwo['Motorista']} Passageiro: {self.fortwo['Passageiro']}")
		print("Finalizando a viagem...")

	def embarque(self):
		print(f"{self.fortwo['Motorista']} embarcou")
		print(f"{self.fortwo['Passageiro']} embarcou")
		if self.fortwo['Motorista'] == 'Piloto' \
				and self.fortwo['Passageiro'] == 'Chefe de serviço':
			self.lista_aviao.append(self.fortwo['Motorista'])

		elif self.fortwo['Motorista'] == 'Chefe de serviço' \
				and self.fortwo['Passageiro'] == 'Policial':
			self.lista_aviao.append(self.fortwo['Motorista'])

		elif self.fortwo['Motorista'] == 'Presidiario':
			self.lista_aviao.append(self.fortwo['Motorista'])
		else:
			self.lista_aviao.append(self.fortwo['Passageiro'])

	def desembarque(self):
		print(f"{self.fortwo['Passageiro']} desembarcou")
		print(f"{self.fortwo['Motorista']} desembarcou")
		self.fortwo['Motorista'] = ''
		self.fortwo['Passageiro'] = ''


start = Start()
start.viagem(lista_terminal[0], lista_terminal[1])
start.embarque()
