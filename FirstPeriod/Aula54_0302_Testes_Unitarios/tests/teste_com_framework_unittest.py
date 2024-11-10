import unittest
from unittest import TestCase
from defs import soma

class TestComFramework(TestCase):

    def test_soma(self):
        # Arrange (organizar e inicializações)


        # Action (ação ou chamada de metodos)
        result = soma(2,2)

        # Assert (verificações)
        self.assertEqual(result,5,"soma errada")
  
#  python -m unittest tests\teste_com_framework_unittest.py
#  py -m unittest tests\teste_com_framework_unittest.py
#  py -m unittest teste_com_framework_unittest.py