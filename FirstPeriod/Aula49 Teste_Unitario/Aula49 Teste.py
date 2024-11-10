# Testes

from sys import exit
from Rev_Classe import Calc

c = Calc(10,20)


def soma(n1, n2):
	return n1 + n2


def multiply(n1,n2,n3):
	return n1 * n2 * n3


def verifica_idade(idade):
	if idade >= 18:
		return True
	else:
		return False

# Verificacao se determinada codição é verdadeira

try:
	assert True
	assert 10 == 10
	assert 'Renan' != 'Gabriel'
	assert soma(2, 5) == 7
	assert multiply(5,7,2) == 70
	assert verifica_idade(18)
	assert verifica_idade(19)
	assert isinstance(c, Calc)
	assert c.soma() == c.get_resultado()
except AssertionError:
	print("Errooooooou!!!!!!")
else:
	print("Acertooooou!!!!")
	try:
		assert verifica_idade(17)
	except AssertionError:
		print("Errooooooou!!!!!!")
	else:
		print("Acertooooou!!!!")
finally:
	exit()


