"""
CSCI-665 Homework 2: Problem 4
This program is implementation of O(N2 log N) algorithm that finds the
maximum number of pairs of points that can be aligned when the given
paper is folded about any particular line.

author: Kapil Dole (section 03)
author: Chirag Kular (section 01)
"""

def merge(left, right):
    """
    This method merges two sublists and sorts them while doing so, this
    is improved merge method which sorts lists of list.
    :param left: Left sublist.
    :param right: Right sublist.
    :return: Merged sorted list.
    """

    # Initializing pointers.
    leftPtr = 0
    rightPtr = 0
    result = []

    # Merging and sorting two sublists.
    while leftPtr < len(left) and rightPtr < len(right):
        if left[leftPtr][0] < right[rightPtr][0] or \
                (left[leftPtr][0] == right[rightPtr][0] and left[leftPtr][1] < right[rightPtr][1]):
            result.append(left[leftPtr])
            leftPtr += 1
        else:
            result.append(right[rightPtr])
            rightPtr += 1

    # Extending the leftover in the sublists.
    if leftPtr < len(left):
        result.extend(left[leftPtr:])
    elif rightPtr < len(right):
            result.extend(right[rightPtr:])

    return result


def sort(List):
    """
    This method sorts list of list using merge sort, which runs in
    N Log(N) complexity.
    :param List:
    :return:
    """

    if len(List) < 2:
        return List
    else:
        mid = len(List)//2
        leftHalf = sort(List[:mid])
        rightHalf = sort(List[mid:])
        return merge(leftHalf, rightHalf)


def maxAlignPoints(List):
    """
    This method first finds N2 pairs of points and then for each
    pair of points, finds slope of their perpendicular bisector.
    Then it calculates mid point of those points and then calulates
    value of C, using given expression Y = MX + C. Then it sorts all
    these (slope, constant) pair using merge sort and the search for
    maximum number of pairs.
    :param List: Input list of pair of points (x, y)
    :return: Maximum count.
    """

    slopeAndConstPair = []
    # Computing N2 pairs of points.
    for i in range(len(List)-1):
        for j in range(i+1, len(List)):
            x1 = List[i][0]
            y1 = List[i][1]
            x2 = List[j][0]
            y2 = List[j][1]

            # Calculating slope.
            if (x2 - x1) == 0:
                slope = float('inf')
            else:
                slope = float(y2 - y1) / float(x2 - x1)

            # Calculating slope of perpendicular bisector.
            if slope == 0:
                perpendicularSlope = float('inf')
            elif slope == float('inf'):
                perpendicularSlope = 0
            else:
                perpendicularSlope = -1 / slope

            # Calculating value of constant (C).
            midPoint = [(x1 + x2)/2, (y1 + y2)/2]
            C = midPoint[1] - (perpendicularSlope * midPoint[0])
            currentList = [perpendicularSlope, C]
            if perpendicularSlope == float('inf'):
                currentList.pop(1)
                currentList.append(midPoint[0])

            slopeAndConstPair.append(currentList)

    sortedList = sort(slopeAndConstPair)

    # Finding maximum number of pair of points.
    max = 1
    last = sortedList[0]
    count = 1
    for counter in range(1, len(sortedList)):
        if last == sortedList[counter]:
            count += 1
            if count > max:
                max = count
        else:
            count = 1
            last = sortedList[counter]

    return max


def main():
    """
    This is main function of our program, which takes input from standard input.
    the first line contains the value n, followed by n pair of points separated
    by space.
    :return: None.
    """

    n = int(input().strip())
    inputList = []
    for counter in range(n):
        List = input().strip().split(' ')
        inputList.append([int(i) for i in List])

    # Printing maximum count.
    print(maxAlignPoints(inputList))


if __name__ == '__main__':
    main()