"""
CSCI-665 Homework 4: Problem 4 part b
This program basically takes an algebraic expression involving only positive integers
and the operators + and - as an input, and returns the maximum value of the expression
after fully parenthesizing it using dynamic programming approach. Complexity of the
algorithm is O(N3).

author: Kapil Dole
author: Chirag Kular
"""
import sys

def evaluateMinMax(Max_Mat, Min_Mat, operators, I, J, K):
    """
    This method calculates minimum and maximum values based on the Kth operator.
    We need both minimum and maximum values to solve this problem because, we
    don't know what next operator will be and hence we have to consider both
    minimum and maximum values for our computation.
    :param Max_Mat: 2D matrix which holds maximum values.
    :param Min_Mat: 2D matrix which holds minimum values.
    :param operators: List of operators in the expression.
    :param I: Ith index.
    :param J: Jth index.
    :param K: Kth index.
    :return: Minimum and Maximum values at given Ith and Jth index.
    """
    if operators[K - 1] == '+':
        maxVal = max(Max_Mat[I][K] + Max_Mat[K+1][J], Min_Mat[I][K] + Max_Mat[K+1][J],
                     Max_Mat[I][K] + Min_Mat[K+1][J], Min_Mat[I][K] + Min_Mat[K+1][J])
        minVal = min(Max_Mat[I][K] + Max_Mat[K+1][J], Min_Mat[I][K] + Max_Mat[K+1][J],
                     Max_Mat[I][K] + Min_Mat[K+1][J], Min_Mat[I][K] + Min_Mat[K+1][J])
    else:
        maxVal = max(Max_Mat[I][K] - Max_Mat[K+1][J], Min_Mat[I][K] - Max_Mat[K+1][J],
                     Max_Mat[I][K] - Min_Mat[K+1][J], Min_Mat[I][K] - Min_Mat[K+1][J])
        minVal = min(Max_Mat[I][K] - Max_Mat[K+1][J], Min_Mat[I][K] - Max_Mat[K+1][J],
                     Max_Mat[I][K] - Min_Mat[K+1][J], Min_Mat[I][K] - Min_Mat[K+1][J])

    return maxVal, minVal


def findMax(operands, operators):
    """
    This method computes maximum value of the given expression by fully parenthesizing
    it. Here, we are using matrix chain multiplication algorithm for finding so. Its
    complexity is O(N3).
    :param operands: List of operands in the expression.
    :param operators: List of operators in the expression.
    :return: Maximum value of expression after parenthesizing it.
    """
    N = len(operands)
    Max_Mat = []
    Min_Mat = []
    # Initializing matrix.
    for counter in range(N+1):
        Min_Mat.append([0 for count in range(N+1)])
        Max_Mat.append([0 for count in range(N+1)])
    # Assigning operands to the diagonal elements of the matrix based on their index.
    for index in range(1, N+1):
        Min_Mat[index][index] = operands[index - 1]
        Max_Mat[index][index] = operands[index - 1]

    # Applying matrix chain multiplication algorithm.
    for D in range(1, N):
        for L in range(1, N-D+1):
            R = L + D
            Max_Mat[L][R] = -sys.maxsize
            Min_Mat[L][R] = sys.maxsize
            for K in range(L, R):
                maxVal, minVal = evaluateMinMax(Max_Mat, Min_Mat, operators, L, R, K)
                if Max_Mat[L][R] < maxVal:
                    Max_Mat[L][R] = maxVal
                if Min_Mat[L][R] > minVal:
                    Min_Mat[L][R] = minVal

    return Max_Mat[1][N]


def main():
    """
    This is main function of our program, which takes input from standard input and
    displays the output after processing input list.
    :return: None.
    """
    input_expr = input().strip().split(' ')
    operands = []
    operators = []
    counter = 0
    # Separating operands and operators.
    while counter < len(input_expr):
        if input_expr[counter].isnumeric():
            operands.append(int(input_expr[counter]))
        else:
            operators.append(input_expr[counter])
        counter += 1

    print(findMax(operands, operators))


if __name__ == '__main__':
    main()