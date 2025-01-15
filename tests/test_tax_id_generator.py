import unittest
from src.tax_id_generator import TaxIdGenerator

class TestTaxIdGenerator(unittest.TestCase):

    def setUp(self):
        self.generator = TaxIdGenerator()

    def test_generate_random_tax_id_length(self):
        cpf = self.generator.generate_random_tax_id()
        self.assertEqual(len(cpf), 11, "Generated CPF should be 11 digits long")

    def test_generate_random_tax_id_digits(self):
        cpf = self.generator.generate_random_tax_id()
        self.assertTrue(cpf.isdigit(), "Generated CPF should contain only digits")

    def test_generate_random_tax_id_unique(self):
        cpf1 = self.generator.generate_random_tax_id()
        cpf2 = self.generator.generate_random_tax_id()
        self.assertNotEqual(cpf1, cpf2, "Generated CPFs should be unique")

    def test_calculate_first_verification_digit(self):
        partial_cpf = '123456789'
        expected_digit = self.generator._TaxIdGenerator__calcular_digito(partial_cpf)
        self.assertEqual(expected_digit, '0', "First verification digit should be 0 for '123456789'")

    def test_calculate_second_verification_digit(self):
        partial_cpf = '1234567890'
        expected_digit = self.generator._TaxIdGenerator__calcular_digito(partial_cpf)
        self.assertEqual(expected_digit, '9', "Second verification digit should be 9 for '1234567890'")

if __name__ == '__main__':
    unittest.main()