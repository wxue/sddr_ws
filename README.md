# sddr_ws
simple differential drive robot - ROS

## Environment

##### ROS version: /opt/ros/kinetic/


## Get it to demo

1. In /sddr_ws, source to work space
```
source devel/setup.bash
```

2. 


### Task:

Using ROS Kinetic Kame, create a catkin package with the following functionality:

1. Declares dependencies (if you use other ROS packages)

2. Contains documentation about the launchers and parameters if any.

3. Can be built with catkin_make

4. Contains the URDF description of a simple differential drive robot

5. Contains a launcher to view the robot model in RViz

6. OPTIONAL: Contains a launcher to simulate the robot in Gazebo and allows for the following functionality via launcher parameters:

    1. Keyboard teleop mode, where the robot motion can be commanded by the keyboard.

    2. Circle mode, where the robot drives incessantly along a circle of a user-defined diameter (passed as a parameter in m)

    3. Square mode, where the robot drives incessantly along a square of user-defined side-length (passed as a parameter in m)
