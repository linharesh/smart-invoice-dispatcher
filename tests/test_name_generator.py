import unittest
from unittest.mock import patch

from src.name_generator import NameGenerator

class TestNameGenerator(unittest.TestCase):

    @patch('random.choice')
    def test_generate_random_name(self, mock_choice):
        # Mock the random.choice to return predictable values
        mock_choice.side_effect = ["Miguel", "A.", "Silva"]

        # Call the method
        result = NameGenerator.generate_random_name()

        # Assert the expected output
        self.assertEqual(result, "Miguel A. Silva")

    def test_generate_random_name_structure(self):
        # Call the method
        result = NameGenerator.generate_random_name()

        # Split the result into parts
        parts = result.split()

        # Assert that the result has exactly 3 parts (first name, middle initial, last name)
        self.assertEqual(len(parts), 3)

        # Assert that the middle initial is a single character followed by a dot
        self.assertTrue(len(parts[1]) == 2 and parts[1].endswith('.'))

    def test_generate_random_name_randomness(self):
        # Generate multiple names to check for randomness
        names = [NameGenerator.generate_random_name() for _ in range(100)]

        # Assert that not all names are the same (indicating randomness)
        self.assertGreater(len(set(names)), 1)

if __name__ == '__main__':
    unittest.main()