import unittest as ut
import Calculadora_números_complejos as cc

class test_calculadora(ut.TestCase):
    # Test suma
    def test_suma_complejos(self):
        resultado_1 = cc.complex_addition((3, 2),(1, -4))
        resultado_2 = cc.complex_addition((-5, 2),(5, -2))
        self.assertEqual(resultado_1, (4, -2))
        self.assertEqual(resultado_2, (0, 0))
        
    # Test suma
    def test_resta_complejos(self):
        resultado_3 = cc.complex_subtraction((3, 2), (1, -4))
        resultado_4 = cc.complex_subtraction((10, 5), (10, 0))
        self.assertEqual(resultado_3,(2, 6))
        self.assertEqual(resultado_4,(0, 5))
        
    # Test multiplicacion
    def test_mult_complejos(self):
        resultado_5 = cc.complex_multiplication((3, 2), (1, -4))
        resultado_6 = cc.complex_multiplication((0, 1),(0, 1))
        self.assertEqual(resultado_5, (11, -10))
        self.assertEqual(resultado_6, (-1, 0))
        
    # Test division
    def test_division_complejos(self):
        resultado_7 = cc.complex_division((-2, 1),(1, 2))
        resultado_8 = cc.complex_division((4, 0),(2, 0))
        self.assertEqual(resultado_7, (0, 1))
        self.assertEqual(resultado_8, (2, 0))
        
    # Test Modulo
    def test_modulo_complejos(self):
        resultado_9 = cc.complex_modulus((3, 4))
        resultado_10 = cc.complex_modulus((1, 1))
        self.assertAlmostEqual(resultado_9, 5)
        self.assertAlmostEqual(resultado_10, 1.41421356)
        
    # Test conjugado
    def test_conjugado_complejo(self):
        resultado_11 = cc.complex_conjugation((2, -3)) 
        resultado_12 = cc.complex_conjugation((-5, 0))
        self.assertEqual(resultado_11,(2, 3))
        self.assertEqual(resultado_12, (-5, -0))
        
    # Test Conversion sistema de coordenadas
    def test_cartesiano_polar(self):
        resultado_13 = cc. cartesian_to_polar((1, 1))
        rho_13_esperado = 1.41421356
        angle_13_esperado = 0.785398163397
        rho_13 = resultado_13[0]
        angle_13 = resultado_13[1]
        self.assertAlmostEqual(rho_13_esperado, rho_13)
        self.assertAlmostEqual(angle_13_esperado, angle_13)
        
        resultado_14 = cc. cartesian_to_polar((4, -2))
        rho_14_esperado = 4.472135954
        angle_14_esperado = -0.463647609
        rho_14 = resultado_14[0]
        angle_14 = resultado_14[1]
        self.assertAlmostEqual(rho_14_esperado, rho_14)
        self.assertAlmostEqual(angle_14_esperado, angle_14)
        
    def test_polar_cartesiano(self):
        resultado_15 = cc.polar_to_cartesian((1.4142, 0.7854))
        resultado_16 = cc.polar_to_cartesian((2, 1.5708))
        self.assertEqual(resultado_15, (1, 1))
        self.assertEqual(resultado_16,(0, 2))
    
    #Test fase
    def test_fase_complejo(self):
        resultado_17 = cc.complex_phase((1, 1))
        resultado_18 = cc.complex_phase((2, 3))
        self.assertAlmostEqual(resultado_17, 0.785398163397)
        self.assertAlmostEqual(resultado_18, 0.9827937232)
        
def main():
    ut.main()
main()