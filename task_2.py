#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_2():
    for i in range (4):
        move_right()
        if i < 3:
            move_down()    
        if i == 1:
            fill_cell()
        else:
            continue

          
if __name__ == '__main__':
    run_tasks()
