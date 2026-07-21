import rclpy
from geometry_msgs.msg import Twist
from rclpy.node import Node

class Move_turtle(Node):
    def __init__(self):
        super().__init__('move_turtle') #노드이름

        #타이머등록
        self.create_timer(0.1, self.timer_callback)
        self.pub = self.create_publisher(Twist, 'turtle1/cmd_vel', 10)
        self.count = 0.0


    def timer_callback(self):
        msg = Twist()   #dds에 보낼 객체 초기화
        msg.linear.x = 0.0 + self.count
        msg.angular.z = 1.0
        self.pub.publish(msg)   #dds로 보낼 기능 수행
        

def main(args=None):
    rclpy.init(args=args)   #rmw 활성화
    node = Move_turtle()