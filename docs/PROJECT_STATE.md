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

## Verified Robot Control Milestone

- UR5e simulation launched using the installed
  `ur_simulation_gz` package.
- `joint_state_broadcaster`: active.
- `scaled_joint_trajectory_controller`: active.
- Six UR5e joint states published on `/joint_states`.
- Six joint position command interfaces available and claimed.
- A trajectory targeted `shoulder_pan_joint` at 0.10 rad.
- The subsequent joint-state message reported approximately 0.10 rad.
- Visual movement and end-to-end MoveIt planning remain to be verified.

## Next Task

Verify the installed UR MoveIt launch configuration, start MoveIt
with the running simulation as appropriate, and test a planned motion.

## Verified MoveIt Planning and Execution Milestone

- The combined UR5e Gazebo and MoveIt launch starts successfully.
- RViz displays the UR5e model and the `ur_manipulator` planning group.
- MoveIt successfully plans a trajectory.
- `joint_state_broadcaster` is active.
- `scaled_joint_trajectory_controller` is active.
- MoveIt is connected to the scaled trajectory controller action.
- A planned motion was executed, and visible robot movement was
  confirmed in Gazebo.
- A subsequent `/joint_states` message reported
  `shoulder_pan_joint` at approximately 0.254 radians.
- Exact target accuracy has not yet been verified.

## Next Task

Design and integrate a simulated gripper for the UR5e, then
develop and test a basic pick-and-place workflow for SortiBot AI.
