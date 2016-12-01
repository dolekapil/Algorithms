"""
CSCI-665 Homework 4: Problem 2
This program takes input integer list and given largest possible sum in
increasing subsequence, it uses dynamic programming approach for solving
the problem and it runs in O(N2) complexity.

author: Kapil Dole
author: Chirag Kular
"""

def maximumIncreasingSubsequence(n, nums):
    """
    This method takes input integer sequence and finds the increasing
    subsequence with maximum sum. It runs in O(N2) time complexity.
    :param n: Total number of elements.
    :param nums: Input subsequence.
    :return: Increasing subsequence largest sum.
    """
    Summation = [0] * n
    S = [0] * n
    maxSum = 0
    for index1 in range(0, n):
        S[index1] = 1
        Summation[index1] = nums[index1]
        for index2 in range(0, index1):
            # Check if list is in increasing or not.
            if nums[index2] < nums[index1]:
                # If the length of 2 subsequences are equal, then choose
                # one with maximum Summation value.
                if S[index1] == S[index2] + 1:
                    if Summation[index2] + nums[index1] > Summation[index1]:
                        Summation[index1] = Summation[index2] + nums[index1]
                # If the length of the current subsequences is greater than
                # previous subsequence and if the Summation of previous and
                # current element is greater than current Summation, then
                # update the Summation array.
                elif S[index1] < S[index2] + 1:
                    if Summation[index2] + nums[index1] > Summation[index1]:
                        S[index1] = S[index2] + 1
                        Summation[index1] = Summation[index2] + nums[index1]
                # Updating the maximum sum value, if current is greater.
                if maxSum < Summation[index1]:
                    maxSum = Summation[index1]

    return maxSum


def main():
    """
    This is main function of our program which takes input from standard
    input and prints the maximum sum of increasing subsequence.
    :return: None.
    """
    n = int(input().strip())
    input_list = input().strip().split(" ")
    nums = [int(num) for num in input_list]
    print(maximumIncreasingSubsequence(n, nums))


if __name__ == '__main__':
    main()
