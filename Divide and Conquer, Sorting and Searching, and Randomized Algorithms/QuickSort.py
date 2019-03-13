# -*- coding: utf-8 -*-

import pdb
import sys
import time
import random
import math

global listSort
global compareCount

def Partition(leftIndex: int, rightIndex: int, pivotIndex: int):
    global compareCount
    #pdb.set_trace()
    #print("right:{} - left:{} + lastCount:{} = newCount:{}".format(rightIndex, leftIndex, compareCount, compareCount + rightIndex - leftIndex))
    #print("The pivot element is {}.".format(listSort[pivotIndex]))
    compareCount += rightIndex - leftIndex
    listSort[leftIndex], listSort[pivotIndex] = listSort[pivotIndex], listSort[leftIndex]
    lessPivotIndex = leftIndex + 1
    for i in range(leftIndex + 1, rightIndex + 1):
        if listSort[i] < listSort[leftIndex]:
            listSort[i], listSort[lessPivotIndex] = listSort[lessPivotIndex], listSort[i]
            lessPivotIndex += 1
    listSort[leftIndex], listSort[lessPivotIndex - 1] = listSort[lessPivotIndex - 1], listSort[leftIndex]
    #pdb.set_trace()
    return lessPivotIndex - 1

def MedianOfThree(leftIndex: int, rightIndex: int, middleIndex: int):
    if(listSort[leftIndex] < listSort[middleIndex] < listSort[rightIndex] or listSort[rightIndex] < listSort[middleIndex] < listSort[leftIndex]):
        return middleIndex
    elif(listSort[rightIndex] < listSort[leftIndex] < listSort[middleIndex] or listSort[middleIndex] < listSort[leftIndex] < listSort[rightIndex]):
        return leftIndex
    elif(listSort[leftIndex] < listSort[rightIndex] < listSort[middleIndex] or listSort[middleIndex] < listSort[rightIndex] < listSort[leftIndex]):
        return rightIndex

def QuickSort(leftIndex: int, rightIndex: int):
    global compareCount
    if((rightIndex - leftIndex) <= 1):
        if(rightIndex - leftIndex == 1):
            compareCount += 1
            if(listSort[leftIndex] > listSort[rightIndex]):
                listSort[leftIndex], listSort[rightIndex] = listSort[rightIndex], listSort[leftIndex]
        #print(listSort)
        #print(50 * "=")
        return
    else:
        #pdb.set_trace()
        #random select the pivot in the QuickSort part
        #pivotIndex = random.randint(leftIndex, rightIndex)
        #choose the first element of the part as pivot
        #pivotIndex = leftIndex
        #choose the last element of the part as pivot
        #pivotIndex = rightIndex
        #choose the median element of the part as pivot
        pivotIndex = MedianOfThree(leftIndex, rightIndex, math.floor((leftIndex + rightIndex) // 2))
        #partition the [leftIndex, rightIndex] part into <p----p---->p
        pivotIndexNew = Partition(leftIndex, rightIndex, pivotIndex)
        #divide and conquer two parts
        QuickSort(leftIndex, pivotIndexNew - 1)
        QuickSort(pivotIndexNew + 1, rightIndex)

if __name__ == '__main__':
    listSort = []
    compareCount = 0
    # read data from file
    with open("QuickSort.txt") as f:
        for line in f:
            listSort.append(int(line))
    print("listSort's length is {}.\nThe first 100 elements are {}.".format(len(listSort), listSort[:100]))

    #listSort = [2, 20, 1, 15, 3, 11, 13, 6, 16, 10, 19, 5, 4, 9, 8, 14, 18, 17, 7, 12]
    #pdb.set_trace()
    startTime = time.clock()
    QuickSort(0, len(listSort) - 1)
    print("listSort has been QuickSorted. It takes {} seconds.\nThe first 100 elements are {}.".format(time.clock() - startTime, listSort[:100]))
    print("Totoal comparision number is {}".format(compareCount))
