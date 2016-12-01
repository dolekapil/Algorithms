"""
CSCI-665 Homework 4: Problem 1
This program takes input integer list and the output is divided into two parts,
first part will divide sequence X into non-empty consecutive subsequences such
that the sum of each subsequence is even. This part uses greedy approach and runs
in O(N) time complexity. The second part will divide the sequence X into consecutive
subsequences such that the sum of each subsequence is odd. This part uses dynamic
programming approach and runs in O(N) complexity.

author: Kapil Dole
author: Chirag Kular
"""
import math

def oddSumPartition(n, nums):
    """
    This method takes the input list as input and gives the possible ways
    to divide the subsequence into consequative subsequences such that each
    subsequence sum is odd. This method uses dynamic programming approach
    and runs in O(N) time complexity.
    :param n: Total number of input elements.
    :param nums: Input sequence.
    :return: Possible ways of dividing subsequence, each having odd sum.
    """
    S = [0] * n
    checkFirstOdd = True
    prevEvenSum = 0
    preOddIndex = 0
    for index1 in range(n):
        # If number at given index is even, we are copying the content of
        # dynamic array at previous index.
        if nums[index1] % 2 == 0:
            if index1 > 0:
                S[index1] = S[index1 - 1]
            prevEvenSum += S[index1]
        else:
            # If the number at given index is first odd number, we are
            # incrementing counter of the dynamic array by 1.
            if checkFirstOdd:
                S[index1] += 1
                checkFirstOdd = False
                preOddIndex = index1
            # Otherwise, we are adding sum of the dynamic array content
            # for the even numbers preceding the given number till it finds
            # odd number and then dynamic array content at that odd number
            # index and one before it.
            else:
                if preOddIndex > 0:
                    S[index1] = prevEvenSum + S[preOddIndex] + S[preOddIndex - 1]
                else:
                    S[index1] = prevEvenSum + S[preOddIndex]
                preOddIndex = index1
                prevEvenSum = 0

    return S[n - 1]


def evenSumPartition(n, nums):
    """
    This method takes the input list as input and gives the possible ways
    to divide the subsequence into consequative subsequences such that each
    subsequence sum is even. This method uses greedy approach and runs in
    O(N) time complexity.
    :param n: Total number of input elements.
    :param nums: input sequence.
    :return: Possible ways of dividing subsequence, each having even sum.
    """
    counter = 0
    index = 0
    checkEven = True
    while index < n:
        # If number at given index is odd.
        if nums[index] % 2 == 1:
            # Check if given sum is even, if it is then change the flag
            # to false, otherwise set flag to true and increment the
            # counter by 1.
            if checkEven:
                checkEven = False
            else:
                checkEven = True
                counter += 1
        else:
            # if the number at given index it even and flag is true, then
            # increment the counter by 1.
            if checkEven:
                counter += 1
        index += 1
    # return 2^counter - 1 as total possible ways if counter > 0, else 0.
    return (0, int(math.pow(2, counter-1)))[counter > 0]


def main():
    """
    This is main function of our program which takes input from standard
    input and prints possible ways of even and odd partitions.
    :return: None.
    """
    n = int(input().strip())
    input_list = input().strip().split(" ")
    nums = [int(num) for num in input_list]
    print(evenSumPartition(n, nums))
    print(oddSumPartition(n, nums))


if __name__ == '__main__':
    main()