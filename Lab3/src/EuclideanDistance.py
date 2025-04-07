#!/usr/bin/env python3
import rospy
from turtlesim.srv import TeleportAbsolute
from turtlesim.msg import Pose
import math

class TurtleMovementController:
    def __init__(self):
        rospy.init_node('turtle_movement_controller')
        
        # Espera a que el servicio de teletransportación para turtle1 esté disponible
        rospy.wait_for_service('/turtle1/teleport_absolute')
        self.teleport_service = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
        
        # Se suscribe al tópico de la pose de turtle1 para obtener su posición actual
        rospy.Subscriber('/turtle1/pose', Pose, self.update_pose)
        
        self.current_pose = None
        self.rate = rospy.Rate(10)

    def update_pose(self, pose):
        # Actualiza la pose actual de la tortuga
        self.current_pose = pose

    def get_user_input_for_goal(self):
        # Solicita al usuario las coordenadas y orientación deseadas (en radianes)
        x_coord = float(input("Ingresa la coordenada x deseada: "))
        y_coord = float(input("Ingresa la coordenada y deseada: "))
        orientation = float(input("Ingresa la orientación deseada (en radianes): "))
        return x_coord, y_coord, orientation

    def calculate_dist_and_angle(self, target_x, target_y):
        """
        Calcula y muestra:
         - DTG: Distancia euclidiana entre la pose actual y el objetivo.
         - ATG: Ángulo hacia el objetivo usando atan2.
         
         Explicación de mapeo de velocidades (si se aplicara movimiento):
           - La velocidad lineal es proporcional a DTG (la tortuga se mueve más rápido cuando está más lejos)
           - La velocidad angular es proporcional a (ATG - orientación actual) (para corregir la dirección)
        """
        if self.current_pose is None:
            rospy.loginfo("La pose actual no está disponible aún.")
            return None, None
        dist_to_goal = math.sqrt((target_x - self.current_pose.x)**2 + (target_y - self.current_pose.y)**2)
        angle_to_goal = math.atan2(target_y - self.current_pose.y, target_x - self.current_pose.x)
        rospy.loginfo("DTG: %.2f, ATG: %.2f", dist_to_goal, angle_to_goal)
        return dist_to_goal, angle_to_goal

    def start(self):
        # Bucle infinito: pide las coordenadas del objetivo al usuario y teletransporta turtle1
        while not rospy.is_shutdown():
            goal_x, goal_y, goal_theta = self.get_user_input_for_goal()
            # Calcula y muestra DTG y ATG basados en la pose actual de turtle1
            self.calculate_dist_and_angle(goal_x, goal_y)
            # Teletransporta a turtle1 a la posición deseada directamente
            try:
                self.teleport_service(goal_x, goal_y, goal_theta)
                rospy.loginfo("Tortuga teletransportada a (%.2f, %.2f) con orientación %.2f",
                              goal_x, goal_y, goal_theta)
            except rospy.ServiceException as e:
                rospy.logerr("Fallo al llamar al servicio de teletransportación: %s", e)
            rospy.sleep(2)

if __name__ == '__main__':
    try:
        movement_controller = TurtleMovementController()
        movement_controller.start()
    except rospy.ROSInterruptException:
        pass
