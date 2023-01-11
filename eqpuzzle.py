import PySimpleGUI as sg

#sg.Window(title="Hello World", layout=[[]], margins=(100, 50)).read()


msg = "Hello World"
print(msg)

from itertools import permutations,product

# Numbers Permutation generation

goal = 19
numberArray = ["22", "12", "9", "7"]
numberPermutations = []
uniqueNumberPermutations = []
for numberPermutation in list(permutations(numberArray,4)):
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


# generate expressions for each number permutation against operation permutations
# and then all parenthesized orderings
# and then evaluate the expression to calculate the result

class Solution:
    def __init__(self,expression, result):
        self.expression = expression
        self.result = result
    
    def print_info(self):
        print(f"Expression: {self.expression}, Result: {self.result}")

def evaluateExpression(expression, goal, solutions):
        result = eval(expression)
        #print (expression + " == " + str(result))
        if result == goal:
            solution = Solution(expression, result)
            solution.print_info()
            solutions.append(solution)


solutions = []
for np in uniqueNumberPermutations:
    print(np)
    operationPermutations = product(operations, repeat=3)

    for op in operationPermutations:
        #print(op)
        expression = str("(" + np[0] + op[0] + "(" + np[1] + op[1] + np[2] + "))" + op[2] + np[3])
        evaluateExpression(expression, goal, solutions)
        expression = str(np[0] + op[0] + "((" + np[1] + op[1] + np[2] + ")" + op[2] + np[3] +")")
        evaluateExpression(expression, goal, solutions)
        expression = str(np[0] + op[0] + "(" + np[1] + op[1] + "(" + np[2] + op[2] + np[3] +"))")
        evaluateExpression(expression, goal, solutions)
        expression = str("(" + np[0] + op[0] + np[1] + ")" + op[1] + "(" + np[2] + op[2] + np[3] +")")
        evaluateExpression(expression, goal, solutions)


#-------- old code for reference ---------------
# 