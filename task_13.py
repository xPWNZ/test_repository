#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    if wall_is_above() == True and wall_is_beneath() == True:
        while wall_is_above() == True:
            move_right()
        move_up()
        while wall_is_on_the_right() == False:
            move_right()
        if wall_is_on_the_right() == True:
            move_left()
            while wall_is_beneath() == True:
                move_left()
            if wall_is_beneath() == False:
                move_down()
                while wall_is_beneath() == True:
                    move_left()
                move_down()
            while wall_is_on_the_right() == False:
                move_right()
            while wall_is_on_the_left() == False:
                move_left()
            while wall_is_above() == True:
                move_right()
            move_up()
            while wall_is_on_the_right() == False:
                move_right()
    elif wall_is_above() == True and wall_is_beneath() == False:
        move_down()
        while wall_is_on_the_right() == False:
            move_right()
        if wall_is_on_the_right() == True:
            move_left
            while wall_is_above() == True:
                move_left()
            move_up()
            while wall_is_above() == True:
                move_left()
            move_up()
            while wall_is_on_the_right() == False:
                move_right()
            while wall_is_on_the_left() == False:
                move_left()
            while wall_is_beneath() == True:
                move_right()
            move_down()
            while wall_is_on_the_right() == False:
                move_right()
    elif wall_is_above() == False and wall_is_beneath() == True:
        move_up()
        while wall_is_on_the_right() == False:
            move_right()
        if wall_is_on_the_right() == True:
            move_left()
            while wall_is_beneath() == True:
                move_left()
            if wall_is_beneath() == False:
                move_down()
                while wall_is_beneath() == True:
                    move_left()
                move_down()
            while wall_is_on_the_right() == False:
                move_right()
            while wall_is_on_the_left() == False:
                move_left()
            while wall_is_above() == True:
                move_right()
            move_up()
            while wall_is_on_the_right() == False:
                move_right()
    else:
        move_up()
        while wall_is_on_the_right() == False:
            move_right()
        if wall_is_on_the_right() == True:
            move_left()
            while wall_is_beneath() == True:
                move_left()
            move_down() 
            while wall_is_beneath() == True:
                move_left()
            move_down()
            while wall_is_on_the_right() == False:
                move_right()
            while wall_is_on_the_left() == False:
                move_left()
            while wall_is_above() == True:
                move_right() 
            move_up()
            while wall_is_on_the_right() == False:
                move_right()
if __name__ == '__main__':
    run_tasks()
