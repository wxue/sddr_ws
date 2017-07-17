# sddr_ws
simple differential drive robot - ROS

## Environment

##### ROS version: /opt/ros/kinetic/

Install Dependences:
```
sudo apt-get install ros-kinetic-desktop-full

sudo apt-get install ros-kinetic-turtlebot-gazebo 

sudo apt-get install ros-kinetic-turtlebot-teleop

rosdep update
```

Check env:
```
printenv | grep ROS
```
> ROS_ROOT=/opt/ros/kinetic/share/ros
ROS_PACKAGE_PATH=/home/weiyu/Dev/ROS/sddr_ws/src:/opt/ros/kinetic/share
ROS_MASTER_URI=http://127.0.0.1:11311
OLDPWD=/home/weiyu/Dev/ROS
LD_LIBRARY_PATH=/home/weiyu/Dev/ROS/sddr_ws/devel/lib:/opt/ros/kinetic/lib
PWD=/home/weiyu/Dev/ROS/sddr_ws
ROS_HOSTNAME=localhost
ROSLISP_PACKAGE_DIRECTORIES=/home/weiyu/Dev/ROS/sddr_ws/devel/share/common-lisp
ROS_DISTRO=kinetic
ROS_IP=127.0.0.1
CMAKE_PREFIX_PATH=/home/weiyu/Dev/ROS/sddr_ws/devel:/opt/ros/kinetic
ROS_ETC_DIR=/opt/ros/kinetic/etc/ros


## Get it to demo

1. In /sddr_ws, source to work space
```
source devel/setup.bash
```

2. build packages
```
cd /sddr_ws

catkin_make
```

3. launch robot model in RViz
```
roslaunch diff_drive_rviz diff_drive_rviz.launch
```

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
