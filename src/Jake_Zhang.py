"""
  Capstone Project.  Code written by Jake Zhang
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_wait_until_color_is()

def run_test_wait_until_color_is():
    sensor = rb.ColorSensor()
    sensor.wait_until_color_is('black')




main()
