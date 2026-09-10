from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    config_file = PathJoinSubstitution([
        FindPackageShare("m1ct_d2"),
        "params",
        "m1ct_d2.yaml"])
    return LaunchDescription(
        [
            DeclareLaunchArgument(
                "config",
                default_value=config_file,
                description="Yaml config file"
                ),
            Node(
                package="m1ct_d2",
                executable="m1ct_d2",
                output="both",
                parameters=[LaunchConfiguration("config")]
            )
        ]
    )