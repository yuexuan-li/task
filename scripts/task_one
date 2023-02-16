#!/usr/bin/env python3
import rospy
import random
from std_msgs.msg import Int32MultiArray

def publisher():
    rospy.init_node('publisher_node', anonymous=True)
    pub = rospy.Publisher('random_int', Int32MultiArray, queue_size=10)
    rate = rospy.Rate(10)
    
    # int_array = Int32MultiArray()
    # int_array.data = [random.randint(0,500) for i in range(8)]

    while not rospy.is_shutdown():
        int_array = Int32MultiArray()
        for i in range(8):
            int_array.data.append(random.randint(0,500))
        pub.publish(int_array)
        rate.sleep()

if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
