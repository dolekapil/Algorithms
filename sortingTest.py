"""
CSCI-665 Homework 1: Problem 5
This program compare the running times of the three algorithms,
Merge Sort, Insertion Sort and Bucket Sort, across all dierent inputs.

author: Kapil Dole
author: Chirag Kular
"""

import math
from node import Node
import random
import time

def InsertionSort(list):
    """
    This function is implementation of Insertion sort algorithm, where
    we try to keep each sub list sorted as we traverse through list.
    Its time complexity is O(N2).
    :param list: Unsorted list.
    :return: Sorted list.
    """

    for counter in range(1, len(list)):
        val = list[counter]
        index = counter
        while index > 0 and list[index-1] > val:
            list[index] = list[index-1]
            index -= 1
        list[index] = val

    return list


def BucketSort(list):
    """
    This program is implementation of bucket sort, where we will be inserting
    elements in the buckets and sort each bucket using insertion sort and finally
    append all the buckets. Running time complexity of bucket sort is O(N) in ideal
    case.
    :param list: Unsorted List
    :return: First node of sorted linked list.
    """

    n = len(list)
    # Initializing buckets.
    buckets = [None for counter in range(n)]

    # Inserting values into buckets.
    for counter in range(n):
        loc = math.floor(n*list[counter])
        if buckets[loc] is None:
            buckets[loc] = Node(list[counter])
        else:
            insertInBucket(buckets[loc], Node(list[counter]))

    # Sorting each bucket using insertion sort.
    for counter in range(n):
        sortedBucket = insertionSortOnBucket(buckets[counter])
        buckets[counter] = sortedBucket

    # Concatenating all sorted buckets.

    result = []

    for counter in range(n):
        if buckets[counter] is not None:
            current = buckets[counter]
            while current is not None:
                result.append(current.value)
                current = current.next

    return result


def insertionSortOnBucket(node):
    """
    This function implements insertion sort on linked list.
    :param node: Head node of bucket.
    :return: Head node for sorted bucket.
    """

    if node is None:
        return

    sortedList = node
    node = node.next
    sortedList.next = None

    while node is not None:
        currentNode = node
        node = node.next

        if currentNode.value < sortedList.value:
            currentNode.next = sortedList
            sortedList = currentNode
        else:
            searchNode = sortedList
            while searchNode.next is not None and currentNode.value > searchNode.next.value:
                searchNode = searchNode.next

            currentNode.next = searchNode.next
            searchNode.next = currentNode

    return sortedList


def insertInBucket(firstNode, currentNode):
    """
    This function inserts value into bucket, if bucket is empty then
    it will add value to it otherwise it will chain to existing list.
    :param firstNode: Existing value in the bucket.
    :param currentNode: New value to add to bucket.
    :return:
    """

    if firstNode is None:
        return

    while firstNode.next != None:
        firstNode = firstNode.next

    firstNode.next = currentNode


def MergeSort(list):
    """
    This function if Merge sort implementation, where we split
    the input list into n lists and sort them while merging them.
    Time complexity of merge sort is O(N log(N)).
    :param list: Unsorted input list.
    :return: Sorted list.
    """

    if len(list) < 2:
        return list
    else:
        mid = len(list)//2
        leftHalf = MergeSort(list[:mid])
        rightHalf = MergeSort(list[mid:])

        return Merge(leftHalf, rightHalf)


def Merge(left, right):
    """
    This function merges two lists into single list and while doing
    so, it will sort the list and return single sorted list.
    :param left: Left half of unsorted list.
    :param right: Right half of unsorted list.
    :return: Merged sorted list.
    """
    leftPtr = 0
    rightPtr = 0
    result = []

    while leftPtr < len(left) and rightPtr < len(right):
        if left[leftPtr] < right[rightPtr]:
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


def testUniformDistribution():
    """

    :return:
    """

    a = 0
    b = 1
    print("Testing the algorithms on random floating point numbers with a uniform distribution in the range [0; 1).")
    print("For N = 10")
    # when n = 10
    test1 = []
    for counter in range(10):
        test1.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test1)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test1)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test1)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n")


    print("For N = 100")
    # when n = 100
    test2 = []
    for counter in range(100):
        test2.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test2)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test2)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test2)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n")


    print("For N = 1000")
    # when n = 1000
    test3 = []
    for counter in range(1000):
        test3.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test3)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test3)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test3)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n")

    print("For N = 10000")
    # when n = 10000
    test4 = []
    for counter in range(10000):
        test4.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test4)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test4)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test4)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n")


    print("For N = 100000")
    # when n = 100000
    test5 = []
    for counter in range(100000):
        test5.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test5)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test5)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test5)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n")


    print("For N = 1000000")
    # when n = 1000000
    test6 = []
    for counter in range(1000000):
        test6.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test6)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test6)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test6)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n\n")


def testGaussianDistribution():
    print("Testing the algorithms on random floating point numbers with a uniform distribution in the range [0; 1).")
    print("For N = 10")
    # when n = 10
    test1 = []
    for counter in range(10):
        test1.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test1)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test1)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test1)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n")


    print("For N = 100")
    # when n = 100
    test2 = []
    for counter in range(100):
        test2.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test2)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test2)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test2)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n")


    print("For N = 1000")
    # when n = 1000
    test3 = []
    for counter in range(1000):
        test3.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test3)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test3)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test3)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n")

    print("For N = 10000")
    # when n = 10000
    test4 = []
    for counter in range(10000):
        test4.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test4)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test4)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test4)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n")


    print("For N = 100000")
    # when n = 100000
    test5 = []
    for counter in range(100000):
        test5.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test5)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test5)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test5)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n")


    print("For N = 1000000")
    # when n = 1000000
    test6 = []
    for counter in range(1000000):
        test6.append(random.uniform(0,1))

    print("Insertion Sort:")
    start_time = time.time()
    InsertionSort(test6)
    time_insertion = time.time() - start_time
    print("Time:"+str(time_insertion)+" seconds.")

    print("Merge Sort:")
    start_time = time.time()
    MergeSort(test6)
    time_merge = time.time() - start_time
    print("Time:"+str(time_merge)+" seconds.")

    print("Bucket Sort:")
    start_time = time.time()
    BucketSort(test6)
    time_bucket = time.time() - start_time
    print("Time:"+str(time_bucket)+" seconds.\n\n")

def main():
    """
    This is main function of our program which makes calls
    to different test function for comparing between different
    sorting algorithms.
    :return: None.
    """

    testUniformDistribution()
    testGaussianDistribution()



if __name__ == '__main__':
    main()