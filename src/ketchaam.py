"""
  Capstone Project.  Code written by Alex Ketcham.
  Fall term, 2018-2019.
"""

import rosebotics as rb
import time


def main():
    """ Runs YOUR specific part of the project """
    robot = rb.Snatch3rRobot()
    robot.drive_system.go_straight_inches(5, 100, rb.StopAction.BRAKE)


main()
