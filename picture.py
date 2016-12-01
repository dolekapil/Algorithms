"""
CSCI-665 Homework 2: Problem 3
This program sorts the people standing for photograph such that 7 year
old students in increasing order of their height followed by teacher
and followed by 8 year old students in decreasing order of their height,
and calculates minimum swaps requires to do so. This is typical example
of counting inversions and we have solved it using divide and conquer
approach with O(N log(N)) complexity.

author: Kapil Dole (section 03)
author: Chirag Kular (section 01)
"""

def sort_and_count(list):
    """
    This method sorts the list in the required order, 7 year old in
    increasing order, teacher and 8 year old in decreasing order, using
    divide and conquer approach, which counts total number of swaps while
    doing so.
    :param list: Input list.
    :return: Sorted list and total number of swaps.
    """

    if len(list) < 2:
        return list, 0
    else:
        mid = len(list)//2
        left, countLeft = sort_and_count(list[:mid])
        right, countRight = sort_and_count(list[mid:])
        mergedList, countMerged = merge(left, right)
        return mergedList, (countLeft + countRight + countMerged)


def merge(left, right):
    """
    This method merges the two sub lists in single list such that, it
    will be sorted in given particular order. ( 7 year - teacher - 8 year ).
    :param left: Left sublist.
    :param right: Right sublist.
    :return: Merged list and total number of swaps.
    """

    # Initializing counter.
    counter = 0
    mergedList = []

    while left and right:
        # When 7 year old student is encountered.
        if left[0][0] == 7:
            if right[0][0] == 7:
                if left[0][1] <= right[0][1]:
                    mergedList.append(left.pop(0))
                else:
                    counter += len(left)
                    mergedList.append(right.pop(0))
            else:
                mergedList.append(left.pop(0))
        # When 8 year old student is encountered.
        elif left[0][0] == 8:
            if right[0][0] == 8:
                if left[0][1] >= right[0][1]:
                    mergedList.append(left.pop(0))
                else:
                    counter += len(left)
                    mergedList.append(right.pop(0))
            else:
                counter += len(left)
                mergedList.append(right.pop(0))
        # When teacher is encountered.
        else:
            if right[0][0] == 7:
                counter += len(left)
                mergedList.append(right.pop(0))
            else:
                mergedList.append(left.pop(0))

    # Appending leftover of left or right sublist.
    if left:
        mergedList.extend(left)
    if right:
        mergedList.extend(right)

    return mergedList, counter


def main():
    """
    This is main function of our program, which takes input from standard input.
    the first line contains the value n, which is odd integer greater than equal
    to 3. This will be followed by n entries for the person's age and his/her height
    separated by space.
    :return: None.
    """

    n = int(input().strip())
    inputList = []
    for counter in range(n):
        entry = input().strip().split()
        inputList.append([int(entry[0]), float(entry[1])])

    sortedList, noOfSwaps = sort_and_count(inputList)
    # Printing total number of swaps required.
    print(noOfSwaps)


if __name__ == '__main__':
    main()
