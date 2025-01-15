import unittest
from unittest.mock import patch, MagicMock
from src.transfer import TransferCreator

class TestTransferCreator(unittest.TestCase):

    @patch('src.transfer.StarkBankAuth')
    @patch('src.transfer.starkbank')
    def test_create_transfer_success(self, mock_starkbank, mock_auth):
        # Arrange
        mock_user = MagicMock()
        mock_auth.return_value.get_user.return_value = mock_user
        mock_transfer = MagicMock()
        mock_starkbank.transfer.create.return_value = mock_transfer

        transfer_creator = TransferCreator()

        # Act
        result = transfer_creator.create(amount=1000)

        # Assert
        self.assertEqual(result, mock_transfer)
        mock_starkbank.transfer.create.assert_called_once()
        mock_auth.return_value.get_user.assert_called_once()

    @patch('src.transfer.StarkBankAuth')
    @patch('src.transfer.starkbank')
    def test_create_transfer_failure(self, mock_starkbank, mock_auth):
        # Arrange
        mock_user = MagicMock()
        mock_auth.return_value.get_user.return_value = mock_user
        mock_starkbank.transfer.create.side_effect = Exception("Transfer failed")

        transfer_creator = TransferCreator()

        # Act & Assert
        with self.assertRaises(Exception) as context:
            transfer_creator.create(amount=1000)
        
        self.assertTrue("Transfer failed" in str(context.exception))
        mock_starkbank.transfer.create.assert_called_once()
        mock_auth.return_value.get_user.assert_called_once()

if __name__ == '__main__':
    unittest.main()