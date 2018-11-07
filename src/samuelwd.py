"""
  Capstone Project.  Code written by PUT_YOUR_NAME_HERE.
  Fall term, 2018-2019.
"""

import rosebotics_new as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    #run_test_turn_degrees()
    #run_test_spin_degrees()
    #run_test_ring()
    run_test_ArmAndClaw()

def run_test_spin_degrees():
    robot = rb.Snatch3rRobot()
    robot.drive_system.spin_in_place_degrees(45)
    robot.drive_system.spin_in_place_degrees(-90)

def run_test_turn_degrees():
    robot = rb.Snatch3rRobot()
    robot.drive_system.turn_degrees(90)
    robot.drive_system.turn_degrees(-90)

def run_test_ArmAndClaw():
    robot = rb.Snatch3rRobot()
    print("testing rasie arm close claw")
    robot.arm.raise_arm_and_close_claw(duty_cycle_percent=100)
    print("testing calibrate")
    robot.arm.calibrate()
    print("testing move to position")
    robot.arm.move_arm_to_position(360 * 6.2) #postion in degrees

def run_test_ring():
    robot = rb.Snatch3rRobot()
    while True:
        robot.drive_system.start_moving(30, 30)
        if robot.color_sensor.wait_until_intensity_is_greater_than(10) == True:
            robot.drive_system.spin_in_place_degrees(-50, 100)
main()
