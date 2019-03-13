# -*- coding: utf-8 -*-

import pdb
import sys
import time
import random
import math

def Partition(leftIndex: int, rightIndex: int, pivotIndex: int):
    global compareCount
    #pdb.set_trace()
    #print("right:{} - left:{} + lastCount:{} = newCount:{}".format(rightIndex, leftIndex, compareCount, compareCount + rightIndex - leftIndex))
    #print("The pivot element is {}.".format(listSort[pivotIndex]))
    #compareCount += rightIndex - leftIndex
    listSelect[leftIndex], listSelect[pivotIndex] = listSelect[pivotIndex], listSelect[leftIndex]
    lessPivotIndex = leftIndex + 1
    for i in range(leftIndex + 1, rightIndex + 1):
        if listSelect[i] < listSelect[leftIndex]:
            listSelect[i], listSelect[lessPivotIndex] = listSelect[lessPivotIndex], listSelect[i]
            lessPivotIndex += 1
    listSelect[leftIndex], listSelect[lessPivotIndex - 1] = listSelect[lessPivotIndex - 1], listSelect[leftIndex]
    #pdb.set_trace()
    return lessPivotIndex - 1

def RSelect(leftIndex: int, rightIndex: int, ithOrder: int):
    if(rightIndex == leftIndex):
        return leftIndex
    else:
        #random select the pivot in the QuickSort part
        pivotIndex = random.randint(leftIndex, rightIndex)
        print("In {} find the {}th-order element. The cur-pivot is {}".format(listSelect[leftIndex : rightIndex + 1], ithOrder, listSelect[pivotIndex]))
        #pdb.set_trace()
        pivotIndexNew = Partition(leftIndex, rightIndex, pivotIndex)
        if(pivotIndexNew - leftIndex + 1 > ithOrder): #the ithOrder element falls in 1st part
            return RSelect(leftIndex, pivotIndexNew - 1, ithOrder)
        elif(pivotIndexNew - leftIndex + 1 == ithOrder): #the ithOrder element is the pivot
            return pivotIndexNew
        elif(pivotIndexNew - leftIndex + 1 < ithOrder): #the ithOrder element falls in 2nd part
            return RSelect(pivotIndexNew + 1, rightIndex, ithOrder - (pivotIndexNew - leftIndex + 1))

if __name__ == "__main__":
    listSelect = [2, 100, 45, 6, 3, 1, 20, 9, 7, 4, 56, 8, 10, 5]
    #ithOrder = random.randint(1, len(listSelect))
    ithOrder = 12
    print("The list is {}. Search the {}th element.".format(listSelect, ithOrder))
    ithIndex = RSelect(0, len(listSelect) - 1, ithOrder)
    print("The {}th element is {}.".format(ithOrder, listSelect[ithIndex]))
    print(listSelect)
