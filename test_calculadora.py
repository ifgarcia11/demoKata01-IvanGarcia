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

    def test_sumar_una_cadenaConDosNumeros(self):
        self.assertEqual(Calculadora().sumar("5,2,4,1"),12,"Multiples numeros")

    def test_sumar_una_cadena_conMultiplesNumerosSeparadores(self):
        self.assertEqual(Calculadora().sumar("5,2&4:1:2&8"),22,"Multiples numeros")