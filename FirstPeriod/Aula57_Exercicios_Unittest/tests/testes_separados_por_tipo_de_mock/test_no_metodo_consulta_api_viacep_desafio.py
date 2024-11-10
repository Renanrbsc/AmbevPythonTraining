from unittest import TestCase
from unittest.mock import patch, call

from run import consulta_api_viacep

class TestMock(TestCase):

    @patch('run.input')
    @patch('app.api_cep.ApiCep.execute')
    def test_de_mock_em_execute(self, mock_execute, mock_input):
        # Arrange

        # Action
        mock_input.return_value = '89035520'
        mock_execute.return_value = {'cep': '89035-520', 'logradouro': 'Rua Hermann Eckelberg', 'complemento': '', 'bairro': 'Vila Nova', 'localidade': 'Blumenau', 'uf': 'SC', 'unidade': '', 'ibge': '4202404', 'gia': ''}
        metodo = consulta_api_viacep()
        # Assertion
        mock_execute.assert_called_once_with('89035520')
        mock_execute.assert_called_once()


# py -m unittest 
# py -m unittest tests\test_no_metodo_consulta_api_viacep_desafio.py


    # Teste de Cobertura
    #
    # 1- pip3 install coverage
    # 2- py -m coverage run -m unittest discover
    # 3- py -m coverage report -m
    # 4- py -m coverage html