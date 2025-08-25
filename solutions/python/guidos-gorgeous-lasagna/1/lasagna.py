"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""

#CONSTANTS
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2


def bake_time_remaining(elapsed_bake_time):
    """Calculates the time left for the Lasagna to be ready.
    :param elapsed_bake_time: int -> the time currently spent in baking
    :return: int -> the time left for Lasagna to be ready
    """
    return EXPECTED_BAKE_TIME-elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):
    """Calculates the time needed to prepare the slices of Lasagna.
    :param number_of_layers: int -> the number of layers of lasagna
    :return: int -> the time needed to prepare all slices
    """
    return number_of_layers*PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculates the total time elapsed in preparing and cooking Lasagna
    :param1 number_of_layers:int -> the number of layers of lasagna
    :param2 elapsed_bake_time:int -> time spent in baking lasagna
    :return: int -> total time elapsed while making lasagna
    """
    return (number_of_layers*PREPARATION_TIME) + elapsed_bake_time

