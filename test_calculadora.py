from unittest import TestCase
from Calculadora import Calculadora

class TestCalculadora(TestCase):
    def test_sumar(self):
        self.assertEqual(Calculadora().sumar(""),0,"Cadena vacia")

    def test_sumar_una_cadena(self):
        self.assertEqual(Calculadora().sumar("1"),1,"un numero")

    def test_sumar_una_cadenaConUnNumero(self):
        self.assertEqual(Calculadora().sumar("1"),1,"un numero")
        self.assertEqual(Calculadora().sumar("2"),2,"un numero")

    def test_sumar_una_cadenaConDosNumeros(self):
        self.assertEqual(Calculadora().sumar("1,2"),3,"Dos numeros")
