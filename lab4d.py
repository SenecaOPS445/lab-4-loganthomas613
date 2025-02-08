#!/usr/bin/env python3
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(arg):
    # Place code here - refer to function specifics in section below
    return arg[0:5]
def last_seven(arg):
    # Place code here - refer to function specifics in section below
    return arg[-7:]
def middle_number(arg):
    # Place code here - refer to function specifics in section below
    arg1 = str(arg)
    return arg1[1:3]
def first_three_last_three(arg1, arg2):
    # Place code here - refer to function specifics in section below
    return (arg1[0:3] + arg2[-3:])

if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))