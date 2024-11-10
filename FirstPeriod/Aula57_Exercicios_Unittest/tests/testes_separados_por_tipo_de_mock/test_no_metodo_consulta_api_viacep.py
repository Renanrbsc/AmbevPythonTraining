from unittest import TestCase
from unittest.mock import patch, call

from run import consulta_api_viacep

class TestMock(TestCase):


    @patch('run.input')
    def test_de_retorno_do_metodo(self, mock_input):
        # Arrange

        # Action
        mock_input.return_value = '89035520'
        metodo = consulta_api_viacep()
        # Assertion
        self.assertEqual(metodo,'Cep consultado com sucesso!')
    
    @patch('run.input')
    def test_de_mock_em_input(self, mock_input):
        # Arrange

        # Action
        mock_input.return_value = '89035520'
        metodo = consulta_api_viacep()
        # Assertion
        mock_input.assert_called_once_with('Informe o cep para consulta: ')
        mock_input.assert_called_once()


    @patch('run.input')
    @patch('run.print')
    def test_de_mock_em_print(self,mock_print, mock_input):
        # Arrange

        # Action
        mock_input.return_value = '89035520'

        metodo = consulta_api_viacep()
        # Assertion
        mock_print.assert_called_once_with({'cep': '89035-520', 'logradouro': 'Rua Hermann Eckelberg', 'complemento': '', 'bairro': 'Vila Nova', 'localidade': 'Blumenau', 'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''})
        mock_print.assert_called_once()


# py -m unittest 
# py -m unittest tests\test_no_metodo_consulta_api_viacep.py


    # Teste de Cobertura
    #
    # 1- pip3 install coverage
    # 2- py -m coverage run -m unittest discover
    # 3- py -m coverage report -m
    # 4- py -m coverage html