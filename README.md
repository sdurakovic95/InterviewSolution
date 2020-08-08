# InterviewSolution
### Description of interview_solution.py script
###### This script loads .csv file and creates a simplified output file which contains nominal resistances for a certain set of temperatures.

Process of making creating JSON file is divided into few steps and functions. 
- Step 1: Parsing of input arguments. In case that input arguments are not correct, function throws exception with corresponding message. 
- Step 2: Opening csv file. After succesfull opened file, function loads csv data to matrix (two-dimensional array).
- Step 3: Finding of key and value headers with their corresponding meauserment units in loaded data. After headers are found, function makes directory with "key" and "value"      values. 
- Step 4: Data filtering using parameters "start","end" and "divisor", and making of "output_data" for JSON file.
- Step 5: Creating JSON file which contains "output_data". Name of created json file is the same as input csv file name. 




