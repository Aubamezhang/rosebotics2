"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Jake Zhang
"""

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import random


def main():

    robot = rb.Snatch3rRobot()
    ir_sensor = robot.proximity_sensor
    arm_and_claw = rb.ArmAndClaw(touch_sensor=1)
    rc = RemoteControlEtc(robot, ir_sensor, ev3, arm_and_claw)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    while True:
        # if robot.beacon_button_sensor.is_top_red_button_pressed():
        #     ev3.Sound.beep()
        # if robot.beacon_button_sensor.is_top_blue_button_pressed():
        #     ev3.Sound.speak('Hello. How are you')
        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEtc(object):
    def __init__(self, robot, ir_sensor, ev3, arm_and_claw):
        self.robot = robot
        self.proximity = ir_sensor
        self.ev3 = ev3
        self.arm = arm_and_claw
        """
        Store the robot.
            :type robot: rb.Snatch3rRobot
        """

    def go_forward(self, speed_string):
        print('Telling the robot to start moving at', speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

    def detect_distance(self, distance_string):
        print('Robot will speak within', distance_string, 'inches to object')
        distance = int(distance_string)
        inches = self.proximity.get_distance_to_nearest_object_in_inches()
        if inches <= distance:
            ev3.Sound.speak('checking object')

    def route1(self):
        print('Robot will move in straight route')
        self.robot.arm.calibrate()
        self.robot.drive_system.move_for_seconds(5, 75, 75)
        while True:
            print(self.proximity.get_distance_to_nearest_object_in_inches())
            time.sleep(.5)
            if self.proximity.get_distance_to_nearest_object_in_inches() <= 2:
                if self.proximity.get_distance_to_nearest_object_in_inches() >= 0:
                    self.robot.arm.raise_arm_and_close_claw()
                    break
        self.robot.drive_system.spin_in_place_degrees(180, 75, 75)
        self.robot.drive_system.move_for_seconds(5, 75, 75)


        # route 1 DONE

    def route2(self):
        print('Robot will move in random route')
        self.robot.arm.calibrate()
        rng_loop = random.randint(2, 6)
        for x in range(rng_loop):
            rng_speed = random.randint(50, 100)
            rng_degrees = random.randint(-180, 180)
            rng_inches = random.randint(3, 20)
            self.robot.drive_system.go_straight_inches(rng_inches, rng_speed, rng_speed)
            self.robot.drive_system.spin_in_place_degrees(rng_degrees, rng_speed, rng_speed)
            time.sleep(1)
            if self.proximity.get_distance_to_nearest_object_in_inches() <= 2:
                if self.proximity.get_distance_to_nearest_object_in_inches() >= .75:
                    self.robot.arm.raise_arm_and_close_claw()
        # route 2 DONE






        # robot will drive a certain distance, if any object is detected, it will be determined as trash and will carry
        # it back to the starting point






main()