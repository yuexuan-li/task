#!/usr/bin/env python
import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray

window_size = 20
window = []
mean = [0.0] * 8

def callback(data):
    window.append(data.data)
    if len(window) > window_size:
        window.pop(0)
    for i in range(8):
        mean[i] = sum([x[i] for x in window]) / len(window)
    rospy.loginfo('Subscriber: [%s]', ', '.join(['%.3f' % num for num in mean]))

def SubscriberNode():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('topic', Float32MultiArray, callback)
    rospy.spin()

if __name__ == '__main__':
    SubscriberNode()
