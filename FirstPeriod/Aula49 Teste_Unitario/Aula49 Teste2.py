from class_calculator import Calc


class Test:
	def __init__(self):
		self.calc = Calc(10,10)

	def test_soma(self):
		try:
			assert self.calc.soma() == 20
		except AssertionError:
			print("A soma não passou no teste!")
		else:
			print("A soma passou no teste!")

	def test_subtrair(self):
		try:
			assert self.calc.subtracao() == 0
		except AssertionError:
			print("A subtração não passou no teste!")
		else:
			print("A subtração passou no teste!")

	def test_multiply(self):
		try:
			assert self.calc.multiplicacao() == 100
		except AssertionError:
			print("A multiplicação não passou no teste!")
		else:
			print("A multiplicação passou no teste!")

	def test_get(self):
		try:
			assert self.calc.get_n1() == 10
			assert self.calc.get_n2() == 10
		except AssertionError:
			print("Metodo get não passou no teste!")
		else:
			print("Metodo get passou no teste!")

	def test_set(self):
		try:
			self.calc.set_n1(20)
			self.calc.set_n2(20)
			assert self.calc.get_n1() == 20
			assert self.calc.get_n2() == 20
		except AssertionError:
			print("Metodo set não passou no teste!")
		else:
			print("Metodo set passou no teste!")

	def main_test(self):
		self.test_soma()
		self.test_subtrair()
		self.test_multiply()
		self.test_get()
		self.test_set()


if __name__ == "__main__":
	test = Test()
	test.main_test()
