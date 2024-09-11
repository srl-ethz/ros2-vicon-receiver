from launch import LaunchDescription
from launch_ros.actions import Node
from launch_ros.actions import ComposableNodeContainer
from launch_ros.descriptions import ComposableNode

def generate_launch_description():

    hostname = '10.10.10.5'
    buffer_size = 200
    topic_namespace = 'vicon'

    return LaunchDescription([
        Node(
            package='vicon_receiver', executable='vicon_client', output='screen',
            parameters=[{'hostname': hostname, 'buffer_size': buffer_size, 'namespace': topic_namespace}]
        ),

        # tf2 format:
        # x, y, z, qx, qy, qz, qw, parent, child
        # with transformation child->parent (i.e. T_PC)

        # Parent: ENU, Child: NED. 
        # Transform NED->ENU: intrinsic XYZ 180° pitch, -90° yaw
        Node(package = "tf2_ros", 
            executable = "static_transform_publisher",
            arguments = ["0", "0", "0", "0.7071068", "0.7071068", "0", "0", "world", "world_ned"])
    ])
