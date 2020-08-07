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

    def __set_column_index_from_row(self, row, key_header, value_header):
        self.key_header_index = row.index(key_header)
        self.value_header_index = row.index(value_header)

    def __append_filtered_data_value(self,row):
        try:
            key = float(row[self.key_header_index].encode('ascii', 'ignore'))
            value = float(row[self.value_header_index].encode('ascii', 'ignore'))
            self.filtered_data[key] = value
        except Exception as e:
            pass

    def __set_output_data(self, start, end, step):
        self.output_data = {key: value for key, value in self.filtered_data.items() if
                            start <= key <= end and key % step == 0}

    def __get_output_file_name(self):
        return self.file_name.rsplit(InterviewSolution.CSV_EXT, 1)[0] + InterviewSolution.JSON_EXT

    def parse_input_parameters(self):
        '''
        hhhh
        :return:
        '''
        print('Parsing of input parameters...')
        self.parser = argparse.ArgumentParser(description='This script loads .csv file and creates a simplified'
                                                          ' output file which contains nominal resistances for a '
                                                          'certain set of temperatures.')
        self.parser.add_argument('-c', type=str,  required='true',
                                 help="required argument -c and argument value C (name of csv file)")
        args = self.parser.parse_args()
        self.file_name = args.c

    def read_csv_file(self):
        print('Opening csv file...')
        self.data = []
        if not self.file_name.endswith(InterviewSolution.CSV_EXT):
            raise Exception('File '+ self.file_name + ' extension is not csv: ')

        try:
            with open(self.file_name, 'r') as csv_file:
                csv_reader = csv.reader(csv_file, delimiter=',')
                for line in csv_reader:
                    self.data.append(line)
            print('Loading csv data...')
        except FileNotFoundError:
            raise Exception('No such file: ' + self.file_name)
        except ...:
            raise Exception('Could not open file: ' + self.file_name)

    def filter_data(self, key_header: str, value_header):
        print('Data filtering...')
        self.filtered_data = {}
        self.key_header_index = -1
        self.value_header_index = -1

        for row in self.data:
            if key_header in row and value_header in row:
                self.__set_column_index_from_row(row, key_header, value_header)
            elif self.key_header_index != -1 and self.value_header_index != -1:
                self.__append_filtered_data_value(row)

        if self.key_header_index == -1 or self.value_header_index == -1:
            raise Exception ('No key or value header in csv file: ' + self.file_name)

    def create_json_file(self,start=0,end=100,step=5):
        print('Creating json file...')
        self.__set_output_data(start,end,step)

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
        #print(interview_solution.data)
        interview_solution.filter_data("Temp","Nom")
        interview_solution.create_json_file(0,100,5)
        print('Process is finished, json file is created.')
    except Exception as e:
        print(sys.argv[0] + ': error: ' + e.args[0])
        # self.parser.print_help()


