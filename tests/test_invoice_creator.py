import unittest
from unittest.mock import patch, MagicMock
from src.invoice_creator import InvoiceCreator

class TestInvoiceCreator(unittest.TestCase):

    @patch('src.invoice_creator.StarkBankAuth')
    @patch('src.invoice_creator.TaxIdGenerator')
    @patch('src.invoice_creator.NameGenerator')
    @patch('src.invoice_creator.starkbank.Invoice')
    @patch('src.invoice_creator.starkbank.invoice.create')
    def test_create_invoices_success(self, mock_invoice_create, mock_invoice, mock_name_generator, mock_tax_id_generator, mock_starkbank_auth):
        # Setup mocks
        mock_name_generator.generate_random_name.return_value = "John Doe"
        mock_tax_id_generator.return_value.generate_random_tax_id.return_value = "123.456.789-00"
        mock_invoice_create.return_value = ["invoice1", "invoice2", "invoice3"]
        mock_starkbank_auth.return_value.get_user.return_value = "mock_user"

        # Create instance of InvoiceCreator
        invoice_creator = InvoiceCreator()

        # Call the method
        result = invoice_creator.create_invoices(num_invoices=3)

        # Assertions
        self.assertEqual(result, ["invoice1", "invoice2", "invoice3"])
        self.assertEqual(mock_invoice.call_count, 3)
        mock_invoice_create.assert_called_once()

    @patch('src.invoice_creator.StarkBankAuth')
    @patch('src.invoice_creator.TaxIdGenerator')
    @patch('src.invoice_creator.NameGenerator')
    @patch('src.invoice_creator.starkbank.Invoice')
    @patch('src.invoice_creator.starkbank.invoice.create')
    def test_create_invoices_exception(self, mock_invoice_create, mock_invoice, mock_name_generator, mock_tax_id_generator, mock_starkbank_auth):
        # Setup mocks
        mock_name_generator.generate_random_name.return_value = "John Doe"
        mock_tax_id_generator.return_value.generate_random_tax_id.return_value = "123.456.789-00"
        mock_invoice_create.side_effect = Exception("API Error")
        mock_starkbank_auth.return_value.get_user.return_value = "mock_user"

        # Create instance of InvoiceCreator
        invoice_creator = InvoiceCreator()

        # Call the method and assert exception
        with self.assertRaises(Exception) as context:
            invoice_creator.create_invoices(num_invoices=3)

        self.assertTrue("API Error" in str(context.exception))
        self.assertEqual(mock_invoice.call_count, 3)
        mock_invoice_create.assert_called_once()

if __name__ == '__main__':
    unittest.main()