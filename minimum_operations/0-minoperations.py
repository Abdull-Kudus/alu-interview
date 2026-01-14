#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    """
        Calculates the fewest number of operation needed
        to result exactly n H characters in the file
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor  # Use integer division
        divisor += 1

    return operations
