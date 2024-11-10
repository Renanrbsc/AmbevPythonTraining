from unittest import TestCase
from unittest.mock import patch, call

from run import consulta_api_viacep

class TestRun(TestCase):

    @patch('run.input')
    @patch('run.print')
    @patch('app.api_cep.ApiCep.execute')
    def test_metodo_consulta_api_cep(self, mock_execute, mock_print, mock_input):
        # Arrange
        mock_input.return_value = '89035520'
        mock_execute.return_value = {'cep': '89035-520', 'logradouro': 'Rua Hermann Eckelberg', 'complemento': '', 'bairro': 'Vila Nova', 'localidade': 'Blumenau', 'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''}

        # Action
        metodo = consulta_api_viacep()

        # Assertion
        self.assertEqual(metodo,'Cep consultado com sucesso!')
        mock_input.assert_called_once_with('Informe o cep para consulta: ')
        mock_input.assert_called_once()
        mock_print.assert_called_once_with({'cep': '89035-520', 'logradouro': 'Rua Hermann Eckelberg', 'complemento': '', 'bairro': 'Vila Nova', 'localidade': 'Blumenau', 'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''})
        mock_print.assert_called_once()
        mock_execute.assert_called_once_with('89035520')
        mock_execute.assert_called_once()

# py -m unittest 
# py -m unittest tests\test_run.py


    # Teste de Cobertura
    #
    # 1- pip3 install coverage
    # 2- py -m coverage run -m unittest discover
    # 3- py -m coverage report -m
    # 4- py -m coverage html