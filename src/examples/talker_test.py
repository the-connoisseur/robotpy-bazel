import time
import unittest

import rclpy
import launch_testing.markers
import std_msgs.msg
from launch import LaunchDescription
from launch.actions import TimerAction
from launch_ros.actions import Node
from launch_testing.actions import ReadyToTest

@launch_testing.markers.keep_alive
def generate_test_description():
    return LaunchDescription([
        Node(
            executable = 'src/examples/talker',
            parameters = [
                {
                    'timer_period_sec': 0.01
                }
            ],
            arguments = [
                "--ros-args",
                "--log-level",
                "warn"
            ],
        ),
        # The talker node seems to take ~half a second to start publishing. Since our
        # test cases expect talker to be in steady state (already publishing
        # periodically), have the test node launch a full second after the talker to be
        # on the safe side.
        # TODO: Is there a more deterministic way to do this?
        TimerAction(
            period = 1.0,
            actions = [
                ReadyToTest()
            ]
        ),
    ])

class TalkerTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rclpy.init()

    @classmethod
    def tearDownClass(cls):
        rclpy.shutdown()

    def setUp(self):
        self.node = rclpy.create_node('talker_test')

    def tearDown(self):
        self.node.destroy_node()

    def test_talker_publish_frequency(self, proc_output):
        """Tests that the talker publishes at the frequency specified via the parameter."""
        messages_rx = []
        subscriber = self.node.create_subscription(std_msgs.msg.String, 'chatter', lambda message: messages_rx.append(message), 10)

        try:
            # Run for 1 second and verify that we got ~100 messages (once every 10ms).
            end_time = time.time() + 1
            while time.time() < end_time:
                rclpy.spin_once(self.node, timeout_sec=0.02)
            self.assertGreater(len(messages_rx), 100)
        finally:
            self.node.destroy_subscription(subscriber)
