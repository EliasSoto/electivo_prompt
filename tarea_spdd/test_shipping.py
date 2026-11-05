import unittest
from shipping_calculator import ShippingCalculator

class TestShippingCalculator(unittest.TestCase):
    
    # =========================================================
    # BATERÍA DE PRUEBAS DEL PROFESOR
    # =========================================================
    # Los estudiantes deben lograr que el código generado por su 
    # archivo .prompt pase todas estas pruebas sin tocar el código Python.
    # =========================================================

    def test_standard_national_shipping(self):
        # Carrito $50, Nacional, No Express -> Costo Base $10.0
        cost = ShippingCalculator.calculate_shipping(50.0, False, 'NATIONAL')
        self.assertEqual(cost, 10.0)

    def test_free_national_shipping(self):
        # Carrito $150 (>= $100), Nacional, No Express -> Gratis $0.0
        cost = ShippingCalculator.calculate_shipping(150.0, False, 'NATIONAL')
        self.assertEqual(cost, 0.0)

    def test_express_national_shipping(self):
        # Carrito $50, Nacional, Express -> Base $10.0 + Express $15.0 = $25.0
        cost = ShippingCalculator.calculate_shipping(50.0, True, 'NATIONAL')
        self.assertEqual(cost, 25.0)

    def test_free_base_but_express_national(self):
        # Carrito $100 (Gratis base), Nacional, Express -> Base $0.0 + Express $15.0 = $15.0
        cost = ShippingCalculator.calculate_shipping(100.0, True, 'NATIONAL')
        self.assertEqual(cost, 15.0)

    def test_international_standard(self):
        # Carrito $50, Internacional, No Express -> (Base $10.0) * 2 = $20.0
        cost = ShippingCalculator.calculate_shipping(50.0, False, 'INTERNATIONAL')
        self.assertEqual(cost, 20.0)

    def test_international_express_and_free_base(self):
        # Carrito $200 (Gratis base), Internacional, Express -> (Base $0.0 + Express $15.0) * 2 = $30.0
        cost = ShippingCalculator.calculate_shipping(200.0, True, 'INTERNATIONAL')
        self.assertEqual(cost, 30.0)

    def test_unknown_destination_raises_error(self):
        # Destino desconocido debe levantar ValueError
        with self.assertRaises(ValueError):
            ShippingCalculator.calculate_shipping(50.0, False, 'MARS')

if __name__ == '__main__':
    unittest.main()