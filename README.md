# SortiBot AI

An intelligent, AI-powered robotic e-waste sorting system
developed as a simulation and research prototype.

## Project goals

- Simulate a robotic sorting cell with an arm, gripper, camera,
  conveyor and sorting bins.
- Detect and classify electronic-waste objects using computer vision.
- Plan and validate pick-and-place operations.
- Handle uncertain classifications and failed operations safely.
- Record sorting results and display system performance.
- Evaluate the system using reproducible tests and documented metrics.

## Planned technology stack

- ROS 2 Jazzy
- Gazebo Harmonic
- Python and C++
- OpenCV and a suitable pretrained detection model
- MoveIt 2, subject to compatibility and installation checks
- FastAPI and a web dashboard, introduced in later milestones

## Project status

Phase 0 environment inspection is complete.
Simulation, perception, manipulation and dashboard implementation
have not yet been verified or completed.

## Scope

This is a simulation and research prototype, not a certified
real-world waste-handling system.

## Documentation

See [Project State](docs/PROJECT_STATE.md) for the verified
environment, current progress and next task.
