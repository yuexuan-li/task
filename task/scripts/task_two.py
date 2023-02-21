#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray

class Subscriber_node:
    def __init__(self):
        self.window_size = 20
        self.window = []
        self.mean = [0.0,0.0,0.0]

        rospy.init_node('subscribernode', anonymous=True)
        rospy.Subscriber('topic', Float32MultiArray, self.callback)
        rospy.spin()

    def callback(self, data):
        self.window.append(data.data)
        if len(self.window) > self.window_size:
            self.window.pop(0)
        for i in range(3):
            self.mean[i] = sum([x[i] for x in self.window]) / len(self.window)
        rospy.loginfo('mean: [%f,%f,%f]', self.mean[0], self.mean[0], self.mean[0])

if __name__ == '__main__':
    Subscriber_node()