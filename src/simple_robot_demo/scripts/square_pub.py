#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist 

# Configurable
square_side_length = 1

def teleop(m):
    msg = Twist()

    pub = rospy.Publisher('/cmd_vel_mux/input/teleop', Twist, queue_size=10)
    rospy.init_node('teleop', anonymous=True)
    rate = rospy.Rate(50) # Hz
    # With its argument of 10, we should expect to go through the loop 10 times per second
    # (as long as our processing time does not exceed 1/10th of a second!)
    while not rospy.is_shutdown():
        # full stop
        for x in xrange(1,100):
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            # rospy.loginfo(msg)
            pub.publish(msg)
            rate.sleep()
        # go straight
        for x in xrange(1,300*m):
            msg.linear.x = 0.0
            msg.angular.z = 2.2
            # rospy.loginfo(msg)
            pub.publish(msg)
            rate.sleep()
        # full stop
        for x in xrange(1,100):
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            # rospy.loginfo(msg)
            pub.publish(msg)
            rate.sleep()
        # turn
        for x in xrange(1,45):
            msg.linear.x = 0.2
            msg.angular.z = 0.2
            # rospy.loginfo(msg)
            pub.publish(msg)
            rate.sleep()

if __name__ == '__main__':
    try:
        teleop(square_side_length)
    except rospy.ROSInterruptException:
        pass
