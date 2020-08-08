# InterviewSolution
### Description of interview_solution.py script
###### This script loads .csv file and creates a simplified output file which contains nominal resistances for a certain set of temperatures.

Process of making creating JSON file is divided into few steps and functions. 
- Step 1: Parsing of input arguments. In case that input arguments are not correct, function throws exception with corresponding message. 
- Step 2: Opening csv file. After succesfull opened file, function loads csv data to matrix (two-dimensional array).
- Step 3: Finding of key and value headers with their corresponding meauserment units in loaded data. After headers are found, function makes directory with "key" and "value"      values. 
- Step 4: Data filtering using parameters "start","end" and "divisor", and making of "output_data" for JSON file.
- Step 5: Creating JSON file which contains "output_data". Name of created json file is the same as input csv file name. 

### Usage examples
#### Usage example 1 :  The correct way of running interview_solution.py script

```bash
python interview_solution.py -c NTCG163JF103FT1.csv 

Parsing of input parameters...
Opening csv file...
Loading csv data...
Data filtering...
Creating json file...
Process is finished, json file is created.
```
#### Usage example 2 : Running script with -h argument

```bash
python interview_solution.py -h

Parsing of input parameters...
usage: interview_solution.py [-h] -c C

This script loads .csv file and creates a simplified output file which contains nominal resistances for a certain set
of temperatures.

optional arguments:
  -h, --help  show this help message and exit
  -c C        required argument -c and argument value C ("FileName".csv)
```
#### Usage example 3: Running script without argument

```bash
python interview_solution.py

Parsing of input parameters...
usage: interview_solution.py [-h] -c C
interview_solution.py: error: the following arguments are required: -c
```
#### Usage example 4: Running script without argument value

```bash
python interview_solution.py -c

Parsing of input parameters...
usage: interview_solution.py [-h] -c C
interview_solution.py: error: argument -c: expected one argument
```

#### Usage example 5 : Running scripts with no ".csv" argument

```bash
python interview_solution.py -c NTCG163JF103FT1.txt

Parsing of input parameters...
Opening csv file...
usage: interview_solution.py [-h] -c C
interview_solution.py: error: File NTCG163JF103FT1.txt extension is not csv:
```
#### Usage example 6 : Opening file that does not exist

```bash
python interview_solution.py -c aaNTCG163JF103FT1.csv

Parsing of input parameters...
Opening csv file...
usage: interview_solution.py [-h] -c C
interview_solution.py: error: No such file: aaNTCG163JF103FT1.csv
```

#### Usage example 7 : Running script correctly, but csv file doesn't contain key or header value 

```bash
interview_solution.py -c NTCG163JF103FT1.csv

Parsing of input parameters...
Opening csv file...
Loading csv data...
Data filtering...
usage: interview_solution.py [-h] -c C
interview_solution.py: error: No key or value header in csv file: NTCG163JF103FT1.csv
```

#### Usage example 8 :  Incorrect measurement unit of "key" column 

```bash
python interview_solution.py -c NTCG163JF103FT1.csv

Parsing of input parameters...
Opening csv file...
Loading csv data...
Data filtering...
usage: interview_solution.py [-h] -c C
interview_solution.py: error: Column with header "Temp" and measurement unit "(degC)" is not found in file NTCG163JF103FT1.csv
```
#### Usage example 9 : Incorrect measurement unit of "value" column 

```bash
python interview_solution.py -c NTCG163JF103FT1.csv

Parsing of input parameters...
Opening csv file...
Loading csv data...
Data filtering...
usage: interview_solution.py [-h] -c C
interview_solution.py: error: Column with header "Nom" and measurement unit "(k ohm)"  is not found in file NTCG163JF103FT1.csv
```
### Note 
If the input csv file is not utf-8 encoded, there is certainly at least one case in which the script will not work correctly.


