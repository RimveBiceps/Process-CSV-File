from os import path

class Validation:

	def file_name_is_valid(self, file_name):
	
		if ' ' in file_name:  # white space in name
			return False
			
		if len(file_name) == 0:  # empty name
			return False
			
		if file_name[-4:] == '.csv':  # no need for file extension
			return False
			
		if not path.exists(file_name + ".csv"): # file doesn't exist
			return False
			
		return True