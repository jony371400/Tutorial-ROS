#! /usr/bin/env python

import rospy
import actionlib
from tutorial.msg import WashTheDishesAction, WashTheDishesGoal

def feedback_cb(msg):
    print('Feedback received:', msg)

def call_server():

    client = actionlib.SimpleActionClient(
        'TopicName', 
        WashTheDishesAction
    )

    goal = WashTheDishesGoal()
    goal.number_of_minutes = 5

    client.wait_for_server()
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