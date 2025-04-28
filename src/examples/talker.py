import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__('talker')
        self.declare_parameter('timer_period_sec', 1.0)
        self.timer_period_sec = self.get_parameter('timer_period_sec')
        self.publisher = self.create_publisher(String, 'chatter', 10)
        self.timer = self.create_timer(self.timer_period_sec.value, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = String()
        msg.data = f'Hello, world: {self.i}'
        self.publisher.publish(msg)
        self.get_logger().info(f'Publishing: {msg.data}')
        self.i += 1

def main():
    rclpy.init()
    talker = Talker()
    try:
        rclpy.spin(talker)
    except KeyboardInterrupt:
        pass
    finally:
        talker.destroy_node()
        # TODO: Uncomment the following line once the double shutdown bug is fixed.
        # https://github.com/ros2/rclpy/issues/1081
        # rclpy.shutdown()

if __name__ == '__main__':
    main()
