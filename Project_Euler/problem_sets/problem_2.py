"""
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of
the even-valued terms.
"""


###########
# Library #
###########

def new_fibonacci(start, end):
    lst = []
    if start == 0:
        lst = lst + [start] + [1]
    else:
        lst = lst + [start]

    while lst[-1] < end:
        while len(lst) < 2:
            lst = lst + lst[:1]
        lst = lst + [lst[-1] + lst[-2]]
    return lst


def sum_of_even_fibonacci_numbers(lst):
    sum_of_even_fibonacci = sum([i for i in lst if i % 2 == 0])
    return sum_of_even_fibonacci


##########
# Script #
##########

def main():
    start = 0
    end = 4000000
    even_fibs = sum_of_even_fibonacci_numbers(new_fibonacci(start, end))
    print even_fibs


if __name__ == '__main__':
    main()