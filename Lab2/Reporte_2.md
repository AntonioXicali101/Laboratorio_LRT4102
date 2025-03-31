# Report_2_174527

## BASIC
- Create a ros package called Prcaticas_lab with the dependencies rospy, roscpp & std_msgs. 
- Insert the files listener.py & talker.py
- Compile the package.
- Run the talker file.
- Run the listener file.
- Conclude about its functioning.

### talker.py
The talker.py file is a node that acts as a publisher. Its main function is to send messages to a specific topic. In this case, the node creates a message and periodically publishes it to a specific topic. The node follows a continuous cycle, sending the message at regular intervals until it stops.The talker.py file is a node that acts as a publisher. Its main function is to send messages to a specific topic. In this case, the node creates a message and periodically publishes it to a specific topic. The node follows a continuous cycle, sending the message at regular intervals until it stops.

![Descripción de la imagen](https://github.com/AntonioXicali101/Laboratorio_LRT4102/blob/c722a0bb625e64d56a408d8d1038058936e2a49e/Lab2/media/talker.png)


### listener.py
The listening.py file is a node that acts as a subscriber. This node subscribes to a specific topic and waits to receive messages published by the talker.py node. Each time it receives a message, the node executes a callback function that processes the message content. In this case, the received message is displayed on the subscriber's terminal. This subscription and reception process enables communication between different nodes in a distributed system.

![Descripción de la imagen](https://github.com/AntonioXicali101/Laboratorio_LRT4102/blob/2945d33b8a92d1e4b8cd6ff05ad89878aa967ee5/Lab2/media/listener.png)

## MEDIUM
- Create a keyboard control for turtlesim.
- Draw a square and a equilateral triangule withb turtlesim (No control).

### teleop.py
This code allows keyboard teleoperation of the turtlesim turtle. It captures key presses (without needing to press Enter) and maps 
specific keys to linear and angular velocity commands. For example, keys such as 'w', 'a', 's', and 'd' are used for translational 
movement, while 'o' and 'i' control rotation (right and left, respectively). The node publishes these commands to the `/turtle1/
cmd_vel` topic.

### CyT.py
This code demonstrates how to draw geometric shapes (such as a triangle and a square) using turtlesim. It calculates vertex coordinates 
based on preset dimensions, validates that the vertices are within the work area, and then moves the turtle sequentially between them 
to draw the shape. Additionally, it includes functions to clear the screen and teleport the turtle back to its initial position after 
drawing.

## ADVANCED
- Position control for turtlesim (P).
- Position control for turtlesim (P).
- Position control for turtlesim (P).

### turtle_pc.py
This code uses a **proportional controller** to move the turtlesim turtle to a user-specified (x, y) position. It subscribes to the 
turtle's pose and publishes velocity commands to drive the turtle. The program prompts the user for x and y coordinates, then 
calculates the error in position and adjusts the turtle's movement accordingly using proportional control.

### turtle_pdc.py
This code implements a **PD (Proportional-Derivative) controller** to move the turtlesim turtle to a user-specified (x, y) position. 
The PD controller computes the control signal based on both the current error and the rate of change of the error. This results in 
smoother movement. The node subscribes to the turtle's pose and continuously updates the command until the turtle reaches the desired 
position.

### turtle_pidc.py
This code uses a **PID (Proportional-Integral-Derivative) controller** to move the turtlesim turtle to a user-specified (x, y) 
position. It calculates the proportional, integral, and derivative terms for both the linear (distance) and angular (orientation) 
movements. The code prompts the user for the target coordinates, and the PID control loop computes the necessary commands to drive the 
turtle accurately to the goal.
