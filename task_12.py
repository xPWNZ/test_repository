#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_6():
    if wall_is_beneath() == True and wall_is_above() == False or cell_is_filled() == True:
        fill_cell()
    while wall_is_on_the_right() == False:
        move_right()
        if wall_is_beneath() == True and wall_is_above() == False or cell_is_filled() == True:
            fill_cell()


if __name__ == '__main__':
    run_tasks()
