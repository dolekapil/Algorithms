"""
CSCI-665 Homework 1: Problem 3
This program finds out duplicate element in the sorted list and
it runs in logarithmic time complexity O(Log(N)).

author: Kapil Dole
author: Chirag Kular
"""

def checkDup(list):
    """
    This function finds the duplicate value from the given sorted list and
    returns it in logarithmic time. Here, we have used improved binary search.
    :param list: Input list.
    :return: Duplicate value.
    """

    start = 0
    end = len(list)-1
    while start <= end:
        mid = (start + end) // 2

        if list[mid] == list[mid+1] or list[mid] == list[mid-1]:
            return list[mid]

        if list[mid] == mid:
            start = mid + 1
        else:
            end = mid - 1

def main():
    """
    This is main function of our program, which takes input from standard input.
    the first line contains the value n. Following this are n+2 lines, each line
    containing a single number. In total, the n+2 lines will contain all of the
    numbers in the range [0,n], inclusive, in sorted order.
    :return: None.
    """

    n = int(input().strip())
    inputList = []
    for counter in range(n+2):
        inputList.append(int(input().strip()))

    print(checkDup(inputList))


if __name__ == '__main__':
    main()

