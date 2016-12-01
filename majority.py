"""
CSCI-665 Homework 2: Problem 5
This program is implementation of O(N) algorithm that finds
whether the given list contains a) more than n/2 duplicate
elements. b) more the n/3 duplicate elements. here, we have
implements improved median select algorithm for doing so.

author: Kapil Dole (section 03)
author: Chirag Kular (section 01)
"""

def findMedian(List, k):
    """
    This method is implementation of improved median select
    algorithm, which runs in O(N) time complexity.
    :param List: Input list.
    :param k: K th index.
    :return: K th index median value.
    """

    # Base case.
    if len(List) <= 5:
        List.sort()
        return List[k]

    spiltList = []
    index = 0
    # Splitting input list into sublists, each of length 5.
    while((index+5) <= len(List)):
        spiltList.append(List[index:(index+5)])
        index += 5
    if len(List) % 5 != 0:
        spiltList.append(List[index:])

    # Recursively finding median of each sublist.
    medianList = []
    for eachList in spiltList:
        median = findMedian(eachList, (len(eachList)-1)//2)
        medianList.append(median)

    # Finding median of median list.
    medianOfMedian = findMedian(medianList, (len(medianList)-1)//2)

    leftMedianList = []
    medList = []
    rightMedianList = []

    # splitting values in 3 buckets.
    for num in List:
        if num < medianOfMedian:
            leftMedianList.append(num)
        elif num == medianOfMedian:
            medList.append(num)
        else:
            rightMedianList.append(num)

    # Recursively calling the method if value of k is greater or
    # less that check value, otherwise return median value.
    if k < len(leftMedianList):
        return findMedian(leftMedianList, k)
    elif k >= len(leftMedianList) and k < len(leftMedianList) + len(medList):
        return medianOfMedian
    else:
        return findMedian(rightMedianList, (k-len(leftMedianList)-len(medList)))


def main():
    """
    This is main function of our program, which takes input from standard input.
    the first line contains the value n, which is length of list, followed by
    elements of list separated by space. Once we finds out K th median value
    we check that value in list to make sure, if there are n/2 or n/3 elements
    or not in the given list in O(N) time complexity
    :return: None.
    """

    n = int(input().strip())
    List = input().strip().split(' ')
    inputList = [int(i) for i in List]

    checkHalf = findMedian(inputList, (n-1)//2)

    # Computing occurrence of median value.
    counter = 0
    for num in inputList:
        if num == checkHalf:
            counter += 1

    # Checking if the count is greater than n/2 or n/3.
    if counter > n//2:
        print("YES")
        print("YES")
    else:
        print("NO")
        if counter > n//3:
            print("YES")
        else:
            # Searching in left one third list.
            checkOneThird = findMedian(inputList, (n-1)//3)
            counter = 0
            for num in inputList:
                if num == checkOneThird:
                    counter += 1
            if counter > n//3:
                print("YES")
            else:
                # Searching in right one third list.
                checkOneThird = findMedian(inputList, (2*n-1)//3)
                counter = 0
                for num in inputList:
                    if num == checkOneThird:
                        counter += 1
                if counter > n//3:
                    print("YES")
                else:
                    print("NO")


if __name__ == '__main__':
    main()
