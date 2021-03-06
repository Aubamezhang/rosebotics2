"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Samuel Dickinson.
"""

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3


def main():
    robot = rb.Snatch3rRobot()
    remote_control = RemoteControlEtc(robot)
    mqtt_client = com.MqttClient(remote_control)
    mqtt_client.connect_to_pc()

    while True:
        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep()
        if robot.beacon_button_sensor.is_top_blue_button_pressed():
            ev3.Sound.speak("Hello, How are you?")
        time.sleep(0.01)  # For the delegate to do its work

class RemoteControlEtc(object):
    def __init__(self, robot):
        '''
        Stores the robot.
            :type robot: rb.Snatch3rRobot
        '''
        self.robot = robot

    def go_forward(self,speed_string):
        '''Makes the robot go forward at the given speed'''
        print("Telling the robot to start moving at ", speed_string)
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)


main()