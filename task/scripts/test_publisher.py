#!/usr/bin/env python3

import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray

def test_pub():
    rospy.init_node('publisher_node', anonymous=True)
    pub_node = rospy.Publisher('topic', Float32MultiArray, queue_size=10)
    rate = rospy.Rate(10)
    
    while not rospy.is_shutdown():
        data = Float32MultiArray()
        data.data = np.random.rand(3).tolist()
        pub_node.publish(data)
        rospy.loginfo('Published: %s', data)
        rate.sleep()

if __name__ == '__main__':
    try:
        test_pub()
    except rospy.ROSInterruptException:
        pass

