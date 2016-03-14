from unittest import TestCase
from Calculadora import Calculadora

class TestCalculadora(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacia")
