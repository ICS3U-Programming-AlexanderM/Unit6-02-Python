#!/usr/bin/env python3

# Created by: Alexander Matheson
# Created on: Feb 1 2022
# This program generates 10 random numbers
# and finds the largest.
import constant
import random


# function to find the largest number
def find_max_value(rand_list):
    largest = 0
    for counter in range(len(rand_list)):
        if rand_list[counter] > largest:
            largest = rand_list[counter]
    return largest


def main():
    # declare list
    main_list = []
    # generate random numbers
    for counter in range(constant.MAX_SIZE):
        rand = random.randint(constant.MIN_NUM, constant.MAX_NUM)
        main_list.append(rand)
    # display random numbers
    print("The list is: {}". format(main_list))
    # call function to mind max value
    largest_num = find_max_value(main_list)
    # display max value
    print("The largest number is: {}". format(largest_num))


if __name__ == "__main__":
    main()
