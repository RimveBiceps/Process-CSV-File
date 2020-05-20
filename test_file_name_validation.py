import unittest
from file_name_validation import Validation


class TestFileNameValidation(unittest.TestCase):

	def setUp(self):
		self.validation = Validation()

	def test_file_name_with_white_space(self):
		# Assume
		file_name = 'failo vardas'
		# Action
		result = self.validation.file_name_is_valid(file_name)
		# Assert
		self.assertFalse(result)
		
	def test_file_name_empty(self):
		# Assume
		file_name = ''
		# Action
		result = self.validation.file_name_is_valid(file_name)
		# Assert
		self.assertFalse(result)
		
	def test_file_name_with_extension(self):
		# Assume
		file_name = 'test.csv'
		# Action
		result = self.validation.file_name_is_valid(file_name)
		# Assert
		self.assertFalse(result)
		
	def test_file_name_is_valid_and_it_exists(self):
		# Assume
		file_name = 'duomenys'
		# Action
		result = self.validation.file_name_is_valid(file_name)
		# Assert
		self.assertTrue(result)
		
	def test_file_name_is_valid_and_it_doesnt_exists(self):
		# Assume
		file_name = 'nera'
		# Action
		result = self.validation.file_name_is_valid(file_name)
		# Assert
		self.assertFalse(result)
		
if __name__ == '__main__':
	unittest.main()