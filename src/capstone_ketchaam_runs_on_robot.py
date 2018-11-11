"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

Also: responds to Beacon button-presses by beeping, speaking.

This module runs on the ROBOT.
It uses MQTT to RECEIVE information from a program running on the LAPTOP.

Authors:  David Mutchler, his colleagues, and Alex Ketcham.
"""
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------


import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3



def main():

    robot = rb.Snatch3rRobot()
    print('complete')

    remote = RemoteControl(robot)
    print('complete2')
    client = com.MqttClient(remote)
    print('complete3')
    client.connect_to_pc()
    print('complete4')

    # beacon_test(robot)


class RemoteControl(object):
    def __init__(self, robot):
        """
        :type robot: rb.Snatch3rRobot

        """
        self.robot = robot

    def go_forward(self, speed_string):
        print('all clear')
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

    def down(self):
        print('recieved')
        self.robot.drive_system.start_moving(-100, -100)

    def up(self):
        print('recieved')
        self.robot.drive_system.start_moving(100, 100)

    def right(self):
        print('recieved')
        self.robot.drive_system.spin_in_place_degrees(90)
        self.robot.drive_system.start_moving(100, 100)

    def left(self):
        print('recieved')
        self.robot.drive_system.spin_in_place_degrees(-90)
        self.robot.drive_system.start_moving(100, 100)

def beacon_test(robot):

    while True:

        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep()


        if robot.beacon_button_sensor.is_bottom_blue_button_pressed():
            ev3.Sound.speak('Hello. How are you?')

        time.sleep(0.01)  # For the delegate to do its work




main()

