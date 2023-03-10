# Task  
## Installation
Please follow these steps
```
cd catkin_ws/src/task/scripts/
source /opt/ros/noetic/setup.bash
source ~/catkin_ws/devel/setup.bash
~/.bashrc
roscore
. ~/catkin_ws/devel/setup.bash
rosrun task task_one.py 
rosrun task test_publisher.py 
rosrun task task_two.py 
```
## Task1: Write a publisher that publishes an 8-dimensional integers, randomly samples from 0-500  
### Set up
Import the random module to generate random integers, the rospy module for ROS Python programming, and the Int32MultiArray message type from the std_msgs package.  
```
import rospy
import random 
from std_msgs.msg import Int32MultiArray
``` 
```
def publisher():
```
Initialize a ROS node named 'publisher_node' and sets anonymous to True. anonymous=True is used when multiple nodes with the same name are created, which can happen when we run the same node multiple times.
```
rospy.init_node('publisher_node', anonymous=True)
```
Create a publisher object named pub that will publish Int32MultiArray messages on the random_int. The queue_size parameter specifies the maximum number of messages that can be stored in the publisher's outgoing message queue. In this case, we set it to 10.
```
pub = rospy.Publisher('random_int', Int32MultiArray, queue_size=10)
```
With its argument of 10, we should expect to go through the loop 10 times per second.
```
rate = rospy.Rate(10)
```
### Main loop
Create  Int32MultiArray message named int_array and set its data field to a list of 8 random integers.
rate.sleep(), which sleeps just long enough to maintain the desired rate through the loop.
```
while not rospy.is_shutdown():
        int_array = Int32MultiArray()
        for i in range(8):
            int_array.data.append(random.randint(0,500))
        pub.publish(int_array)
        rate.sleep()
```
```
if __name__ == '__main__':
    try:
        publisher()
    except rospy.ROSInterruptException:
        pass
```
This catches a rospy.ROSInterruptException exception, which can be thrown by rospy.sleep() and rospy.Rate.sleep()
## Task2: Write a subscriber with a sliding window to compute the mean of each channel. Window size can be 20 
### Set up
Import the rospy module for ROS Python programming and the Float32MultiArray message type from the std_msgs package.
```
import rospy
import numpy as np
from std_msgs.msg import Float32MultiArray
```
```
window_size = 20
window = []
mean = [0.0, 0.0, 0.0]
```
The callback() function is called every time a new message is received on the topic. We append the message data to the window, and if the window size exceeds window_size, we remove the oldest message from the window and subtract its contribution to each channel sum. We then add the new message's contribution to each channel sum, and compute the mean of each channel in the window by dividing each channel sum by the number of messages in the window.    Finally, we log the means using rospy.loginfo().
 ```
  def callback(data):
    window.append(data.data)
    if len(window) > window_size:
        window.pop(0)
    for i in range(3):
        mean[i] = sum([x[i] for x in window]) / len(window)
    rospy.loginfo('Subscriber: [%f, %f, %f]', mean[0], mean[1], mean[2])
```
Use a sliding window to compute the mean of each channel in the incoming messages. We create a global variable window that will hold the most recent window_size messages, and two global variables self.window and self.mean that will hold the sum and mean of each channel in the window.
```
def SubscriberNode():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('topic', Float32MultiArray, callback)
    rospy.spin()
```
We initialize a ROS node named 'subscribernode' and create a subscriber object that listens for messages on the topic. We use rospy.spin() to keep the subscriber node running and listening for messages.
```
def SubscriberNode():
    rospy.init_node('subscriber_node', anonymous=True)
    rospy.Subscriber('topic', Float32MultiArray, callback)
    rospy.spin()
```

```
if __name__ == '__main__':
    SubscriberNode()

