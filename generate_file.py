# Author: Rimvydas Kanapka
# Subject: Reading data from CSV and Exporting it to CSV
# Date: 2020-05-19 - 2020-05-20

import csv
from collections import defaultdict
from file_name_validation import Validation


result_by_worker	= defaultdict(list)  # an empty list for processing data
result_by_worker_type	= defaultdict(list)  # an empty list for processing data
first_file_data		= list()             # list for saving processed data
second_file_data	= list()	       # list for saving processed data

def read_data(file_name):
	'''
	Overview: A function takes file name as argument.
	Data is taken from CSV file and inserted into defaultdict type variable.
	'''	
	with open(file_name + '.csv', 'r', newline = '') as csv_output:
		reader = csv.reader(csv_output, delimiter = ',')
		next(reader, None)  # Skip the header
		
		for Worker, Type, Salary in reader:
			result_by_worker[Worker.strip()] += [float(Salary)]  			# grouping only by worker
			result_by_worker_type[Worker.strip(), Type.strip()] += [float(Salary)]  # grouping by worker and type
	

def process_data():
	'''
	Overview: Data is is being processed here for needed structure.
	First loop is for getting ["Darbuotojas", "Suma", "Mokesciai"] columns data
	Second loop is for getting ["Darbuotojas", "Tipas", "Suma"] columns data
	'''	
	for Worker, Type in result_by_worker.items():
		first_file_data.append([Worker] + [sum(Type)] + [sum(Type) * 40 / 100]) # getting each worker's total salary and 40% taxes

	for WorkerType, Sum in result_by_worker_type.items():
		second_file_data.append([WorkerType[0]] + [WorkerType[1]] + [sum(Sum)]) # getting each worker's total salary by his type
		
		
def create_csv(output_file, header, info):
	'''
	Overview: A function takes file name, CSV file header and file data as arguments.
	Then CSV file is generated with file name, columns and data provided in arguments
	'''	
	with open(output_file, 'w', newline = '') as csv_input:
		writer = csv.writer(csv_input)
		writer.writerow(header)  # write header
		
		for row in info:
			writer.writerow(row) # write data
			
			
def run_functions():
	'''
	Overview: Main function which contains all other functions for generating CSV file.
	'''	
	file_name = input("Please input CSV file name without it's extension: ")
	
	validation = Validation()
	if not validation.file_name_is_valid(file_name):
		print('Wrong file name')
	else:
		read_data(file_name)
		process_data()
		create_csv('darbuotojas_suma_mokesciai.csv', ['Darbuotojas', 'Suma', 'Mokesciai'], first_file_data,) # CSV file is generated with columns: "Darbuotojas", "Suma", "Mokesciai"
		create_csv('darbuotojas_tipas_suma.csv', ['Darbuotojas', 'Tipas', 'Suma'], second_file_data)	     # CSV file is generated with columns: ["Darbuotojas", "Tipas", "Suma"]
		
		print('Done.')
	
run_functions()
