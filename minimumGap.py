"""
CSCI-665 Homework 3: Problem 4
This program solves "minimize gaps" interval scheduling problem using
dynamic programming. Running time for the algorithm is O(N2).

author: Kapil Dole
author: Chirag Kular
"""

def sortByfinishTime(list):
    """
    This function sorts the given intervals by their finishing time.
    It uses merge sort logic and hence its complexity is O(N log N).
    :param list: List of intervals.
    :return: Sorted list of intervals by their finish time.
    """
    if len(list) < 2:
        return list
    else:
        mid = len(list)//2
        leftHalf = sortByfinishTime(list[:mid])
        rightHalf = sortByfinishTime(list[mid:])

        return Merge(leftHalf, rightHalf)


def Merge(left, right):
    """
    This function merges two lists into single list and while doing
    so, it will sort the list and return single sorted list.
    :param left: Left half of unsorted list of intervals.
    :param right: Right half of unsorted list of intervals.
    :return: Merged sorted list of intervals.
    """
    leftPtr = 0
    rightPtr = 0
    result = []

    while leftPtr < len(left) and rightPtr < len(right):
        if left[leftPtr][1] < right[rightPtr][1]:
            result.append(left[leftPtr])
            leftPtr += 1
        else:
            result.append(right[rightPtr])
            rightPtr += 1

    if leftPtr < len(left):
        result.extend(left[leftPtr:])
    elif rightPtr < len(right):
            result.extend(right[rightPtr:])
    return result


def computeP(list):
    """
    This function calculates value of P for each of interval,
    which gives largest index of interval i < j such that
    interval i is compatible with j. Running time of the given
    logic is O(N2).
    :param list: Sorted list of intervals.
    :return: list containing P values for each interval.
    """
    P = []
    P.append(0)
    for counter in range(1, len(list)):
        currentPtr = counter - 1
        maxIndex = 0
        while(currentPtr >= 0):
            if list[counter][0] >= list[currentPtr][1]:
                maxIndex = currentPtr + 1
                break
            currentPtr -= 1
        P.append(maxIndex)
    return P


def findMinimumGap(n, start, finish, StartFinish):
    """
    This function computes non overlapping intervals such that, they
    are having minimum gaps between them and returns the minimum gap
    value. Running time for this logic is O(N2).
    :param n: Total number of intervals.
    :param start: Global start time.
    :param finish: Global finish time.
    :param StartFinish: List containing start-finish time for intervals.
    :return: Minimum gap value rounded to nearest integer.
    """
    sorted = sortByfinishTime(StartFinish)
    P = computeP(sorted)
    S = [0 for _ in range(n + 1)]
    # Iterative loop.
    for index in range(1, n + 1):
        # Taking max of two values.
        S[index] = max(S[P[index - 1]] + sorted[index - 1][1] - sorted[index - 1][0], S[index - 1])
    # Returning minimum gap value.
    return round(finish - start - S[n])


def main():
    """
    This is main function of our program which takes input from
    standard input and runs interval scheduling algorithm on them.
    :return: None.
    """
    n = int(input().strip())
    inpt = input().strip().split(' ')
    start = float(inpt[0])
    finish = float(inpt[1])
    StartFinish = []
    for counter in range(n):
        temp = input().strip().split(' ')
        StartFinish.append([float(val) for val in temp])
    print(findMinimumGap(n, start, finish, StartFinish))


if __name__ == '__main__':
    main()
