#! /usr/bin/env python

import rospy
import actionlib
from tutorial.msg import WashTheDishesAction, WashTheDishesFeedback, WashTheDishesResult

class ActionServer():

    def __init__(self):
        self.a_server = actionlib.SimpleActionServer(
            "TopicName", 
            WashTheDishesAction, 
            execute_cb=self.execute_cb, 
            auto_start=False
        )
        
        self.a_server.start()
        print('Action Server Start')

    def execute_cb(self, goal):
        print('Action Execute')
        success = True
        last_dish_washed = ''
        feedback = WashTheDishesFeedback()
        result = WashTheDishesResult()

        print('Feedback : ' , feedback)
        print('Feedback Type : ' , type(feedback))
        print('Result : ' , result)
        print('Result Type : ' , type(result))

        rate = rospy.Rate(1)

        for i in range(0, goal.number_of_minutes):
            if self.a_server.is_preempt_requested():
                self.a_server.set_preempted()
                success = False
                break

            last_dish_washed = 'bowl-' + str(i)
            feedback.last_dish_washed = last_dish_washed
            result.dishes_washed.append(last_dish_washed)

            self.a_server.publish_feedback(feedback)
            print('Feedback : ' , feedback)
            print('Feedback type : ' , type(feedback))

            rate.sleep()
            print('Action Feedback')

        if success:
            self.a_server.set_succeeded(result)
            print('Action Finish')

if __name__ == "__main__":
    rospy.init_node("ActionServer_Node")
    ActionServer = ActionServer()
    rospy.spin()