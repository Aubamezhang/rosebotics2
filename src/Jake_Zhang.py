"""
  Capstone Project.  Code written by Jake Zhang
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    run_test_wait_until_color_is()
    #run_test_wait_until_pressed()

def run_test_wait_until_color_is():
    robot = rb.Snatch3rRobot()
    color = 'blue'
    robot.color_sensor.wait_until_color_is(color)
    print('STOPPP!')

def run_test_wait_until_pressed():
    robot = rb.Snatch3rRobot()
    robot.touch_sensor.wait_until_pressed()
    print('HOWDY')

main()
