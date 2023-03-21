#!/usr/bin/python3

from pyrob.api import *

@task
def task_8_21():
    if wall_is_above() and wall_is_on_the_left():
        while wall_is_on_the_right() == False:
            move_right()
        while wall_is_beneath() == False:
            move_down()
    elif wall_is_above() and wall_is_on_the_right():
        pass
        while wall_is_on_the_left() == False:
            move_left()
        while wall_is_beneath() == False:
            move_down()
    elif wall_is_beneath() and wall_is_on_the_left():
        while wall_is_on_the_right() == False:
            move_right()
        while wall_is_above() == False:
            move_up()
    else:
        while wall_is_on_the_left() == False:
            move_left()
        while wall_is_above() == False:
            move_up()
if __name__ == '__main__':    
    run_tasks()
