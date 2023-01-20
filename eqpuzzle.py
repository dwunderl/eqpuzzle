# import PySimpleGUI as sg
# sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()

# A class for the 4 numbers and goal - eqParams
# Class level object with an array of 4 numbers
# A class for a permutation, expression and result - eqCandidate

import csv
from itertools import permutations,product

class eqCandidate:
    def __init__(self,expression, result):
        self.expression = expression
        self.result = result
    
    def print_info(self):
        print(f"Expression: {self.expression}, Result: {self.result}")

class eqParams:
    def __init__(self,numbers, goal):
        self.numbers = numbers
        self.goal = goal
    def __init__(self):
        # Initialize class attributes here
        self.numbers = [0] * 4
        self.goal = 0
    def print_info(self):
        print(f"Numbers: {self.numbers}, Goal: {self.goal}")

# generate expressions for each number permutation against operation permutations
# and then all parenthesized orderings
# and then evaluate the expression to calculate the result

def evaluateExpression(expression, goal, solutions):
    try:
        result = eval(expression)
    except ZeroDivisionError:
        print("You can't divide by zero!")
        result = -999
    finally:
        #print (expression + " == " + str(result))
        if result == goal:
            solution = eqCandidate(expression, result)
            solution.print_info()
            solutions.append(solution)

msg = "Hello World"
print(msg)

def getParamsFromCsv(csvFileName):
    eqparams = eqParams()

    with open(csvFileName, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)
            eqparams.numbers = [row[0], row[1], row[2], row[3]]
            eqparams.goal = int(row[4])
    return eqparams

eqparams = getParamsFromCsv("eqpuzzle.csv")

# Numbers Permutation generation

numberPermutations = []
uniqueNumberPermutations = []
for numberPermutation in list(permutations(eqparams.numbers,4)):
    numberPermutations.append(numberPermutation)

    # Only keep isUnique permutations
    if numberPermutation not in uniqueNumberPermutations:
        uniqueNumberPermutations.append(numberPermutation)

# print(numberPermutationList)
# print(uniqueNumberPermutations)

# Operations permutation generation

operations = ["+", "-", "*","/"]
operationPermutations = product(operations, repeat=3)

# for operationPermutation in operationPermutations:
#     print(operationPermutation)




solutions = []
for np in uniqueNumberPermutations:
    print(np)
    operationPermutations = product(operations, repeat=3)

    for op in operationPermutations:
        #print(op)
        expression = str("(" + np[0] + op[0] + "(" + np[1] + op[1] + np[2] + "))" + op[2] + np[3])
        evaluateExpression(expression, eqparams.goal, solutions)
        expression = str(np[0] + op[0] + "((" + np[1] + op[1] + np[2] + ")" + op[2] + np[3] +")")
        evaluateExpression(expression, eqparams.goal, solutions)
        expression = str(np[0] + op[0] + "(" + np[1] + op[1] + "(" + np[2] + op[2] + np[3] +"))")
        evaluateExpression(expression, eqparams.goal, solutions)
        expression = str("(" + np[0] + op[0] + np[1] + ")" + op[1] + "(" + np[2] + op[2] + np[3] +")")
        evaluateExpression(expression, eqparams.goal, solutions)

