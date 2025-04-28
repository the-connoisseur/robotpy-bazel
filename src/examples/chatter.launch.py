from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(executable="src/examples/talker", name="talker"),
            Node(executable="src/examples/listener", name="listener"),
        ]
    )
