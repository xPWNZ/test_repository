#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    if wall_is_beneath() and wall_is_above() or cell_is_filled():
        fill_cell()
    while wall_is_on_the_right() == False:
        move_right()
        if wall_is_beneath() and wall_is_above() or cell_is_filled():
            fill_cell()

if __name__ == '__main__':
    run_tasks()
