#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
#     while wall_is_above() or wall_is_beneath():
#         move_right()
#         if wall_is_on_the_right():
#             break
#         while not cell_is_filled():
#             fill_cell()
    x=True
    while x==True:
        if wall_is_above()==False:
            fill_cell()
        if wall_is_on_the_right()==False:
            move_right()
        else:
            x=False

if __name__ == '__main__':
    run_tasks()
