"""
Mini-application:  Buttons on a Tkinter GUI tell the robot to:
  - Go forward at the speed given in an entry box.

This module runs on your LAPTOP.
It uses MQTT to SEND information to a program running on the ROBOT.

Authors:  David Mutchler, his colleagues, and Alex Ketcham.
"""
# ------------------------------------------------------------------------------
# ------------------------------------------------------------------------------


import tkinter
from tkinter import ttk
import mqtt_remote_method_calls as com
import time



def main():
    """ Constructs and runs a GUI for this program. """
    root = tkinter.Tk()

    server = SERVER()
    client = com.MqttClient(server)
    client.connect_to_ev3()

    # setup_gui(root, client)

    capstone_test(root, client)

    root.mainloop()

class SERVER(object):

    def almost(self):
        print('That was a close call!')

    def touch(self):
        print('No! Dont touch that!')


def capstone_test(root, robot):
    frame = ttk.Frame(root, padding=150)
    frame.grid()

    frame.columnconfigure(0, weight=1)
    frame.columnconfigure(1, weight=1)
    frame.columnconfigure(2, weight=1)
    frame.columnconfigure(3, weight=1)
    frame.rowconfigure(0, weight=1)
    frame.rowconfigure(1, weight=1)
    frame.rowconfigure(2, weight=1)
    frame.rowconfigure(3, weight=1)
    down_arrow = ttk.Button(frame, text='↓', width=20)
    down_arrow.grid(row=1, column=1)
    down_arrow['command'] = (lambda: robot_down(robot))

    up_arrow = ttk.Button(frame, text='↑', width=20)
    up_arrow.grid(row=0, column=1)
    up_arrow['command'] = (lambda: robot_up(robot))

    right_arrow = ttk.Button(frame, text='→', width=20)
    right_arrow.grid(row=1, column=2)
    right_arrow['command'] = (lambda: robot_right(robot))

    left_arrow = ttk.Button(frame, text='←', width=20)
    left_arrow.grid(row=1, column=0)
    left_arrow['command'] = (lambda: robot_left(robot))

    stop = ttk.Button(frame, text='STOP', width=50)
    stop.grid(row=3, column=3)
    stop['command'] = (lambda: robot_stop(robot))

    entry_box = ttk.Entry(frame, width=20)
    entry_box.grid(row=2, column=1)


    root.mainloop()





def robot_down(robot):
    robot.send_message('down')
    print('sent')

def robot_up(robot):
    robot.send_message('up')
    print('sent')

def robot_right(robot):
    robot.send_message('right')
    print('sent')

def robot_left(robot):
    robot.send_message('left')
    print('sent')

def robot_stop(robot):
    robot.send_message('stop')
    print('sent')













def setup_gui(root_window, client):
    """ Constructs and sets up widgets on the given window. """
    frame = ttk.Frame(root_window, padding=10)
    frame.grid()

    speed_entry_box = ttk.Entry(frame)
    go_forward_button = ttk.Button(frame, text="Go forward")

    speed_entry_box.grid()
    go_forward_button.grid()

    go_forward_button['command'] = \
        lambda: handle_go_forward(speed_entry_box, client)


def handle_go_forward(entry_box, client):
    """
    Tells the robot to go forward at the speed specified in the given entry box.
    """
    speed_string = entry_box.get()
    print('sending message')
    client.send_message('go_forward', [speed_string])

main()
