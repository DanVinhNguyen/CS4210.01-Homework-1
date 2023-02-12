#-------------------------------------------------------------------------
# AUTHOR: Dan Nguyen
# FILENAME: decision_tree.py
# SPECIFICATION: This program forms a decision tree given curated data
# FOR: CS 4210- Assignment #1
# TIME SPENT: 6 hours
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard
# dictionaries, lists, and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

# temp function to print matrix
def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            text = matrix[i][j]
            if type(text) == int:
                print(f'{text}', end = '\t')
            else:
                print(f'{text[0:4]}', end = '\t')
        print()

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)


#transform the original categorical training features into numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3
# so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =

# arrays hold values that turn into certain numbers

one = ['Young', 'Myope', 'Normal', 'Yes']
two = ['Prepresbyopic', 'Hypermetrope', 'Reduced', 'No']
three = ['Presbyopic']

# arrays that hold values ONLY specified by the instructions on line 40
'''one = ['Young']
two = ['Prepresbyopic']
three = ['Presbyopic']'''

for i in range(len(db)):
    # temporary holder to append to X
    temp = [] * len(db[i])

    for j in range(len(db[i])):
    # skips last value
        if j == (len(db[i]) - 1):
            continue

        if db[i][j] in one:
            temp.append(1)
        elif db[i][j] in two:
            temp.append(2)
        elif db[i][j] in three:
            temp.append(3)
        else:
            temp.append(db[i][j])
    X.append(temp)

print_matrix(X)
print()


#transform the original categorical training classes into numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =
temp = [] # temporary holder to append to Y

for i in range(len(db)):
    j = len(db[i]) - 1 # sets the j index to the end of the row because that's all we need

    if db[i][j] == 'Yes':
        temp.append(1)
    elif db[i][j] == 'No':
        temp.append(2)
    else:
        continue

Y = temp

for i in Y:
    print(i, end = ' ')
print()

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()