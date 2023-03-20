#!/usr/bin/python3

from pyrob.api import *


def cell_box():
    if wall_is_above() == False and wall_is_beneath() == False or cell_is_filled() == True:
        fill_cell()


def run_right():
    cell_box()
    while wall_is_on_the_right() == False:
        move_right()
        cell_box()


def run_left():
    while wall_is_on_the_right == True:
        move_left()


def up_down():
    if wall_is_above() == True or wall_is_beneath() == False:
        move_down()
    elif wall_is_above() == False or wall_is_beneath() == True:
        move_up()


@task
def task_8_10():
    up_down()


if __name__ == '__main__':
    run_tasks()
