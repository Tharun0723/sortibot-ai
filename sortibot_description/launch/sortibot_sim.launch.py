from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():
    ur_simulation_share = FindPackageShare("ur_simulation_gz")
    sortibot_share = FindPackageShare("sortibot_description")

    simulation_launch = PathJoinSubstitution([
        ur_simulation_share,
        "launch",
        "ur_sim_control.launch.py",
    ])

    robot_description = PathJoinSubstitution([
        sortibot_share,
        "urdf",
        "sortibot_ur5e_gripper.urdf.xacro",
    ])

    controllers_config = PathJoinSubstitution([
        sortibot_share,
        "config",
        "sortibot_controllers.yaml",
    ])

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(simulation_launch),
            launch_arguments={
                "ur_type": "ur5e",
                "description_file": robot_description,
                "controllers_file": controllers_config,
                "initial_joint_controller": "scaled_joint_trajectory_controller",
                "launch_rviz": "true",
                "gazebo_gui": "true",
            }.items(),
        ),
    ])
