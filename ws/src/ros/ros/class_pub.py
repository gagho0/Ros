#param_launch.py

import os

from ament_index_python import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    param_dir = LaunchConfiguration(
        "param_dir", 
        default=os.path,join(
            get_package_share_directory("ros"), 
            "param", 
            "my_param.yaml"
        )
    )
    return LaunchDescription(
        [
            
            Node(
                package='ros',
                executable='my_param',
                parameters=[{"my_param": "내가 만든 쿠키 너를위해 구웠지"}],