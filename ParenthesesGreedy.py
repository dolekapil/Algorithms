"""
CSCI-665 Homework 4: Problem 4 part a
This program basically takes an algebraic expression involving only positive integers
and the operators + and * as an input, and returns the maximum value of the expression
after fully parenthesizing it using greedy approach. Complexity of the algorithm
is O(N).

author: Kapil Dole
author: Chirag Kular
"""

def greedyMax(expression):
    """
    This method computes the maximum value of the given expression, after fully
    parenthesizing it using greedy approach. Here, we are computing addition
    operations and after that we are multiplying the results, which gives us
    maximum value of the expression. The complexity of the algorithm is O(N).
    :param expression: Input expression.
    :return: Maximum value of the expression.
    """
    maxVal = 1
    counter = 0
    temp = 0
    while counter < len(expression):
        current = expression[counter]
        if current.isdigit():
            temp += int(current)
            counter += 1
        # Give addition more priority.
        elif current == '+':
            temp += int(expression[counter + 1])
            counter += 2
        # At last perform multiplication.
        else:
            maxVal *= temp
            temp = 0
            counter += 1
    maxVal *= temp

    return maxVal


def main():
    """
    This is main function of our program, which takes input from standard input and
    displays the maximum value after processing input list.
    :return: None.
    """
    input_expr = input().strip().split(' ')
    print(greedyMax(input_expr))


if __name__ == '__main__':
    main()