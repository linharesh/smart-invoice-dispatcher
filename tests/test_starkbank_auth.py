import unittest
from unittest.mock import patch, mock_open
from src.starkbank_auth import StarkBankAuth
import starkbank

class TestStarkBankAuth(unittest.TestCase):

    @patch('starkbank.Project')
    def test_create_user(self, mock_project):
        auth = StarkBankAuth()
        private_key_content = "fake_private_key_content"
        
        # Call the method
        user = auth.create_user(private_key_content)
        
        # Check if starkbank.Project was called with correct parameters
        mock_project.assert_called_once_with(
            environment=auth.environment,
            id=auth.project_id,
            private_key=private_key_content
        )
        
        # Check if the returned user is the mock object
        self.assertEqual(user, mock_project.return_value)

if __name__ == '__main__':
    unittest.main()