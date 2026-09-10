# M1CT D2 ROS 2 LiDAR Driver

ROS 2 driver for 2D M1CT D2 LiDAR, corrected occurring errors and added a launch file for easy use. Tested with ROS 2 Jazzy.


## Installation

Install dependencies and build:

```bash
source /opt/ros/jazzy/setup.bash
cd ~/lidar_ws
rosdep install --from-paths src --ignore-src -r -y
colcon build --packages-select m1ct_d2 --symlink-install
source install/setup.bash
```

## Configuration

Parameters are stored in `params/m1ct_d2.yaml`.

Check the serial device path on your machine:

```yaml
c1ct_d2:
  ros__parameters:
    port: /dev/serial/by-id/usb-1a86_USB_Serial-if00-port0
    baudrate: 230400
    frame_id: laser_link
    version: 4
```

```bash
ls -l /dev/serial/by-id/
```

Update `port` if necessary.

## Running

Launch the driver with its installed configuration:

```bash
source ~/lidar_ws/install/setup.bash
ros2 launch m1ct_d2 start_lidar.launch.py
```

Use a different configuration file:

```bash
ros2 launch m1ct_d2 start_lidar.launch.py \
  config:=/absolute/path/to/config.yaml
```

## Nodes

One executable creates two ROS 2 nodes:

- `c1ct_d2`: initializes the LiDAR and publishes scan data.
- `m1ct_d2`: subscribes to `lidar_status` for control commands.
