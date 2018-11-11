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
from tkinter.ttk import Frame

import rosebotics_new as rb
import time
import mqtt_remote_method_calls as com
import ev3dev.ev3 as ev3
import tkinter
from tkinter import ttk


def main():

    robot = rb.Snatch3rRobot()

    remote = RemoteControl(robot)
    client = com.MqttClient(remote)
    client.connect_to_pc()

    # beacon_test(robot)
    capstone_test(robot)


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

def beacon_test(robot):

    while True:

        if robot.beacon_button_sensor.is_top_red_button_pressed():
            ev3.Sound.beep()


        if robot.beacon_button_sensor.is_bottom_blue_button_pressed():
            ev3.Sound.speak('Hello. How are you?')

        time.sleep(0.01)  # For the delegate to do its work

def capstone_test(robot):
    root = tkinter.Tk()
    frame = ttk.Frame(root, padding=150)
    frame.grid()

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)

    down_arrow = ttk.Button(frame, text='↓', width=20)
    down_arrow.grid(row=1, column=1)
    down_arrow['command'] = (lambda: down(robot))

    up_arrow = ttk.Button(frame, text='↑', width=20)
    up_arrow.grid(row=0, column=1)
    up_arrow['command'] = (lambda: up(robot))

    right_arrow = ttk.Button(frame, text='→', width=20)
    right_arrow.grid(row=1, column=2)
    right_arrow['command'] = (lambda: right(robot))

    left_arrow = ttk.Button(frame, text='←', width=20)
    left_arrow.grid(row=1, column=0)
    left_arrow['command'] = (lambda: left(robot))

    entry_box = ttk.Entry(frame, width=20)
    entry_box.grid(row=2, column=1)
    entry_contents = entry_box.get()

    while True:
        if robot.color_sensor.wait_until_color_is(entry_contents):
            ev3.Sound.speak(entry_contents)
            break
    root.mainloop()

def down(robot):
    robot.DriveSystem.start_moving(-100, -100)

def up(robot):
    robot.DriveSystem.start_moving(100, 100)

def right(robot):
    robot.DriveSystem.spin_in_place_degrees(90)
    robot.DriveSystem.start_moving(100, 100)

def left(robot):
    robot.DriveSystem.spin_in_place_degrees(-90)
    robot.DriveSystem.start_moving(100, 100)

main()

