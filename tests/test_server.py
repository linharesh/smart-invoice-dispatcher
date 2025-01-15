import unittest
from unittest.mock import patch, MagicMock
from src.server import app, handle_event, is_paid_invoice_event, create_transfer

class ServerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode(), "server is running")

    def test_webhook_no_content(self):
        response = self.app.post('/webhook', data={})
        self.assertEqual(response.status_code, 415)
        self.assertIn("415 Unsupported Media Type", response.text)

    def test_webhook_no_event(self):
        response = self.app.post('/webhook', json={"some_key": "some_value"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("received", response.json["message"])

    @patch('src.server.handle_event')
    def test_webhook_with_event(self, mock_handle_event):
        response = self.app.post('/webhook', json={"event": {"key": "value"}})
        self.assertEqual(response.status_code, 200)
        self.assertIn("received", response.json["message"])
        mock_handle_event.assert_called_once()

    def test_handle_event_paid_invoice(self):
        event = {
            "subscription": "invoice",
            "log": {
                "invoice": {
                    "status": "paid",
                    "amount": 100
                }
            }
        }
        with patch('src.server.create_transfer') as mock_create_transfer:
            handle_event(event)
            mock_create_transfer.assert_called_once_with(100)

    def test_is_paid_invoice_event(self):
        event = {
            "subscription": "invoice",
            "log": {
                "invoice": {
                    "status": "paid"
                }
            }
        }
        self.assertTrue(is_paid_invoice_event(event))

    def test_is_paid_invoice_event_false(self):
        event = {
            "subscription": "invoice",
            "log": {
                "invoice": {
                    "status": "unpaid"
                }
            }
        }
        self.assertFalse(is_paid_invoice_event(event))

    @patch('src.server.TransferCreator')
    def test_create_transfer(self, MockTransferCreator):
        mock_transfer_creator = MockTransferCreator.return_value
        create_transfer(100)
        mock_transfer_creator.create.assert_called_once_with(100)

    def test_create_invoices_missing_amount(self):
        response = self.app.post('/create-invoices', json={})
        self.assertEqual(response.status_code, 400)
        self.assertIn("Missing 'amount'", response.json["error"])

    def test_create_invoices_invalid_amount(self):
        response = self.app.post('/create-invoices', json={"amount": -1})
        self.assertEqual(response.status_code, 400)
        self.assertIn("'amount' must be a positive integer", response.json["error"])

    @patch('src.server.InvoiceCreator')
    def test_create_invoices_success(self, MockInvoiceCreator):
        mock_invoice_creator = MockInvoiceCreator.return_value
        response = self.app.post('/create-invoices', json={"amount": 5})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Successfully created 5 invoices", response.json["message"])
        mock_invoice_creator.create_invoices.assert_called_once_with(5)

    @patch('src.server.InvoiceCreator')
    def test_create_invoices_exception(self, MockInvoiceCreator):
        mock_invoice_creator = MockInvoiceCreator.return_value
        mock_invoice_creator.create_invoices.side_effect = Exception("Test exception")
        response = self.app.post('/create-invoices', json={"amount": 5})
        self.assertEqual(response.status_code, 500)
        self.assertIn("Test exception", response.json["error"])

if __name__ == '__main__':
    unittest.main()

