from sys import argv

if len(argv) == 2:
	sudokuFile = argv[1]
else:
	print "Please specify a sudoku textfile as parameter."
	exit(0)

# print "Name of sudoku textfile: %s" % sudokuFile

f = open(sudokuFile, 'r')

data = f.read().split('\n')

listOfRows = [[],[],[],[],[],[],[],[],[]]
listOfColumns = [[],[],[],[],[],[],[],[],[]]
listOfNonets = [[],[],[],[],[],[],[],[],[]]

# Populating list of rows with appropriate digits from file
for i in range(0,9):
	listOfRows[i] = data[i].split(' ')

# Populating list of columns with appropriate digits from file	
for i in range(0, 9):
	for j in range(0, 9):
		listOfColumns[j].append(listOfRows[i][j])


# Debugging		
print "\nList of Rows:\n"
for row in listOfRows:
	print row
	
print "\nList of Columns:\n"
for column in listOfColumns:
	print column