from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription(
        [
            Node(package="ros", executable="class_pub"),
            Node(package="ros", executable="class_sub"),
        ]
    )