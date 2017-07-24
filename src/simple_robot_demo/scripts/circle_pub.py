#!/usr/bin/env python

__author__ = "Weiyu Xue"
__license__ = "MIT"

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 

# Configurable
circle_radius = 10

def teleop(m):
    msg = Twist()

    pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
    rospy.init_node('teleop', anonymous=True)
    rate = rospy.Rate(10) # Hz
    # With its argument of 10, we should expect to go through the loop 10 times per second
    # (as long as our processing time does not exceed 1/10th of a second!)

    while not rospy.is_shutdown():
        msg.linear.x = 0.04
        msg.linear.z = 0.2
        msg.angular.x = 0.04
        msg.angular.z = 0.5*m
        pub.publish(msg)
        rate.sleep()


if __name__ == '__main__':
    try:
        teleop(circle_radius)
    except rospy.ROSInterruptException:
        pass
