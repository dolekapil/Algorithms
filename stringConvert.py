"""
CSCI-665 Homework 4: Problem 3
This program converts the string X with length m to the string Y with
length n, so that cost incured is minimum. The complexity of algorithm
is O(M*N).

author: Kapil Dole
author: Chirag Kular
"""
import sys

def findMinCost(first, second):
    """
    This method computes the minimum cost required to convert one
    string X to another string Y.
    :param first: First input string.
    :param second: Second input string.
    :return: Minimum cost required to convert the string X to Y.
    """
    m = len(first)
    n = len(second)
    Min_arr = [[0 for _ in range(n+1)] for _ in range(m+1)]

    for index1 in range(m+1):
        for index2 in range(n+1):
            # When first string is empty, we have to insert all
            # characters of second string to first string.
            if index1 == 0:
                Min_arr[index1][index2] = 4 * index2
            # When second string is empty, we have to delete all
            # characters of first string.
            elif index2 == 0:
                Min_arr[index1][index2] = 3 * index1
            # If characters matches at given index, carry forward
            # the previous cost.
            elif first[index1-1] == second[index2-1]:
                Min_arr[index1][index2] = Min_arr[index1 - 1][index2 - 1]
            # Otherwise, compute cost for all three operations, add
            # delete and replace and choose minimum among them.
            else:
                insert_cost = 4 + Min_arr[index1][index2 - 1]
                delete_cost = 3 + Min_arr[index1 - 1][index2]
                if index1 - 2 >= 0:
                    replace_cost = 5 + Min_arr[index1 - 2][index2 - 1]
                else:
                    replace_cost = sys.maxsize
                Min_arr[index1][index2] = min(insert_cost, delete_cost, replace_cost)

    return Min_arr[m][n]


def main():
    """
    This is main method of our program, which takes input from standard input
    and prints minimum cost for converting string X to Y.
    :return:
    """
    first_str = input().strip()
    second_str = input().strip()
    X = [char for char in first_str]
    Y = [char for char in second_str]
    print(findMinCost(X, Y))


if __name__ == '__main__':
    main()