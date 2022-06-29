#! /usr/bin/env python3

import rospy
import actionlib
from tutorial.msg import WashTheDishesAction, WashTheDishesGoal

def feedback_cb(msg):
 print('Feedback received:', msg)

def call_server():

    client = actionlib.SimpleActionClient(
        'wash_dishes_as', 
        WashTheDishesAction
    )

    client.wait_for_server()

    goal = WashTheDishesGoal()
    goal.number_of_minutes = 20

    client.send_goal(goal, feedback_cb=feedback_cb)

    client.wait_for_result()

    result = client.get_result()

    return result

if __name__ == '__main__':

    try:
        rospy.init_node('ActionClient_Node')
        
        print('Action Client Start')
        result = call_server()
        print('Action Client Stop')

    except rospy.ROSInterruptException as e:
        
        print('Something went wrong:', e)