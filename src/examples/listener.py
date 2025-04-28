import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class Listener(Node):
    def __init__(self):
        super().__init__('listener')
        self.create_subscription(String, 'chatter', self.listener_callback, 10)

    def listener_callback(self, msg):
        self.get_logger().debug(f'I heard {msg.data}')

def main():
    rclpy.init()
    listener = Listener()
    try:
        rclpy.spin(listener)
    except KeyboardInterrupt:
        pass
    finally:
        listener.destroy_node()
        # TODO: Uncomment the following line once the double shutdown bug is fixed.
        # https://github.com/ros2/rclpy/issues/1081
        rclpy.shutdown()

if __name__ == '__main__':
    main()
