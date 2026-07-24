import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from tf2_ros.transform_broadcaster import TransformBroadcaster
from geometry_msgs.msg import TransformStamped
from turtlesim.msg import Pose

def euler_to_quaternion_pure(roll, pitch, yaw):
    cr = np.cos(roll * 0.5)
    sr = np.sin(roll * 0.5)
    cp = np.cos(pitch * 0.5)
    sp = np.sin(pitch * 0.5)
    cy = np.cos(yaw * 0.5)
    sy = np.sin(yaw * 0.5)
    qw = cr * cp * cy + sr * sp * sy
    qx = sr * cp * cy - cr * sp * sy
    qy = cr * sp * cy + sr * cp * sy
    qz = cr * cp * sy - sr * sp * cy

    return qx, qy, qz, qw

class M_pub(Node):
    def __init__(self):
        super().__init__("massage_pub")  # 노드 이름
        # timer 등록
        self.transformation = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0]
        self.transformation2 = [1.0, 1.0, 1.0, 1.0, 0.0, 0.0, 1.0]
        self.tf_broadcaster = TransformBroadcaster(self)
        self.create_subscription(Pose,
                                 "turtle1/pose",
                                 self.pose_callback,
                                 10
                                 )

    def pose_callback(self, msg: Pose):
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "world"
        t.child_frame_id = "turtle1"
        x, y, z, w = euler_to_quaternion_pure(0.0,
                                              0.0,
                                              msg.theta
                                              )

        t.transform.translation.x = msg.x
        t.transform.translation.y = msg.y
        t.transform.translation.z = 0.0
        t.transform.rotation.x = x
        t.transform.rotation.y = y
        t.transform.rotation.z = z
        t.transform.rotation.w = w
        
        self.tf_static_broadcaster.sendTransform([t]) #tf 토픽에 발행

        




def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = M_pub()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        node.get_logger().info("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()
