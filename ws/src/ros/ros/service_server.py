import time

import rclpy
from rclpy.node import Node
from user_interface.srv import AddAndOdd

class service_server(Node):
    def __init__(self):
        super().__init__("message_pub")
        # timer 등록
        self.create_service(AddAndOdd, "add_server", self.add_callback)
        

    def add_callback(self, request: AddAndOdd.Request, response: AddAndOdd.Response):
        with self.lock: # race condition 이 생길것같은 부분에 with로 블록화
            response.sum = request.inta + request.intb
            time.sleep(10)
        if response.sum % 2:
            response.odd = "Two ints sum isodd"
        else:
            response.odd = "Two ints sum is not odd"
        return response

    
def main(args=None):
    rclpy.init(args=args)  # rmw 활성화
    node = service_server()
    try:
        rclpy.spin(node)  # 블럭 (무한 루프)
    except KeyboardInterrupt:
        node.get_logger().info("키보드 인터럽트")
    finally:
        node.destroy_node()


if __name__ == "__main__":
    main()
