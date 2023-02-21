#!/usr/bin/env python3
import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray

class Publisher_node:
    def __init__(self):
        self.publisher = rospy.Publisher('topic', Float32MultiArray, queue_size=10)
        rospy.init_node('publishernode', anonymous=True)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            data = Float32MultiArray()
            data.data = np.random.rand(3).tolist()
            self.publisher.publish(data)
            rate.sleep()

if __name__ == '__main__':
    Publisher_node()
