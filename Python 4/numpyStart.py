"""
Topic: Numpy
Date: 22/04/2024
Author: Tom@CODEKIDS
"""

import numpy as np


def ShowInformation():
    print(f'Numpy Version: {np.__version__}')  # np.__version__ shows the current numpy version
    print('\nConfig Settings:')  # \n creates a new line.
    print(np.show_config())  # show_config() shows the current numpy configuration


def ContainsAZero(array: np.array):
    return not np.all(array)


if __name__ == '__main__':
    ShowInformation()

    myFirstArray = np.array([1, 2, 3, 4])
    print(f'Array: {myFirstArray}')
    print(f'Contains a Zero: {ContainsAZero(myFirstArray)}')

    mySecondArray = np.array([0, 1, 2, 3])
    print(f'Array: {mySecondArray}')
    print(f'Contains a Zero: {ContainsAZero(mySecondArray)}')
    