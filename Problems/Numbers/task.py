import operator
from functools import reduce


def multiply(*nums):
    return reduce(operator.mul, nums)
