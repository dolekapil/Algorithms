"""
CSCI-665 Homework 3: Problem 2
This program gives an algorithm that determines total number of different
decoding for given n bits, when encoding table is provided.It uses dynamic
programming for solving the problem and its running time is O(N).

author: Kapil Dole
author: Chirag Kular
"""

# Encoding table.
A = '0'
B = '1'
C = '10'
D = '01'
E = '111'
F = '011'


def getDecoding(str):
    """
    This function provides O(N) algorithm for solving the decoding
    problem, here we are using dynamic programming to solve it, where
    we are making use of overlapping sub problems.
    :param str: Encoded String.
    :return: Total possible number of decoding.
    """

    # Initializing the list.
    S = [0 for counter in range(len(str))]
    for index in range(0, len(S)):
        temp = 0
        # if index is negative, S[j] = 1, where j < 0
        if index - 1 < 0:
            temp += 1
        else:
            temp += S[index - 1]

        # If the previous 2 bits are valid, then add
        # S[j-2] to the S[j], if exists else 0.
        if index - 1 >= 0:
            prev2Bits = str[index - 1] + str[index]
            if prev2Bits == C or prev2Bits == D:
                if index - 2 >= 0:
                    temp += S[index - 2]
                else:
                    temp += 1

        # If the previous 3 bits are valid, then add
        # S[j-3] to the S[j], if exists else 0.
        if index - 2 >= 0:
            prev3Bits = str[index - 2] + str[index - 1] + str[index]
            if prev3Bits == E or prev3Bits == F:
                if index - 3 >= 0:
                    temp += S[index - 3]
                else:
                    temp += 1

        S[index] = temp
    # Returning last element of S, containing our solution.
    return S[index]


def main():
    """
    This is main function of our program which takes input
    from standard input and displays the results.
    :return: None.
    """
    str = input().strip()
    print(getDecoding(str))


if __name__ == '__main__':
    main()
