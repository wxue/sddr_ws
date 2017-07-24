#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 

# Configurable
circle_raidus = 10

def teleop(m):
    msg = Twist()

    pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
    rospy.init_node('teleop', anonymous=True)
    rate = rospy.Rate(10) # Hz
    # With its argument of 10, we should expect to go through the loop 10 times per second
    # (as long as our processing time does not exceed 1/10th of a second!)

    # full stop
    for x in xrange(1,20):
        msg.linear.x = 0.0
        msg.angular.z = 0.0
        pub.publish(msg)
        rate.sleep()

    while not rospy.is_shutdown():
        # msg.linear.x = 0.0
        # msg.angular.z = 2.2
        # pub.publish(msg)
        # rate.sleep()
        # msg.linear.x = 0.2
        # msg.angular.z = 0.2
        # pub.publish(msg)
        # rate.sleep()

        # go straight
        for x in xrange(1,10):
            msg.linear.x = 0.0
            msg.angular.z = 0.2*m
            pub.publish(msg)
            rate.sleep()
        # turn
        for x in xrange(1,5):
            msg.linear.x = 0.05
            msg.angular.z = 0.2*m
            pub.publish(msg)
            rate.sleep()

if __name__ == '__main__':
    try:
        teleop(circle_raidus)
    except rospy.ROSInterruptException:
        pass
