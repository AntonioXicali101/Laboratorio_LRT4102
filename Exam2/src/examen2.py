#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import random
import time

class TurtleSimDetection:
    def __init__(self):
        rospy.init_node('turtlesim_detection_precision', anonymous=True)
        
        # Publisher to move turtle
        self.vel_pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        
        # Subscriber to get turtle position (simulate sensor)
        rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        
        self.current_pose = None
        
        # Simulation parameters
        self.debris_positions = self.generate_debris(10)  # 10 debris items (x,y)
        self.detected_positions = []
        self.false_positives = 0
        
        self.detection_radius = 1.0  # Radius within which detection counts as true positive
        
        self.rate = rospy.Rate(10)  # 10 Hz
        
        # Metrics counters
        self.true_positives = 0
        self.false_positives = 0
        
    def generate_debris(self, count):
        # Generate random debris positions within the turtlesim window (1-10)
        debris = []
        for _ in range(count):
            x = random.uniform(1, 10)
            y = random.uniform(1, 10)
            debris.append((x, y))
        rospy.loginfo(f"Generated debris positions: {debris}")
        return debris
    
    def pose_callback(self, msg):
        self.current_pose = msg
        
    def detect_debris(self):
        # Simulate detection based on distance to debris
        if self.current_pose is None:
            return
        
        detected_now = False
        
        for debris_pos in self.debris_positions:
            dist = ((self.current_pose.x - debris_pos[0])**2 + (self.current_pose.y - debris_pos[1])**2)**0.5
            if dist <= self.detection_radius and debris_pos not in self.detected_positions:
                self.detected_positions.append(debris_pos)
                self.true_positives += 1
                rospy.loginfo(f"True positive detected at {debris_pos}")
                detected_now = True
        
        # Simulate some false positives randomly
        if random.random() < 0.05:  # 5% chance per cycle of false positive detection
            self.false_positives += 1
            rospy.loginfo("False positive detected")
            detected_now = True
        
        return detected_now
    
    def move_turtle_randomly(self):
        # Random walk movement to explore environment
        move_cmd = Twist()
        move_cmd.linear.x = random.uniform(0.5, 1.5)
        move_cmd.angular.z = random.uniform(-1.0, 1.0)
        self.vel_pub.publish(move_cmd)
        
    def calculate_precision(self):
        if self.true_positives + self.false_positives == 0:
            return 0.0
        return self.true_positives / (self.true_positives + self.false_positives)
    
    def run(self):
        start_time = rospy.Time.now()
        duration = rospy.Duration(60)  # Run simulation for 60 seconds
        
        while not rospy.is_shutdown() and rospy.Time.now() - start_time < duration:
            self.move_turtle_randomly()
            self.detect_debris()
            self.rate.sleep()
        
        precision = self.calculate_precision()
        rospy.loginfo(f"Detection Precision: {precision:.2f}")
        print(f"Final Detection Precision: {precision:.2f}")
        print(f"True Positives: {self.true_positives}")
        print(f"False Positives: {self.false_positives}")

if __name__ == '__main__':
    try:
        node = TurtleSimDetection()
        node.run()
    except rospy.ROSInterruptException:
        pass
