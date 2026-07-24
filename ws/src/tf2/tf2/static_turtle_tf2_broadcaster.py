import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from tf2_ros.static_transform_broadcaster import StaticTransformBroadcaster
from geometry_msgs.msg import TransformStamped

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
        self.tf_static_broadcaster = StaticTransformBroadcaster(self)
        self.make_transform()

    def make_transform(self):
        # tf데이터 저장
        t = TransformStamped()
        t.header.stamp = self.get_clock().now().to_msg()
        t.header.frame_id = "world" #중요하다고함(상위 tf2명시)
        t.child_frame_id = "joint1"
        x, y, z, w = euler_to_quaternion_pure(*self.transformation[3:])

        t.transform.translation.x = self.transformation[0]
        t.transform.translation.y = self.transformation[1]
        t.transform.translation.z = self.transformation[2]
        t.transform.rotation.x = x
        t.transform.rotation.y = y
        t.transform.rotation.z = z
        t.transform.rotation.w = w

        x, y, z, w = euler_to_quaternion_pure(*self.transformation2[3:])
        t2 = TransformStamped()
        t2.header.stamp = self.get_clock().now().to_msg()
        t2.header.frame_id = "joint1" #중요하다고함(상위 tf2명시)
        t2.child_frame_id = "joint2"
        t2.transform.translation.x = self.transformation[0]
        t2.transform.translation.y = self.transformation[1]
        t2.transform.translation.z = self.transformation[2]
        t2.transform.rotation.x = x
        t2.transform.rotation.y = y
        t2.transform.rotation.z = z
        t2.transform.rotation.w = w
        
        self.tf_static_broadcaster.sendTransform([t, t2]) #tf 토픽에 발행



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
