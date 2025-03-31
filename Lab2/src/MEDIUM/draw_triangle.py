#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def draw_triangle():
    rospy.init_node('draw_triangle', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    move_cmd = Twist()

    for _ in range(3):  # Lados del triángulo
        # Mover hacia adelante
        move_cmd.linear.x = 2.0  # Velocidad hacia adelante
        move_cmd.angular.z = 0.0  # Sin rotación
        pub.publish(move_cmd)
        rospy.loginfo("Moviendo hacia adelante")
        time.sleep(1)  # Espera 1 segundos para que el robot se mueva

        # Girar 120 grados después de cada línea
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 2.09439510239319  # 120 grados (2π/3 radianes)
        pub.publish(move_cmd)
        rospy.loginfo("Girando 120 grados")
        time.sleep(1)  # Espera 1 segundo para completar el giro

    # Después de completar el triángulo, hacer una línea más hasta el inicio
    move_cmd.linear.x = 2.0  # Avanzar una vez más
    move_cmd.angular.z = 0.0  # Sin rotación
    pub.publish(move_cmd)
    rospy.loginfo("Haciendo una línea más hasta el punto de inicio")
    time.sleep(2)  # Espera 2 segundos para avanzar hasta el inicio

    # Detener al final
    move_cmd.linear.x = 0.0
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)
    rospy.loginfo("Triángulo completado y deteniendo la tortuga")

if __name__ == '__main__':
    try:
        draw_triangle()
    except rospy.ROSInterruptException:
        pass