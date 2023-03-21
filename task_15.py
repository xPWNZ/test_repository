#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    mov(8, 8)
if __name__ == '__main__':    
    run_tasks()
