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


def main():

    robot = rb.Snatch3rRobot()
    ir_sensor = robot.proximity_sensor
    rc = RemoteControlEtc(robot, ir_sensor, ev3)
    mqtt_client = com.MqttClient(rc)
    mqtt_client.connect_to_pc()

    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak('Hello. How are you')
        time.sleep(0.01)  # For the delegate to do its work


class RemoteControlEtc(object):
    def __init__(self, robot, ir_sensor, ev3):
        self.robot = robot
        self.proximity = ir_sensor
        self.ev3 = ev3
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
        self.robot.drive_system.start_moving(75, 75)
        # robot will drive a certain distance, if any object is detected, it will check the object and determine
        # whether or not it is trash. If it is trash, the robot will pick it up and take it back to start, if not, the
        # robot will pick it up and move it out of the way.






main()