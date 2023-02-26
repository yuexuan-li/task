#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray

window_size = 20
window = []
mean = [0.0, 0.0, 0.0]

def callback(data):
    window.append(data.data)
    if len(window) > window_size:
        window.pop(0)
    for i in range(3):
        mean[i] = sum([x[i] for x in window]) / len(window)
    rospy.loginfo('Subscriber: [%f, %f, %f]', mean[0], mean[1], mean[2])

def SubscriberNode():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('topic', Float32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    SubscriberNode()
