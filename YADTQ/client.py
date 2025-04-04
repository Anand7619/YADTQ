from kafka import KafkaProducer
import sys
import termios
import redis
import json
from config import KAFKA_BROKER_URL,TASK_TOPIC
from backend import ResultBackend
#import os
# import time # uuid,secrets,hashlib

rb = ResultBackend()
producer = KafkaProducer(bootstrap_servers = KAFKA_BROKER_URL,value_serializer = lambda m : json.dumps(m).encode('ascii'))

class TaskIDGenerator:
    def __init__(self, start=1):
        self.counter = start

    def get_task_id(self):
        task_id = f"task{str(self.counter).zfill(3)}"
        self.counter += 1
        return task_id


def submit(task_id_gen) :

    print("\nThe tasks supported by the system are ADD, SUB, and MUL ")
    print("Let your input format be TASK OP1 OP2 (ADD 2 3)\n\n")

    print(" -> ",end="")

    task = ""

    task = input()
    task = task.strip().split(" ")
    op1 = task[1]
    op2 = task[2]

    task = task[0]
    taskId = task_id_gen.get_task_id()


    if len(task) < 3 :
        print("Please enter a task in a valid format....")
        return


    new_task = {
        'taskId' : taskId,
        'task' : task,
        'operand 01' : op1,
        'operand 02' : op2,
        'result' : 'null',
        'status' : 'queued'
    }

    rb.submit_task(taskId,new_task)
    producer.send(TASK_TOPIC,new_task)

    print(f'Task successfully created with the taskId : {taskId}')

    print("\nPlease enter your next task\n")

    return


def query(taskId=""):

    rb.query_tasks(taskId)

    print("\nPlease enter your next task\n")

    return



def __main__() :

    task_id_gen = TaskIDGenerator()

    print(" Client Program......  ")
    print(" Provide the information about the task you want to perform : ")
    print(" 1. Enter             ( Enter tasks.................... )")
    print(" 2. Show-Tasks        ( Show progress.................. )")
    print(" 3. View [taskId]     ( Show progress of one task ..... )")
    print(" 4. Reset             ( Clears all..................... )")
    print(" 5. Exit              ( Terminate......................  ) \n\n")

    proc = ""

    while proc != "quit" :
        print(" -> ",end="")
        proc = input()


        proc = proc.strip().split(" ")
        taskId  = proc[1] if len(proc) >= 2 else ""
        proc = proc[0]

        termios.tcflush(sys.stdin, termios.TCIOFLUSH)
        #os.tcflush(sys.stdin.fileno(), os.TCIOFLUSH)

        if proc == "Enter" :
            submit(task_id_gen)
        elif proc == "Show-Tasks" :
            query()
        elif proc == "View" :
            query(taskId)
        elif proc == "Reset" :
            rb.clear()
        elif proc == "Exit" :
            print("\n\nClient executed successfully.....")
            print("Now aborting.....")
            return
        else :
            print("Provide the correct task")

    rb.clear()


if __name__ == "__main__":
    __main__()
