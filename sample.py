__author__ = 'dolek'

def findMedian(sortedList):
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
    list = [1, 1, 1,1,1, 2, 2, 3, 3, 3, 3, 4]
    print(findMedian(list))



if __name__ == '__main__':
    main()