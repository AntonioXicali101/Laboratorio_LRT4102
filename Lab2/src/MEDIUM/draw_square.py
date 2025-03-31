#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def draw_square():
    rospy.init_node('draw_square', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    move_cmd = Twist()

    # Dibujar el cuadrado
    for _ in range(4):  # lados del cuadrado
        # Mover hacia adelante
        move_cmd.linear.x = 2.0  # Velocidad hacia adelante
        move_cmd.angular.z = 0.0  # Sin rotación
        pub.publish(move_cmd)
        rospy.loginfo("Moviendo hacia adelante")
        time.sleep(1)  # Espera 1 segundos para que el robot se mueva

        # Girar 90 grados después de cada línea
        move_cmd.linear.x = 0.0
        move_cmd.angular.z = 1.57079632679489  # 90 grados (pi/2 radianes)
        pub.publish(move_cmd)
        rospy.loginfo("Girando 90 grados")
        time.sleep(1)  # Espera 1 segundo para completar el giro

    # Después de completar el cuadrado, hacer una línea adicional hacia el inicio
    move_cmd.linear.x = 2.0  # Avanzar una vez más
    move_cmd.angular.z = 0.0  # Sin rotación
    pub.publish(move_cmd)
    rospy.loginfo("Haciendo una línea más hasta el punto de inicio")
    time.sleep(2)  # Espera 2 segundos para avanzar hasta el inicio

    # Detener al final
    move_cmd.linear.x = 0.0
    move_cmd.angular.z = 0.0
    pub.publish(move_cmd)
    rospy.loginfo("Cuadrado completado y deteniendo la tortuga")

if __name__ == '__main__':
    try:
        draw_square()
    except rospy.ROSInterruptException:
        pass