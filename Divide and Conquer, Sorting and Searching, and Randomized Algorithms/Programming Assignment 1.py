# -*- coding: utf8 -*-

import sys
import pdb

def Karatsuba(num1: int, num2: int):
    num1 = int(num1)
    num2 = int(num2)
    
    #print(num1, num2)
    #pdb.set_trace()
    num_long = max(len(str(num1)), len(str(num2)))
    num_short = min(len(str(num1)), len(str(num2)))
    if(num_long != num_short):
        #print(num1, num2)
        #pdb.set_trace()
        pass
    first_half = int(num_long / 2)
    second_half = num_long - first_half
    
    if num_short == 1:
        print(num1, "*", num2, "=", num1*num2)
        return num1 * num2
    else:
        num1_part1 = num1 // 10**second_half
        num1_part2 = num1 % 10**second_half
        num2_part1 = num2 // 10**second_half
        num2_part2 = num2 % 10**second_half

        temp_ac = Karatsuba(num1_part1, num2_part1)
##        if(temp_ac != num1_part1 * num2_part1):
##            pdb.set_trace()
        temp_bd = Karatsuba(num1_part2, num2_part2)
##        if(temp_bd != num1_part2 * num2_part2):
##            pdb.set_trace()
        temp_abcd = Karatsuba(num1_part1 + num1_part2, num2_part1 + num2_part2)
##        if(temp_abcd != (num1_part1 + num1_part2) * (num2_part1 + num2_part2)):
##            pdb.set_trace()
        temp_ad_bc = temp_abcd - temp_ac - temp_bd
        result = temp_ac * 10**(2*second_half) + temp_ad_bc * 10**second_half + temp_bd
        print(num1_part1, num1_part2, num2_part1, num2_part2)
        print(num1, "*", num2, "=", result)
##        print(num1, "*", num2, "=", num1 * num2)
##        if(num1* num2 != result):
##            pdb.set_trace()
        return result


if __name__ == '__main__':
    num1 = 3141592653589793238462643383279502884197169399375105820974944592
    num2 = 2718281828459045235360287471352662497757247093699959574966967627
    print(num1, "*", num2, "=", Karatsuba(num1, num2))
