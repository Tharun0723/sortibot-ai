from pathlib import Path

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue
from launch_ros.substitutions import FindPackageShare

from moveit_configs_utils import MoveItConfigsBuilder


def generate_launch_description():
    use_sim_time = LaunchConfiguration("use_sim_time")
    launch_rviz = LaunchConfiguration("launch_rviz")

    description_file = Path(
        "/home/tharun/sortibot-ai/sortibot_description/urdf/"
        "sortibot_ur5e_gripper.urdf.xacro"
    )
    semantic_file = Path(
        "/home/tharun/sortibot-ai/sortibot_description/urdf/"
        "sortibot.srdf.xacro"
    )

    robot_description = {
        "robot_description": ParameterValue(
            Command([
                FindExecutable(name="xacro"),
                " ",
                str(description_file),
                " ",
                "ur_type:=ur5e",
                " ",
                'simulation_controllers:=/home/tharun/sortibot-ai/'
                "install/sortibot_description/share/sortibot_description/"
                "config/sortibot_controllers.yaml",
            ]),
            value_type=str,
        )
    }

    moveit_config = (
        MoveItConfigsBuilder(
            robot_name="sortibot_ur5e",
            package_name="ur_moveit_config",
        )
        .robot_description_semantic(
            file_path=str(semantic_file),
        )
        .robot_description_kinematics(
            file_path="config/kinematics.yaml",
        )
        .joint_limits(file_path="config/joint_limits.yaml")
        .planning_pipelines(pipelines=["ompl"])
        .to_moveit_configs()
    )

    controllers = {
        "moveit_controller_manager":
            "moveit_simple_controller_manager/MoveItSimpleControllerManager",
        "moveit_simple_controller_manager": {
            "controller_names": ["scaled_joint_trajectory_controller"],
            "scaled_joint_trajectory_controller": {
                "type": "FollowJointTrajectory",
                "action_ns": "follow_joint_trajectory",
                "default": True,
                "joints": [
                    "shoulder_pan_joint",
                    "shoulder_lift_joint",
                    "elbow_joint",
                    "wrist_1_joint",
                    "wrist_2_joint",
                    "wrist_3_joint",
                ],
            },
        },
        "trajectory_execution": {
            "allowed_execution_duration_scaling": 1.2,
            "allowed_goal_duration_margin": 0.5,
            "allowed_start_tolerance": 0.02,
            "execution_duration_monitoring": False,
        },
    }

    move_group = Node(
        package="moveit_ros_move_group",
        executable="move_group",
        output="screen",
        parameters=[
            robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
            moveit_config.planning_pipelines,
            moveit_config.joint_limits,
            controllers,
            {"use_sim_time": use_sim_time},
        ],
    )

    rviz = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2_moveit",
        output="screen",
        arguments=[
            "-d",
            str(
                Path("/opt/ros/jazzy/share/ur_moveit_config/config/")
                / "moveit.rviz"
            ),
        ],
        parameters=[
            robot_description,
            moveit_config.robot_description_semantic,
            moveit_config.robot_description_kinematics,
            moveit_config.planning_pipelines,
            moveit_config.joint_limits,
            {"use_sim_time": use_sim_time},
        ],
        condition=None,
    )

    return LaunchDescription([
        DeclareLaunchArgument("use_sim_time", default_value="true"),
        DeclareLaunchArgument("launch_rviz", default_value="true"),
        move_group,
        rviz,
    ])
