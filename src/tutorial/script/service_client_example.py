#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy

from tutorial.srv import AddTwoInts

def handle_service(x, y):
    rospy.wait_for_service('Service_Name')
    
    try:
        add_two_ints = rospy.ServiceProxy('Service_Name', AddTwoInts)
        resp1 = add_two_ints(x, y)
        return resp1.sum
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    print('SYS : ' , sys.argv)
    
    x = int(sys.argv[1])
    y = int(sys.argv[2])

    print('Para1 : ' , x)
    print('Para2 : ' , y)

    result = handle_service(x, y)
    print("Result : " , result)