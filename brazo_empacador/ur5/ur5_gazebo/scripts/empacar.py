#!/usr/bin/python
#
# Send joint values to UR5 using messages
#

from trajectory_msgs.msg import JointTrajectory
from std_msgs.msg import Header
from trajectory_msgs.msg import JointTrajectoryPoint
from send_gripper import *
from send_joint import *
import time
import rospy


def main():
	# Cube 1 movement
	joint_client([ 0.0 , -2.33      , 1.57, -1.65      , -1.5, 0.4 ]) # Pick and place
	time.sleep(10)
	gripper_client(0.0)                                               # Open gripper
	
	joint_client([ 0.38, -1.05      , 1.1 , -1.65      , -1.5       ,  0.4  ]) # Cube 1
	time.sleep(10)
	gripper_client(0.33) 							   # Close gripper
	time.sleep(10)

	joint_client([ 3.05558558, -1.33789885,  1.46551776, -1.84421309, -1.54632284,1.59]) # Piramidal 1
	time.sleep(10)
	gripper_client(0.0)
	time.sleep(10)

	# Cube 2 movement
	joint_client([ 0.0 , -2.33      , 1.57, -1.65      , -1.5, 0.4 ]) # Pick and place
	time.sleep(10)
	gripper_client(0.0)                                               # Open gripper
	
	joint_client([ 0.155, -1.23375662, 1.4 , -1.82231072, -1.5       ,  0.4  ]) # Cube 2
	time.sleep(10)
	gripper_client(0.33) 							   # Close gripper
	time.sleep(10)

	joint_client([ 2.93, -1.33634549,  1.4638541 , -1.83384003, -1.5,1.59]) # Piramidal 2
	time.sleep(10)
	gripper_client(0.0)
	time.sleep(10)



	# Cube 4 movement
	joint_client([ 0.0 , -2.33      , 1.57, -1.65      , -1.5, 0.4 ]) # Pick and place
	time.sleep(10)
	gripper_client(0.0)                                               # Open gripper
	
	joint_client([-0.34, -1.34      , 1.52, -1.81465917, -1.5       , -0.1  ]) # Cube 4
	time.sleep(10)
	gripper_client(0.33) 							   # Close gripper
	time.sleep(10)

	joint_client([ 3.06, -1.36,  1.37704342, -1.75, -1.65409736,1.59]) # Piramidal 4
	time.sleep(10)
	gripper_client(0.0)
	time.sleep(10)

	# Cube 5 movement
	joint_client([ 0.0 , -2.33      , 1.57, -1.65      , -1.5, 0.4 ]) # Pick and place
	time.sleep(10)
	gripper_client(0.0)                                               # Open gripper
	
	joint_client([-0.57, -1.28      , 1.43, -1.81465917, -1.5       , -0.37 ]) # Cube 5
	time.sleep(10)
	gripper_client(0.33) 							   # Close gripper
	time.sleep(10)

	joint_client([ 3.02, -1.36,  1.36820957, -1.78, -1.75,1.59]) # Piramidal 5
	time.sleep(10)
	gripper_client(0.0)
	time.sleep(10)



	# Pick and place
	joint_client([ 3.1416 , -2.33      , 1.57, -1.65      , -1.5, 0.4 ]) # Pick and place
	time.sleep(10)
	gripper_client(0.0)                                               # Open grippe

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        print ("Program interrupted before completion")
