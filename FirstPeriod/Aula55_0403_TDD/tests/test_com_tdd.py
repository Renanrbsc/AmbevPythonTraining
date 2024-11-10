from unittest import TestCase

from Aula55_0403_TDD.par.calcula_se_um_numero_eh_par import calcula_se_um_numero_eh_par

class TestComTDD(TestCase):

    def test_se_um_numero_eh_par(self):


        resultado = calcula_se_um_numero_eh_par(2)

        self.assertTrue(resultado)

    # py -m unittest  Aula55_0403_TDD\tests\test_com_tdd.py

        