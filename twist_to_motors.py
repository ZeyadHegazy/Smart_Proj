#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Float32

h = 0

def callback(data):
	x = data.linear.x
	y = data.linear.y
	z = data.angular.z
	global h
	h = x + y + z

if __name__ == '__main__':
#	try:
	while not rospy.is_shutdown():
		rospy.init_node('zoz', anonymous = True)
		pub = rospy.Publisher("motor1_vel" , Float32 , queue_size = 10)
		rospy.Subscriber("cmd_vel" , Twist , callback)
		pub.publish (not h)
		rospy.Rate(10).sleep()
#		print (h)
#	except rospy.ROSInterruptException:
#		pass
