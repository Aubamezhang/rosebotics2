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


    remote = RemoteControl(robot, ev3)

    client = com.MqttClient(remote)

    client.connect_to_pc()


    run(robot, client)


class RemoteControl(object):
    def __init__(self, robot, ev3):
        """
        :type robot: rb.Snatch3rRobot

        """
        self.robot = robot
        self.ev3 = ev3

    def go_forward(self, speed_string):
        print('all clear')
        speed = int(speed_string)
        self.robot.drive_system.start_moving(speed, speed)

    def down(self):
        print('received')
        self.robot.drive_system.start_moving(-100, -100)

    def up(self):
        print('received')
        self.robot.drive_system.start_moving(100, 100)

    def right(self):
        print('received')
        self.robot.drive_system.spin_in_place_degrees(90)

    def left(self):
        print('received')
        self.robot.drive_system.spin_in_place_degrees(-90)

    def stop(self):
        print('received')
        self.robot.drive_system.stop_moving()

    def upleft(self):
        print('received')
        self.robot.drive_system.spin_in_place_degrees(-45)

    def upright(self):
        print('received')
        self.robot.drive_system.spin_in_place_degrees(45)

    def speak(self, entry):
        print('received')
        self.ev3.Sound.speak(entry)

def run(robot, client):

    while True:

        if robot.proximity_sensor.get_distance_to_nearest_object() < 50:
            ev3.Sound.beep()
            robot.drive_system.move_for_seconds(1, -100, -100)
            robot.drive_system.stop_moving()
            ev3.Sound.speak('Get out of my way!')
            client.send_message('almost')

        if robot.touch_sensor.get_value() == 1:
            ev3.Sound.speak('No! Dont touch that!')
            client.send_message('touch')


        if robot.color_sensor.get_reflected_intensity() > 60:
            ev3.Sound.speak('Its getting pretty bright in hear.')
            client.send_message('bright', robot.color_sensor.get_reflected_intensity())


        time.sleep(0.01)










def beacon_test(robot):

    while True:

        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep()


        if robot.beacon_button_sensor.is_bottom_blue_button_pressed():
            ev3.Sound.speak('Hello. How are you?')

        time.sleep(0.01)  # For the delegate to do its work






main()

