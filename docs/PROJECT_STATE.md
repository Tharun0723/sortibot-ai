# SortiBot AI — Project State

## Goal
Build a simulation-based intelligent robotic e-waste sorting cell.

## Verified environment
- OS: Ubuntu 24.04.5 LTS on WSL2
- Kernel: 6.18.33.2-microsoft-standard-WSL2
- CPU: Intel Core i7-8750H, 6 cores / 12 logical CPUs
- WSL-visible memory: 15 GiB
- WSL filesystem: approximately 949 GB free at inspection
- GPU: NVIDIA Quadro P3200, 6 GB VRAM, visible through nvidia-smi
- Python: 3.12.3
- ROS 2: Jazzy
- Gazebo Sim: 8.15.0
- Git: 2.43.0

## Verified software availability
- ROS packages discovered: rclcpp, rclpy, robot_state_publisher,
  ros_gz_sim, ros_gz_bridge, ros2_control, ros2_controllers,
  xacro and tf2_ros.
- Python libraries discovered: OpenCV and NumPy.
- PyTorch: not installed in the tested Python environment.
- Ultralytics: not installed in the tested Python environment.
- MoveIt 2: not found in the package discovery check.
- CUDA-enabled PyTorch inference: not yet tested.

## Repository boundaries
- Planned repository: sortibot-ai
- Local directory: ~/sortibot-ai
- Initial branch: main
- Existing project: ~/autonomous-ai-search-robot
- Existing project must remain separate and unmodified by SortiBot work.

## Completed
- Phase 0: initial OS, CPU, memory, disk, GPU, ROS, Gazebo,
  Git and existing-project inspection.
- Initial repository scaffold: pending verification.

## Outstanding decisions
- Verify GPU compute capability for the selected AI framework.
- Confirm MoveIt 2 compatibility and availability.
- Select the robotic arm, gripper and camera model.
- Define simulation and perception acceptance tests.
- Choose AI coding and dashboard development tools based on actual needs.

## Next task
Verify the repository files and initial Git commit.
Do not install dependencies or begin simulation development
until the scaffold has been verified.
