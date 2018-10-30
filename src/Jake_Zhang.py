"""
  Capstone Project.  Code written by Jake Zhang
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    # run_test_wait_until_color_is()
    # run_test_wait_until_pressed()
    # run_test_detect_colors()
    # run_test_ring()

def run_test_wait_until_color_is():
    robot = rb.Snatch3rRobot()
    color = rb.Color.BLACK.value
    if robot.color_sensor.wait_until_color_is(color) == True:
        print('STOP!')

def run_test_wait_until_pressed():
    robot = rb.Snatch3rRobot()
    if robot.touch_sensor.wait_until_pressed() == True:
        print('STOP!')

def run_test_detect_colors():
    robot = rb.Snatch3rRobot()
    color = rb.Color.GREEN.value
    robot.drive_system.start_moving(25, 25)
    if robot.color_sensor.wait_until_color_is(color) == True:
        robot.drive_system.stop_moving()

def run_test_ring():
    robot = rb.Snatch3rRobot()
    while True:
        robot.drive_system.start_moving(30, 30)
        if robot.color_sensor.wait_until_intensity_is_greater_than(10) == True:
            robot.drive_system.spin_in_place_degrees(-50, 100)
main()
