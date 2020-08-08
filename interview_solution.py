import csv
import json
import argparse
import sys


class InterviewSolution:
    JSON_EXT = '.json'
    CSV_EXT = '.csv'

    def __init__(self):
        self.parser = None
        self.file_name = ""
        self.data = []
        self.filtered_data = {}
        self.key_header_index = None
        self.value_header_index = None

    def __find_columns_with_correct_headers_and_measurement_units(self, row, key_header, key_mes_unit, value_header, value_mes_unit):
        """
        Find columns with corresponding parameters (key_header, key_mes_unit) and (value_header, value_mes_unit)

        :param row:  Line number from csv file
        :param key_header: Key header in csv file
        :param key_mes_unit: Key header measurement unit
        :param value_header: Value header in csv file
        :param value_mes_unit: Value header measurement unit

        """

        key_header_indexes = [i for i, n in enumerate(self.data[row]) if n == key_header]
        value_header_indexes = [i for i, n in enumerate(self.data[row]) if n == value_header]

        if len(key_header_indexes) != 1:
            key_header_indexes = [x for x in key_header_indexes if self.data[row+1][x] == key_mes_unit]
        if len(key_header_indexes) == 0:
            raise Exception('Column with header "' + key_header + '" and measurement unit "' + key_mes_unit + '" is not found in file ' + self.file_name)
        self.key_header_index = key_header_indexes[0]

        if len(value_header_indexes) != 1:
            value_header_indexes = [x for x in value_header_indexes if self.data[row+1][x] == value_mes_unit]
        if len(value_header_indexes) == 0:
            raise Exception(
                'Column with header "' + value_header + '" and measurement unit "' + value_mes_unit + '"  is not found in file ' + self.file_name)
        self.value_header_index = value_header_indexes[0]

    def __append_filtered_data_value(self,row):
        try:
            key = float(row[self.key_header_index].encode('ascii', 'ignore'))
            value = float(row[self.value_header_index].encode('ascii', 'ignore'))
            self.filtered_data[key] = value
        except Exception as e:
            pass

    def __set_output_data(self, start, end, divisor):
        self.output_data = {key: value for key, value in self.filtered_data.items() if
                            start <= key <= end and key % divisor == 0}

    def __get_output_file_name(self):
        return self.file_name.rsplit(InterviewSolution.CSV_EXT, 1)[0] + InterviewSolution.JSON_EXT

    def parse_input_parameters(self):
        '''
        Parse and check validity of input arguments. Get csv file name from input arguments.

        '''
        print('Parsing of input parameters...')
        self.parser = argparse.ArgumentParser(description='This script loads .csv file and creates a simplified'
                                                          ' output file which contains nominal resistances for a '
                                                          'certain set of temperatures.')
        self.parser.add_argument('-c', type=str,  required='true',
                                 help='required argument -c and argument value C ("FileName".csv)')
        args = self.parser.parse_args()
        self.file_name = args.c

    def read_csv_file(self):
        """
        Read CSV file and load csv data to array.

        """
        print('Opening csv file...')
        self.data = []
        if not self.file_name.endswith(InterviewSolution.CSV_EXT):
            raise Exception('File '+ self.file_name + ' extension is not csv: ')

        try:
            with open(self.file_name, 'r', encoding='utf8') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for line in csv_reader:
                    self.data.append(line)
            print('Loading csv data...')
        except FileNotFoundError:
            raise Exception('No such file: ' + self.file_name)
        except ...:
            raise Exception('Could not open file: ' + self.file_name)

    def filter_data(self, key_header, key_mes_unit, value_header, value_mes_unit):
        """
        Filter data by arguments key_header, key_mes_unit, value_header, value_mes_unit.
        In case that key or value header or mes_unit does not exist, function throws exception with message.

        :param key_header: Header from csv file used as a key in dictionary
        :param key_mes_unit: Measurement unit of key header
        :param value_header: Header from csv used as a value in dictionary
        :param value_mes_unit: Measurement unit of value header

        """
        print('Data filtering...')
        self.filtered_data = {}
        self.key_header_index = -1
        self.value_header_index = -1

        for row in range (0,len(self.data)):
            if key_header in self.data[row] and value_header in self.data[row]:
                self.__find_columns_with_correct_headers_and_measurement_units(row, key_header, key_mes_unit, value_header,value_mes_unit)
            elif self.key_header_index != -1 and self.value_header_index != -1:
                self.__append_filtered_data_value(self.data[row])
        if self.key_header_index == -1 or self.value_header_index == -1:
            raise Exception ('No key or value header in csv file: ' + self.file_name)

    def create_json_file(self,start=0,end=100,divisor=5):
        """
        Create json file with the same name as input csv file.

        :param start: start value in json file
        :param end:   end value in json file
        :param divisor: parameter for filtering input data

        """
        print('Creating json file...')
        self.__set_output_data(start,end,divisor)

        try:
            with open(self.__get_output_file_name(), 'w') as outfile:
                outfile.write(str(json.dumps(self.output_data, indent=4)))
        except ...:
            raise Exception('Could not open file: ' + self.__get_output_file_name())


if __name__ == '__main__':
    interview_solution = InterviewSolution()
    try:
        interview_solution.parse_input_parameters()
        interview_solution.read_csv_file()
        interview_solution.filter_data("Temp","(degC)","Nom","(k ohm)")
        interview_solution.create_json_file(0,100,5)
        print('Process is finished, json file is created.')
    except Exception as e:
        print(interview_solution.parser.format_usage(), end='')
        if len(e.args) != 0:
            print(sys.argv[0] + ': error: ' + e.args[0])
        else:
            print(sys.argv[0] + ': error: Unknown error')


