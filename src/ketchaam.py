"""
  Capstone Project.  Code written by Alex Ketcham.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time
import ev3dev.ev3 as ev3

def main():
    """ Runs YOUR specific part of the project """
    # run_test_go_straight_inches()
    # run_test_polygon()
    # run_test_spin_degrees()
    beep_if_blob_is_bigger_than(80)

def run_test_go_straight_inches():
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(10)
    robot.drive_system.go_straight_inches(4)

def run_test_spin_degrees():
    robot = rb.Snatch3rRobot()
    robot.drive_system.spin_in_place_degrees(30)
    robot.drive_system.spin_in_place_degrees(-180)

def run_test_polygon():
    robot = rb.Snatch3rRobot()
    robot.drive_system.polygon(5)
    robot.drive_system.polygon(3)
    robot.drive_system.polygon(4)

def beep_if_blob_is_bigger_than(area):
    robot = rb.Snatch3rRobot()
    robot.drive_system.start_moving(50, 50)
    if robot.camera.get_biggest_blob().get_area() >= area:
        ev3.Sound.beep()
        robot.drive_system.stop_moving()



main()
