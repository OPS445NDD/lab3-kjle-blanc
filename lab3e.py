#!/usr/bin/env python3

# Create the list called "my_list" here, not within any function defined below.
my_List = [100, 200, 300, 'six hundred']


def give_list():
    # Returns all of items in the global object my_list unchanged
    return my_List

def give_first_item():
    # Returns the first item in the global object my_list as a string
    return str(my_List[0])

def give_first_and_last_item():
    # Returns a list that includes the first and last items in the global object my_list
    return [my_List[0], my_List[-1]]

def give_second_and_third_item():
    # Returns a list that includes the second and third items in the global object my_list
    return [my_List[1], my_List[2]]

if __name__ == '__main__':
    print(give_list())
    print(give_first_item())
    print(give_first_and_last_item())
    print(give_second_and_third_item())
