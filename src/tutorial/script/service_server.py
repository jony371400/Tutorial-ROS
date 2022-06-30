#!/usr/bin/env python

from __future__ import print_function
from cgitb import reset

from tutorial.srv import AddTwoInts,AddTwoIntsResponse
from tutorial.srv import Customization,CustomizationResponse

import rospy

def handle_Example_Service(req):
    print('Example Service')
    print('Req =>  ' , req)
    print('Req A =>  ' , req.a)
    print('Req B =>  ' , req.b)

    print('Type Req => ' , type(req))
    print('Type Req A => ' , type(req.a))
    print('Type Req B => ' , type(req.b))

    return AddTwoIntsResponse(req.a + req.b)


def handle_Customization_Service(req):
    print('Custom Service')
    # print('Req =>  ' , req)
    print('Req NAME =>  ' , req.name)
    print('Req AGE =>  ' , req.age)

    # print('Type Req => ' , type(req))
    # print('Type Req NAME => ' , type(req.name))
    # print('Type Req AGE => ' , type(req.age))

    return CustomizationResponse(req.name , req.age)

def Service_Run():
    rospy.init_node('Service_Node')

    example = rospy.Service('Service_Name', AddTwoInts, handle_Example_Service)
    customization = rospy.Service('Custom_Service', Customization, handle_Customization_Service)

    print("Service Ready!")
    rospy.spin()

if __name__ == "__main__":
    Service_Run()