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
Teleoperation refers to a system that allows a robot or vehicle to be remotely controlled using an interface, such as a controller or app. In the context of robotics, teleoperation is used to send motion commands and sensor control from a remote station to a robot. This is useful when the robot is in an environment where direct interaction is difficult or dangerous for humans. In platforms like ROS, teleoperation is commonly used to enable manual control of robots, such as turtles in simulators or mobile robots in the real world.

### draw_square.py
This code draws a square using a robot in a ROS environment. The code creates a ROS node called draw_square and publishes movement commands to the topic to control the turtle. The process consists of moving the turtle forward for 1 second, then turning 90 degrees and repeating this cycle four times to complete a square. After the square is drawn, the turtle moves forward once more to return to the starting point and then stops.

![Draw a square](https://github.com/AntonioXicali101/Laboratorio_LRT4102/blob/21ee6d8cb3a91c9c9737f64a9433ff470653584a/Lab2/media/square.png)


### draw_triangle.py
This code draws a triangle using a robot in a ROS environment. The draw_triangle node publishes movement commands to the topic to control the turtle. The robot moves forward for 1 second, then turns 120 degrees and repeats this process three times to complete a triangle. After drawing the triangle, the turtle moves forward to the starting point and then stops.

![Draw a triangle](https://github.com/AntonioXicali101/Laboratorio_LRT4102/blob/69a84f0226a0e691ce45832ab7da74bab49cbc2d/Lab2/media/triangle.png)




## ADVANCED
- Position control for turtlesim (P).
- Position control for turtlesim (P).
- Position control for turtlesim (P).

### turtle_pc.py
This code uses a proportional controller to move the turtle in turtlesim to a user-specified (x, y) position. It subscribes to the turtle's pose topic and publishes velocity commands to guide its movement. The program prompts the user for the x and y coordinates, then calculates the position error and adjusts the turtle's movement using proportional control to reach the destination.

### turtle_pdc.py
This code implements a PD (Proportional-Derivative) controller to move the turtle in turtlesim to a user-specified (x, y) position. The PD controller calculates the control signal taking into account both the current error and the rate of change of that error, providing smoother motion. The node subscribes to the turtle's pose and continuously updates the command until the turtle reaches the desired destination.

### turtle_pidc.py
This code uses a PID (Proportional-Integral-Derivative) controller to guide the turtle in TurtleSim to a user-supplied (x, y) position. It calculates proportional, integral, and derivative terms for linear (distance) and angular (orientation) movements. The code prompts the user for the target coordinates, and the PID control loop adjusts the necessary commands to accurately navigate the turtle to the target.
