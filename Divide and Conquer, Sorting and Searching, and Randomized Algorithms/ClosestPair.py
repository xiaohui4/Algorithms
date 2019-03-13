# -*- coding = utf-8 -*-

import pdb
import sys
import MergeSort

global pointsSortX
global pointsSortY

def Distance(point1: tuple, point2: tuple):
    return (point1[0]-point2[0]) ** 2 + (point1[1] - point2[1]) ** 2

def ClosestPair(points: list):
    points_num = len(points)
    minimumDis = None
    closestPair = None
    if points_num <= 3: # base condition 2 or 3 points
        #pdb.set_trace()
        for i in range(points_num):
            for j in range(i + 1, points_num):
                temp_dis = Distance(points[i], points[j])
                if ((minimumDis is None) or (temp_dis < minimumDis)):
                    minimumDis = temp_dis
                    closestPair = (points[i], points[j])
        print("Brute force for {}. Closest-pair: {}. Distance is {}.".format(points, closestPair, minimumDis))
        return (closestPair, minimumDis)
    else: # general condition recursively get closestpair and distance
        #pdb.set_trace()
        left_points = points[:points_num // 2]
        right_points = points[points_num // 2 :]
        print("{} is divided into two parts: {} and {}.".format(points, left_points, right_points))
        leftClosestPair, leftMinimumDis = ClosestPair(left_points)
        rightClosestPair, rightMinimumDis = ClosestPair(right_points)
        splitClosestPair, splitMinimumDis = ClosestSplitPair(points, min(leftMinimumDis, rightMinimumDis))
        if splitClosestPair is not None:
            minimumDis = min(leftMinimumDis, rightMinimumDis, splitMinimumDis)
            if minimumDis == leftMinimumDis:
                closestPair = leftClosestPair
            elif minimumDis == rightMinimumDis:
                closestPair = rightClosestPair
            elif minimumDis == splitMinimumDis:
                closestPair = splitMinimumDis
        else:
            minimumDis = min(leftMinimumDis, rightMinimumDis)
            if minimumDis == leftMinimumDis:
                closestPair = leftClosestPair
            elif minimumDis == rightMinimumDis:
                closestPair = rightClosestPair
        
        print(100 * "-")
        print("Recursive method for general case: {}. The closest-pair is {} and their distance is {}.".format(points, closestPair, minimumDis))
        print(100 * "-")
        return (closestPair, minimumDis)

def ClosestSplitPair(points: list, delta: float):
    # select the points whose x-coordinate fall into [x_bar - delta, x_bar + delta]
    xbar = points[len(points) // 2][0]
    xbar_minus_delta = xbar - delta
    xbar_plus_delta = xbar + delta
    pointsSortX_temp = []
    for index, value in enumerate(pointsSortX):
        if xbar_minus_delta <= value[0] <= xbar_plus_delta:
            pointsSortX_temp.append(value)

    # sort them according to their y-coordinate
    pointsSortY_temp = []
    for element in pointsSortY:
        if element in pointsSortX_temp:
            pointsSortY_temp.append(element)
            
    if len(pointsSortY_temp) == 1: # x-coordinate area is very shallow, just one point
        return (None, None)
    else:
        # brute force search the nearest point in the near 7 points
        minimumDis = None
        closestPair = None
        for i in range(len(pointsSortY_temp)):
            for j in range(i + 1, min(i + 8, len(pointsSortY_temp))):
                temp_dis = Distance(pointsSortY_temp[i], pointsSortY_temp[j])
                if (minimumDis is None) or (temp_dis < minimumDis):
                    minimumDis = temp_dis
                    closestPair = (pointsSortY_temp[i], pointsSortY_temp[j])
        return (closestPair, minimumDis)

def MergeSortPoints(list_sort: list, axis: str): # each element is a tuple meaning 2D coordinates
    list_length = len(list_sort)
    axis_index = 0 if axis == "x" else 1

    if list_length == 1:
        return list_sort
    else:
        result = []
        first_half = MergeSortPoints(list_sort[:list_length // 2], axis)
        second_half = MergeSortPoints(list_sort[list_length // 2 :], axis)
        loop_num = max(len(first_half), len(second_half))

        j, k = (0, 0)
        for i in range(list_length):
            if j == len(first_half):
                result.append(second_half[k])
                k += 1
                continue
            if k == len(second_half):
                result.append(first_half[j])
                j += 1
                continue
            if first_half[j][axis_index] < second_half[k][axis_index]:
                result.append(first_half[j])
                j += 1
            else:
                result.append(second_half[k])
                k += 1
        #print(result)
        return result


if __name__ == "__main__":
    points = [(0, 0), (0.2, 0.27), (1, 5), (1.5, 2), (2.4, 2.2), (2.45, 4.3), (2.9, 1), (3.3, 4.9), (3.5, 0.1), (4, 2.9), (4.2, 0.31), (4.9, 4.7)]
    pointsSortX = MergeSortPoints(points, "x")
    pointsSortY = MergeSortPoints(points, "y")
    print("Points sorted by x is: {}.".format(pointsSortX))
    print("Points sorted by y is: {}.\n\n\n".format(pointsSortY))
    #pdb.set_trace()
    closestpair, delta = ClosestPair(pointsSortX)
    print(closestpair, delta)
