from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.actions import LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import ThisLaunchFileDir
from launch_ros.actions import Node

def generate_launch_description():
    gazebo_package = get_package_share_directory('mini_pupper_gazebo')
    gazebo_simulation = IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [gazebo_package, '/launch/gazebo.launch.py']),
                launch_arguments={
                    "world": gazebo_package + "/worlds/house.world"
                }.items(),
    ),
    
    stt_action = Node(
        package="actions",
        executable="stt_action"
    ),

    
    return LaunchDescription([
        LogInfo(msg=['Execute all of nodes']),
        gazebo_simulation,
        stt_action,
        
        # launch.actions.TimerAction(period=30.0, actions=[load_joint_state_controller,
        #                                                      load_joint_trajectory_effort_controller,
        #                                                      contact_sensor]),
        
    ])