#!/usr/bin/env python3

from __future__ import print_function

import sys
import rospy

from tutorial.srv import Customization

def handle_service(x, y):
    rospy.wait_for_service('Custom_Service')
    
    try:
        custom = rospy.ServiceProxy('Custom_Service', Customization)
        response = custom(x, y)
        # print('res : ' , response)
        return ('NAME => ' + response.CustomerName + ' & AGE => ' + str(response.CustomerAge))
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == "__main__":
    print('SYS : ' , sys.argv)
    
    x = sys.argv[1]
    y = int(sys.argv[2])

    print('Para1 : ' , x)
    print('Para2 : ' , y)

    result = handle_service(x, y)
    print("Result : " , result)